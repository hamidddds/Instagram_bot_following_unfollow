import pychrome
import time
import winsound

# Connect to the Chrome browser (Make sure Chrome is started with remote debugging)
chrome = pychrome.Browser(url="http://127.0.0.1:9222")

# Create a tab
tab = chrome.new_tab()

# Define a callback for page load events


def page_loaded():
    print("Page is fully loaded.")
    winsound.Beep(1000, 500)  # Frequency of 1000 Hz and duration of 500 ms
    tab.stop()  # Stop listening to further events


# Start listening to the page load event
tab.Page.loadEventFired = page_loaded

# Start the tab
tab.start()

# Navigate to the desired webpage
tab.Page.navigate(url="https://example.com")

# Wait for the event
tab.wait(10)

# Stop the tab and close it
tab.stop()
chrome.close_tab(tab)
