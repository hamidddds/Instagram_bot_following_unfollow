import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import time


def find_all_templates(image_path, region, threshold=0.8):
    # Take a screenshot of the region
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # Read the template in grayscale
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    template_height, template_width = template.shape

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    # Find all locations where the match is above the threshold
    locations = np.where(result >= threshold)

    # Get the coordinates of the matching regions
    rectangles = []
    for loc in zip(*locations[::-1]):
        rect = [int(loc[0]), int(loc[1]), template_width, template_height]
        rectangles.append(rect)
        # Adding the rectangle twice to handle groupRectangles
        rectangles.append(rect)

    # Group overlapping rectangles (if any)
    rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.5)

    return rectangles, screenshot_np  # Returning the screenshot as well


def get_chrome_region():
    chrome_windows = [win for win in gw.getWindowsWithTitle(
        'Google Chrome') if win.visible]
    if chrome_windows:
        # Assuming you want the first Chrome window
        chrome_window = chrome_windows[0]
        return (chrome_window.left, chrome_window.top, chrome_window.width, chrome_window.height)
    else:
        raise Exception("No visible Chrome window found")


def FindImages(path, region=None, screenshot_filename='screenshot.png'):
    if region is None:
        region = get_chrome_region()

    FollowButtons, screenshot_np = find_all_templates(
        path, region, threshold=0.8)

    # Save the screenshot
    cv2.imwrite(screenshot_filename, screenshot_np)

    # Move the mouse to each found button and wait 1 second
    if len(FollowButtons) > 0:
        for rect in FollowButtons:
            # Adjust the coordinates to the actual screen
            screen_x = region[0] + rect[0] + rect[2] // 2
            screen_y = region[1] + rect[1] + rect[3] // 2
            pyautogui.moveTo(screen_x, screen_y)
            time.sleep(1)
            print(f"Mouse moved to follow button at: {rect}")
    else:
        print("No follow buttons found.")

    print(f"Screenshot saved as {screenshot_filename}")


# Example of how to call this main function from another file:
# main('path_to_image.png')
