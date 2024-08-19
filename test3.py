import pyautogui
import numpy as np
import cv2
import time


def is_plain_color(region):
    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)

    # Convert the screenshot to a NumPy array
    screenshot_np = np.array(screenshot)

    # Convert the image from RGB to BGR (as OpenCV uses BGR format)
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Save the screenshot using OpenCV
    cv2.imwrite("screenshot_region.png", screenshot_bgr)

    # Get the unique colors in the image
    unique_colors = np.unique(
        screenshot_bgr.reshape(-1, screenshot_bgr.shape[2]), axis=0)

    # Check if there's only one unique color in the image
    if len(unique_colors) == 1:
        return True  # The region is plain color
    else:
        return False  # The region has something inside


time.sleep(1)

# Example usage
region1 = (289, 151, 900, 50)
region2 = (1149, 143, 50, 600)
region3 = (1000, 333, 300, 300)

if is_plain_color(region1):
    print("The region is a plain color.")
else:
    print("The region contains other elements.")
