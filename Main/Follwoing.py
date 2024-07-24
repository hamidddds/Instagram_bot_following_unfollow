import HumanMove as hu
import pyautogui as py
from pyclick import HumanClicker, HumanCurve
import math
import random
import time
import json
from PIL import ImageGrab  # Required for screen capture
import pyperclip  # Required for clipboard operations
import os
import platform


def locate_center_on_screen(image_path, region=None, confidence=0.7):
    try:
        return py.locateCenterOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


def MovingToFollowSection(RemainedFollowed):  # return0 means it fails #end

    image_filenames = ['images/Following_like_button.png',
                       'images/Following_red_like_button.png',
                       'images/Following_red_like_comment_forward_button.png',
                       'images/Following_Like_Foward_button.png',
                       'images/Following_like_comment_forward_button.png',
                       'images/Following_Like_Comment_button.png',
                       'images/Following_red_like_comment.png',
                       ]

    Others = locate_center_on_screen('Images\others.png',
                                     region=(1000, 800, 600, 200), confidence=0.7)
    if (Others != None):
        hu.HumanLikeMove(Others[0], Others[1])
        py.click()
        time.sleep(1)
    else:
        for filename in image_filenames:
            time.sleep(0.6)
            V = locate_center_on_screen(filename, region=(
                700, 800, 600, 400), confidence=0.8)
            time.sleep(1)
            hu.HumanLikeMove(V[0], V[1])
            time.sleep(0.4)
            py.moveRel(0, 40, 0.5)
            time.sleep(0.35)
            py.click()
            time.sleep(2)


def MovingToFollowSection(RemainedFollowed):


def clear_terminal():
    """
    Clears the terminal screen.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


clear_terminal()
time.sleep(3)
MovingToFollowSection(4)

        while True:
            FollowButtom = list(py.locateAllOnScreen(
                'images/FollowButtom.png', region=(700, 300, 500, 500), confidence=0.9))

            time.sleep(random.uniform(0.5, 0.9))
            # start following
            if len(FollowButtom) != 0:
                for pos in FollowButtom:
                    pos = py.center(pos)
                    hu.HumanLikeMove(pos[0]+random.randint(-15, 15)-240,
                                  pos[1]+random.randint(-8, 8))
                    time.sleep(random.uniform(0.8, 1))
                    # HumanLikeMove(, 0)
                    # py.moveRel(-288, 0, 0.6)
                    time.sleep(random.uniform(0.8, 1))
                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.5, 0.7))
                    py.moveRel(0, -10, 0.3)
                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.8, 1))
                    py.moveRel(400, 0, 0.6)
                    time.sleep(random.uniform(0.8, 1))
                a = self.Open_pages()
                if a == 1:
                    return self.Followed, self.situation
            time.sleep(2)
            # scroll
            im = ImageGrab.grab(bbox=(765, 377, 1130, 755))
            im.save('endofthepost_image__before.jpg')

            time.sleep(random.uniform(0.8, 1.2))
            hu.HumanLikeMove(1000+random.randint(-10, 10),
                          550+random.randint(-20, 20),)
            time.sleep(random.uniform(0.8, 1.2))
            NowScroll = random.randint(-500, -300)
            hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
            im1 = ImageGrab.grab(bbox=(765, 377, 1130, 755))
            # im1.save('endofthepost_image__after.jpg')
            EndOfScroll = py.locateOnScreen(im, confidence=0.9)

            if EndOfScroll != None:
                print('End of scroll,lets go to the next post!')
                im1.save('endofthepost_image__after.jpg')
                self.situation = 4
                return self.Followed, self.situation

    def Open_pages(self):
        time.sleep(0.5)
        # Send Alt+D to focus the address bar
        py.hotkey('alt', 'd')

        # Wait for a short time to ensure the address bar is focused
        time.sleep(0.5)

        # Send Ctrl+C to copy the URL to clipboard
        py.hotkey('ctrl', 'c')
        Homepage = copyurlUrl()

        py.hotkey('ctrl', 'Tab')

        print(Homepage)

        Name_Of_page = ''
        username = []

        while 1:
            time.sleep(random.uniform(0.5, 0.7))
            Name_Of_page = copyurlUrl()
            time.sleep(random.uniform(0.5, 0.7))
            print(Name_Of_page)
            #
            username = Name_Of_page.split("www.instagram.com/")[-1].rstrip('/')
            # print(username)
            # print(self.saved_following)
            if Homepage == Name_Of_page:
                with open('my_list.json', 'w') as file:
                    json.dump(self.saved_following, file)
                return
            else:
                if username in self.saved_following:
                    time.sleep(random.uniform(0.4, 0.8))
                    py.hotkey('ctrl', 'w')
                else:
                    self.saved_following.append(username)
                    time.sleep(random.uniform(0.5, 0.7))
                    FollowButtom = py.locateOnScreen(
                        'images/followbutton2.png', region=(650, 100, 800, 150), confidence=0.8)
                    time.sleep(random.uniform(0.5, 0.9))
                    # start following

                    if FollowButtom:
                        print('Following...')
                        hu.HumanLikeMove(FollowButtom[0]+random.randint(25, 35),
                                      FollowButtom[1]+random.randint(10, 15))
                        time.sleep(random.uniform(0.8, 1))
                        py.click()
                        time.sleep(random.uniform(1, 1.4))
                       # winsound.Beep(1000, 200)
                        self.Followed += 1

                        if self.Followed >= self.Following_Number:
                            while True:
                                time.sleep(random.uniform(0.5, 0.7))
                                Name_Of_page = copyurlUrl()
                                time.sleep(random.uniform(0.5, 0.7))
                                username = Name_Of_page.split(
                                    "www.instagram.com/")[-1].rstrip('/')
                                if Homepage == Name_Of_page:
                                    with open('my_list.json', 'w') as file:
                                        json.dump(self.saved_following, file)
                                        self.situation = 10
                                        return 1
                                else:
                                    py.hotkey('ctrl', 'w')
                        time.sleep(random.uniform(0.4, 0.8))
                        py.hotkey('ctrl', 'w')
                        time.sleep(random.uniform(0.4, 0.8))

