import pyautogui
from PIL import Image, ImageDraw
import pygetwindow as gw

# Get the Chrome window by its title
chrome_window = None
for window in gw.getWindowsWithTitle('Google Chrome'):
    chrome_window = window
    break

if chrome_window is None:
    print("Chrome window not found!")
else:
    # Capture the full screen
    screenshot = pyautogui.screenshot()

    # Get the position and size of the Chrome window
    region = (chrome_window.left, chrome_window.top,
              chrome_window.width, chrome_window.height)

    # Create a black image of the same size as the screenshot
    black_mask = Image.new("RGB", screenshot.size, (0, 0, 0))

    # Create a mask for the region to keep (Chrome window area)
    mask = Image.new("L", screenshot.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle(region, fill=255)

    # Composite the screenshot with the black mask using the region mask
    result = Image.composite(screenshot, black_mask, mask)

    # Save the resulting image
    result.save("chrome_screenshot_masked.png")

    # Alternatively, show the resulting image (for visual confirmation)
    result.show()
