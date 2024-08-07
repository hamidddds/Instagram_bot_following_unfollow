import pygetwindow as gw
import pyautogui


def convertor():

    # Get Chrome window details
    chrome_window = gw.getWindowsWithTitle('Chrome')[0]
    chrome_x, chrome_y = chrome_window.left, chrome_window.top
    chrome_width, chrome_height = chrome_window.width, chrome_window.height

    # Convert coordinates to be relative to the Chrome window

    x1 = chrome_x + int(chrome_width-420)/2-10
    y1 = chrome_y + int(chrome_height-450)/2+60
    # x2 = chrome_x + x1 + 400
    # y2 = chrome_y + y1 + 430
    x2 = 400
    y2 = 430
    return (x1, y1, x2, y2)


# Define the bounding box
bbox = (700, 350, 1200, 800)

# Convert bounding box coordinates
converted_bbox = convertor(bbox)

# Take a screenshot of the specified region
screenshot = pyautogui.screenshot(region=converted_bbox)

# Save or show the screenshot
screenshot.show()  # This will open the screenshot in the default image viewer
