import pygetwindow as gw
from PIL import ImageGrab
import time


def convertor(self):
    # Get Chrome window details
    chrome_window = gw.getWindowsWithTitle('Chrome')[0]
    chrome_x, chrome_y = chrome_window.left, chrome_window.top
    chrome_width, chrome_height = chrome_window.width, chrome_window.height

    # Convert coordinates to be relative to the Chrome window
    x1 = chrome_x + int((chrome_width - 420) / 2) - 10
    y1 = chrome_y + int((chrome_height - 450) / 2) + 60
    x2 = x1 + 400  # width of the window
    y2 = y1 + 430  # height of the window

    return (x1, y1, x2, y2)


time.sleep(1)
# Example usage
bbox = convertor(None)  # Pass 'None' or the appropriate instance if needed
image = ImageGrab.grab(bbox)

# To display the image (optional)
image.show()
