import HumanMove as hm
import pyautogui as py
import random
import time
from PIL import ImageGrab  # Required for screen capture


button_positions = {
    "home": (98, 247),
    "search": (94, 307),
    "explore": (100, 364),
    "reels": (95, 413),
    "messages": (103, 472),
    "notification": (104, 527),
    "profile": (90, 640)
}


def Move(button_name):
    if button_name in button_positions:
        x, y = button_positions[button_name]
        time.sleep(random.uniform(0.5, 0.9))
        py.press('Esc')
        time.sleep(random.uniform(0.5, 0.9))
        py.press('Esc')
        time.sleep(random.uniform(0.5, 0.9))
        py.press('Esc')
        hm.HumanLikeMove(x + random.randint(2, 30), y + random.randint(0, 10))
        time.sleep(random.uniform(0.5, 1))
        hm.HumanLikeClick()
    else:
        print("Button not found")
