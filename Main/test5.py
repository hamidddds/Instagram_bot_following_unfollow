import pygetwindow as gw


import pygetwindow as gw


def changewindowssize():
    # Find all Chrome windows
    chrome_windows = gw.getWindowsWithTitle('Chrome')

    if chrome_windows:
        # Select the first Chrome window found
        chrome_window = chrome_windows[0]

        # If the window is maximized, restore it first
        if chrome_window.isMaximized:
            chrome_window.restore()

        # Set the desired width and height
        new_width = 1400
        new_height = 1038

        # Resize the window
        chrome_window.resizeTo(new_width, new_height)

        # Move the window to the top-left corner
        chrome_window.moveTo(-8, 1)
    else:
        print("Chrome window not found.")


changewindowssize()
