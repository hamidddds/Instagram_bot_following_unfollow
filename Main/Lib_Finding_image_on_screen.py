import os
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import time


def find_all_templates(template_path, search_region, match_threshold):
    # Take a screenshot of the specified region
    screenshot_pil = pyautogui.screenshot(region=search_region)

    # Convert the screenshot from PIL format to a NumPy array and then to BGR for OpenCV
    screenshot_bgr = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)

    # Read the template image in grayscale
    template_gray = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    template_height, template_width = template_gray.shape

    # Perform template matching
    match_result = cv2.matchTemplate(
        screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Identify all locations where the match exceeds the threshold
    match_locations = np.where(match_result >= match_threshold)

    # Collect rectangles representing matching regions
    rectangles = []
    for location in zip(*match_locations[::-1]):
        rect = [int(location[0]), int(location[1]),
                template_width, template_height]
        rectangles.append(rect)
        rectangles.append(rect)  # Add twice for groupRectangles

    # Group overlapping rectangles
    grouped_rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.5)

    # Return found regions and the screenshot
    return grouped_rectangles, screenshot_bgr


def get_chrome_region(vertical_ratio=1, horizontal_ratio=1, horizontal_position=None, vertical_position=None):
    chrome_windows = [win for win in gw.getWindowsWithTitle(
        'Google Chrome') if win.visible]
    if chrome_windows:
        # Assuming the first visible Chrome window is the target
        chrome_window = chrome_windows[0]
        region_height = round(chrome_window.height * vertical_ratio)
        region_width = round(chrome_window.width * horizontal_ratio)
        region_top = chrome_window.top
        region_left = chrome_window.left

        if horizontal_position == "right":
            region_left = chrome_window.left + region_width
        if vertical_position == "down":
            region_top = chrome_window.top + region_height

        return (region_left, region_top, region_width, region_height)
    else:
        raise Exception("No visible Chrome window found")


def find_images(template_path, search_region=None, match_threshold=None):
    if match_threshold is None:
        match_threshold = 0.8  # Default threshold
    if search_region is None:
        search_region = get_chrome_region(
            1, 1/2, "right", "down")  # Default region

    matching_regions, screenshot_bgr = find_all_templates(
        template_path, search_region, match_threshold)

    # Save the screenshot with found regions
    screenshot_filename = os.path.join("screenshots", "matched_screenshot.png")
    cv2.imwrite(screenshot_filename, screenshot_bgr)

    # List to hold the positions of found templates
    positions = []

    # Convert match rectangles to screen coordinates
    if len(matching_regions) > 0:
        for rect in matching_regions:
            screen_x = search_region[0] + rect[0] + rect[2] // 2
            screen_y = search_region[1] + rect[1] + rect[3] // 2
            positions.append((screen_x, screen_y))
            # Uncomment the lines below to move the mouse to each found template
            # pyautogui.moveTo(screen_x, screen_y)
            # time.sleep(1)
            # print(f"Mouse moved to template at: {rect}")
    else:
        return None

    # Uncomment to see where the screenshot was saved
    # print(f"Screenshot saved as {screenshot_filename}")

    return positions  # Return the list of found positions


# Create screenshots directory if it doesn't exist
# if not os.path.exists("screenshots"):
#     os.makedirs("screenshots")

# Example usage of find_images function
positions = find_images(r'Images\others.png')
print("Positions of found templates:", positions)
