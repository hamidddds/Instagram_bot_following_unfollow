import time
import random
import lib_HumanMove as hu
from PIL import ImageGrab  # Required for screen capture
import pyautogui as py
start_time = time.time()


def locateOnScreen(image_path, region=None, confidence=0.7):
    try:
        return py.locateOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


while 1:
    time.sleep(2)
    # scroll
    im = ImageGrab.grab(bbox=(765, 377, 1130, 755))
    # im.save('endofthepost_image__before.jpg')

    time.sleep(random.uniform(0.8, 1.2))
    print("1")
    hu.HumanLikeMove(1000+random.randint(-10, 10),
                     550+random.randint(-20, 20),)
    print("2")
    time.sleep(random.uniform(0.8, 1.2))
    print("3")
    NowScroll = random.randint(-500, -300)
    print("4")
    hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
    print("5")
    time.sleep(random.uniform(2, 4))
    print("6")
    im1 = ImageGrab.grab(bbox=(765, 377, 1130, 755))
    print("7")
    im1.save('endofthepost_image__after.jpg')
    print("8")
    EndOfScroll = locateOnScreen(im, confidence=0.9)
    print("9")
