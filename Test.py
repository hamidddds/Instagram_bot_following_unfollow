import os
import datetime
import pyautogui as py


def screenshoterror(name=''):
    try:
        # Capture the screenshot
        screenshot = py.screenshot()

        # Create a timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

        # Construct the filename
        filename = f"{name}{timestamp}.png"

        # Define the directory to save the screenshot
        directory = r'/screenshots/Error_screenshots'

        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Construct the full file path
        filepath = os.path.join(directory, filename)

        # Save the screenshot
        screenshot.save(filepath)

        print(f"Screenshot saved as: {filepath}")

    except Exception as e:
        print(f"An error occurred: {e}")


screenshoterror("salam")
