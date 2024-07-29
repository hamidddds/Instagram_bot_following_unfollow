import pyautogui
import time

# Bring Chrome to the foreground


# Close all tabs except the first one
while True:
    # Close the current tab (Ctrl + w)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
    # Check if the first tab is reached
    if "New Tab" in pyautogui.getWindowsWithTitle()[0].title:
        break

# Focus on the first tab (Ctrl + 1)
pyautogui.hotkey('ctrl', '1')
