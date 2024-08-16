import os
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw


def find_all_templates(image_path, region, threshold):
    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # Read the template image in grayscale
    template_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    template_height, template_width = template_image.shape

    # Perform template matching
    match_result = cv2.matchTemplate(
        screenshot_gray, template_image, cv2.TM_CCOEFF_NORMED)

    # Find all locations where the match is above the threshold
    match_locations = np.where(match_result >= threshold)

    # Get the coordinates of the matching regions
    match_rectangles = []
    for location in zip(*match_locations[::-1]):
        match_rect = [int(location[0]), int(location[1]),
                      template_width, template_height]
        match_rectangles.append(match_rect)
        # Adding the rectangle twice to handle groupRectangles
        match_rectangles.append(match_rect)

    # Group overlapping rectangles (if any)
    grouped_rectangles, _ = cv2.groupRectangles(match_rectangles, 1, 0.5)

    return grouped_rectangles, screenshot_np  # Returning the screenshot as well


def get_chrome_region(region_coefficients):
    vertical_coeff = region_coefficients[0]
    horizontal_coeff = region_coefficients[1]
    horizontal_position = region_coefficients[2]
    vertical_position = region_coefficients[3]

    chrome_windows = [window for window in gw.getWindowsWithTitle(
        'Google Chrome') if window.visible]
    if chrome_windows:
        # Assuming you want the first Chrome window
        chrome_window = chrome_windows[0]
        region_height = round(chrome_window.height * vertical_coeff)
        region_width = round(chrome_window.width * horizontal_coeff)
        top_position = chrome_window.top
        left_position = chrome_window.left
        if horizontal_position == "right":
            left_position = chrome_window.left + region_width
        if vertical_position == "down":
            top_position = chrome_window.top + region_height

        return (left_position, top_position, region_width, region_height)
    else:
        raise Exception("No visible Chrome window found")


def find_images(template_path, region_coefficients=None, match_threshold=None, chrome_region=None):
    if match_threshold is None:
        match_threshold = 0.8
    if region_coefficients is None:
        region_coefficients = [1, 1, "", ""]

    if chrome_region == None:
        chrome_region = get_chrome_region(region_coefficients)

    matching_rectangles, screenshot_np = find_all_templates(
        template_path, chrome_region, match_threshold)
    screenshot_filename = os.path.join("screenshots", "screenshot.png")
    cv2.imwrite(screenshot_filename, screenshot_np)

    # List to hold the positions
    match_positions = []

    # Move the mouse to each found match and wait 1 second
    if len(matching_rectangles) > 0:
        for rect in matching_rectangles:
            # Adjust the coordinates to the actual screen
            screen_x = chrome_region[0] + rect[0] + rect[2] // 2
            screen_y = chrome_region[1] + rect[1] + rect[3] // 2
            match_positions.append((screen_x, screen_y))
            # pyautogui.moveTo(screen_x, screen_y)
            # time.sleep(1)
            # print(f"Mouse moved to matched region at: {rect}")
    else:
        return None

    return match_positions  # Return the list of positions


# Example usage:
# if not os.path.exists("screenshots"):
#     os.makedirs("screenshots")
# positions = find_images(r'Images\others.png', region_coefficients=[1, 1/2, "left", ""])
# print("Positions of found regions:", positions)
