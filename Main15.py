import datetime
from pyclick import HumanClicker, HumanCurve
import math
from timeit import default_timer as timer
from random import random
import pyautogui as py
import time
import random
from random import randrange
import subprocess
from PIL import Image, ImageGrab
import chime
from datetime import date
import tkinter as t
from tkinter import ttk
import pyperclip
import sys
chime.theme('zelda')


# C:\Users\hamid\Desktop\Main\venv\Scripts\activate.bat
# Add validity of each page

def ChangeTheProcessBar(Text):
    global NewProcess
    global root
    NewProcess.pack_forget()
    NewProcess = t.Label(root, text=Text)
    NewProcess.pack()
    root.update()
    time.sleep(1)


def MoveF(x, y, t):

    fromPoint = py.position()
    options = {
        "knotsCount": 2,
    }
    human_curve = HumanCurve(fromPoint=fromPoint, toPoint=(x, y), **options)
    hc = HumanClicker()
    # move the mouse to position (100,100) on the screen in approximately 2 seconds
    hc.move((x, y), t, humanCurve=human_curve)


def HumanLikeMove(movex, movey):
    x, y = py.position()
    distance = math.sqrt(pow((x-movex), 2) + pow((y-movey), 2))
# 2140 total
    if distance <= 150:
        MoveF(movex, movey, random.uniform(0.7, 1.1))
    elif 150 < distance <= 300:
        MoveF(movex, movey, random.uniform(1.3, 1.6))
    elif 300 < distance <= 700:
        MoveF(movex, movey, random.uniform(1.6, 2.1))
    else:
        MoveF(movex, movey, random.uniform(2.5, 3))


def HumanLikeClick():
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)
    py.click()
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)


def Humanlikescroll(x):
    RN = random.randint(1, 3)
    x1 = round(x/RN)
    x2 = x % RN
    py.scroll(x2)
    for _ in range(RN):
        time.sleep(random.uniform(0.7, 1.2))
        py.scroll(x1)


def HumanLikeKeyboard(word):
    time.sleep(1)
    i = 0
    for _ in range(len(word)):
        b = random.uniform(0.09, 0.3)
        time.sleep(b)
        py.write(word[i])
        i += 1


def MovePostRight():
    N_postChnage = 0
    time.sleep(random.uniform(0.8, 1))

    likers = py.locateCenterOnScreen(
        'images/rightleftpost.png', region=(580, 100, 700, 900), confidence=0.7)

    time.sleep(random.uniform(0.8, 1))
    if likers != None:
        time.sleep(random.uniform(1, 3))
        py.moveTo(likers[0]+3, likers[1]+3, 1)
        time.sleep(random.uniform(0.2, 0.4))
        # chime.success()  # ??
        py.click()
        N_postChnage += 1
    return N_postChnage


def scrollpage():
    c = random.randint(400, 1000)
    Humanlikescroll(-c)
    Wait = random.randint(0, 2)
    time.sleep(Wait)


def ClickMore():
    N_postChnage = 0
    time.sleep(1)
    MorePos = py.locateOnScreen(
        'images/MoreInMainPage.png', region=(450, 130, 1000, 800), confidence=0.8)
    time.sleep(1)
    if MorePos != None:
        xx = py.center(MorePos)
        HumanLikeMove(xx[0], xx[1])
        # chime.success()
        for _ in range(1, 3):
            time.sleep(random.uniform(1, 3))
            py.click()
            N_postChnage = +1
    return N_postChnage


def HumanLikeWait(t, Bx, By):
    start = time.time()
    first = py.position()
    X_RelPose = Y_RelPose = 0
    fromPoint = py.position()

    while time.time() - start < t:

        if first[0] - Bx/2 < 50:
            x = random.randint(-fromPoint[0] +
                               50, -fromPoint[0]+Bx/2+first[0]+50)
        elif first[0] + Bx/2 > 1880:
            x = random.randint(-fromPoint[0]-Bx /
                               2+first[0], 1880-fromPoint[0] - 50)
        else:
            x = random.randint(-fromPoint[0]-Bx/2 +
                               first[0], -fromPoint[0]+Bx/2+first[0])

        if first[1] - By/2 < 50:
            y = random.randint(-fromPoint[1] +
                               50, -fromPoint[1]+By/2+first[1]+50)
        elif first[1] + By/2 > 1880:
            y = random.randint(-fromPoint[1]-By /
                               2+first[1], 1880-fromPoint[1] - 50)

        else:
            y = random.randint(-fromPoint[1]-By/2 +
                               first[1], -fromPoint[1]+By/2+first[1])

        X_RelPose = X_RelPose + x
        Y_RelPose = Y_RelPose + y

        fromPoint = py.position()

        options = {
            "knotsCount": 2,
        }

        human_curve = HumanCurve(fromPoint=fromPoint, toPoint=(
            fromPoint[0] + x, fromPoint[1] + y), **options)

        hc = HumanClicker()

        Chance = random.randint(1, 3)
        if Chance != 3:
            # move the mouse to position (100,100) on the screen in approximately 2 seconds
            hc.move((fromPoint[0] + x, fromPoint[1] + y),
                    random.uniform(1, 2), humanCurve=human_curve)
        else:
            time.sleep(random.uniform(1, 2))

        # py.moveTo(fromPoint[0] + x, fromPoint[1] + y,0.1)
        time.sleep(random.uniform(0.1, 0.3))
        fromPoint = py.position()

    HumanLikeMove(first[0]+random.randint(-5, 5),
                  first[1]+random.randint(-5, 5))


def homebuttom():
    time.sleep(random.uniform(0.5, 0.9))
    py.press('Esc')
    time.sleep(random.uniform(0.5, 0.9))
    py.press('Esc')
    time.sleep(random.uniform(0.5, 0.9))
    py.press('Esc')
    HumanLikeMove(70+random.randint(2, 30), 155+random.randint(0, 10))
    time.sleep(random.uniform(0.5, 1))
    HumanLikeClick()


def EnterUrl(Nameurl):
    HumanLikeMove(593+random.randint(-10, 10), 54)
    time.sleep(random.uniform(0.5, 0.8))
    HumanLikeClick()
    with py.hold('ctrl'):
        py.press(['a'])
    time.sleep(random.uniform(0.5, 0.8))
    py.press('Backspace')
    HumanLikeKeyboard(Nameurl)
    time.sleep(random.uniform(0.5, 0.8))
    py.press('Enter')
    time.sleep(8)


def LikingStories():
    global NewProcess
    global root
    NumStoryLiked = 0
    x = random.randint(745, 774)
    y = random.randint(161, 185)
    HumanLikeMove(x, y)
    HumanLikeClick()
    Validity = py.locateOnScreen(
        'images/validityStory.png', region=(1700, 50, 300, 300), confidence=0.8)
    if Validity != None:
        while NumStoryLiked < 10:
            LikeOrNot = random.randint(0, 1)
            if LikeOrNot == 1:
                py.moveTo(891, 980, 0.4)
                time.sleep(random.uniform(0.2, 0.4))
                HumanLikeMove(
                    1125+random.randint(-3, 3), 971-random.randint(-3, 3))
                py.click()
                # chime.success()
                time.sleep(random.uniform(3, 4))
                py.press('Right')
                NumStoryLiked += 1
            else:
                time.sleep(random.uniform(1, 2))
                py.press('Right')
        return 0
    py.press('Esc')
    return NumStoryLiked


def OpenTargetpage(TPages):
    for _ in range(5):
        ChangeTheProcessBar('Openning the Target Page...')
        SearchButtom = py.locateOnScreen(
            'images/SearchButtom.png', confidence=0.8)
        if SearchButtom != None:  # validity of homepage
            HumanLikeMove(SearchButtom[0]+random.randint(10, 200),
                          SearchButtom[1]+random.randint(10, 30))  # click on search buttom
            HumanLikeClick()
            time.sleep(random.uniform(0.5, 1))
            HumanLikeMove(246+random.randint(-120, 120), 211 +
                          random.randint(-12, +12))  # click on search box
            time.sleep(random.uniform(0.5, 1))
            HumanLikeKeyboard(TPages)
            time.sleep(random.uniform(2, 2.5))
            py.press('Enter')
            time.sleep(random.uniform(2, 2.5))
            py.press('Enter')
            time.sleep(random.uniform(2, 2.5))
            py.press('Enter')
            time.sleep(1)
            if validity.targetpage(TPages) == True:
                return None
        else:
            EnterUrl('www.instagram.com')
            time.sleep(4)


def FollowingPost(RemainedFollowed):  # return0 means it fails #end
    ChangeTheProcessBar('Initiating Following people...')
    Followed = 0
    FlagEndOfPost = 0
    EndOfScroll = None
    V = py.locateOnScreen('images/like_button.png',
                          region=(700, 800, 600, 400), confidence=0.8)
    if V == None:
        ChangeTheProcessBar('Cannot Recognize The Target Post Page???')
        print('Cannot Recognize The Target Post Page???')
        EnterUrl('www.instagram.com')
        return Followed, 'NotDone', FlagEndOfPost
    else:  # start following
        # 6 is number of indivituals in each page
        time.sleep(0.8)
        OpenFollowing = py.locateCenterOnScreen('images/LikeAndCommentShape.png',
                                                region=(950, 700, 650, 200), confidence=0.7)
        HumanLikeMove(OpenFollowing[0], OpenFollowing[1])
        time.sleep(0.4)
        OpenFollowing = py.locateCenterOnScreen('images/LikeAndCommentShape.png',
                                                region=(950, 700, 650, 200), confidence=0.7)
        py.moveRel(0, 40, 0.5)
        time.sleep(0.4)
        py.click()
        time.sleep(2)
        Others = py.locateCenterOnScreen('images/others.png',
                                         region=(1000, 800, 600, 200), confidence=0.7)
        if Others != None and validity.FollowingV() != True:
            HumanLikeMove(Others[0], Others[1])
            py.click()
            time.sleep(1)

        if validity.FollowingV() != True:
            ChangeTheProcessBar('Cannot Recognize The following???')
            EnterUrl('www.instagram.com')
            return Followed, 'NotDone', FlagEndOfPost
        while Followed < RemainedFollowed:
            time.sleep(0.5)
            FollowButtom = list(py.locateAllOnScreen(
                'images/FollowButtom.png', region=(700, 300, 500, 500), confidence=0.9))
            time.sleep(random.uniform(0.5, 0.9))
            # start following

            if FollowButtom != None:
                ChangeTheProcessBar('Following...')
                for pos in FollowButtom:
                    C = random.randint(1, 7)
                    if C != 5:
                        pos = py.center(pos)
                        HumanLikeMove(pos[0]+random.randint(-15, 15),
                                      pos[1]+random.randint(-8, 8))
                        time.sleep(random.uniform(0.8, 1))
                        # chime.success()
                        py.click()
                        time.sleep(random.uniform(1.4, 1.8))
                        Followed += 1
                        if Followed >= RemainedFollowed:
                            return Followed, 'Done', FlagEndOfPost
            HumanLikeMove(1700+random.randint(-40, 40),
                          500+random.randint(-20, 20))
            time.sleep(random.uniform(0.8, 1.2))

            im = ImageGrab.grab(bbox=(765, 377, 1130, 755))

            time.sleep(random.uniform(0.8, 1.2))
            HumanLikeMove(1000+random.randint(-10, 10),
                          550+random.randint(-20, 20),)

            time.sleep(random.uniform(0.8, 1.2))
            NowScroll = random.randint(-500, -300)
            Humanlikescroll(NowScroll)  # 430 scroll kamele

            time.sleep(random.uniform(0.8, 1.2))
            HumanLikeMove(1700+random.randint(-40, 40),
                          500+random.randint(-20, 20))

            time.sleep(random.uniform(0.8, 1))
            EndOfScroll = py.locateOnScreen(im, confidence=0.9)

            if EndOfScroll != None:
                FlagEndOfPost = 1
                print('End of scroll,lets go to the next post!')
                ChangeTheProcessBar('End of scroll,lets go to the next post!')
                break

    py.press("Esc")
    time.sleep(0.2)
    py.press("Esc")
    time.sleep(0.3)
    return (Followed, 'Done', FlagEndOfPost)


def HomePageManager(TimeToScrollHomePage):

    # output
    N_Replys, N_LikedComments, N_LikedPost, N_Comments, N_ClickingMore, N_postChnage = 0, 0, 0, 0, 0, 0

    if validity.homepage() == False:
        print('Cannot see the home page')
        return (N_Replys, N_LikedComments, N_LikedPost, N_Comments, N_ClickingMore, N_postChnage, 0, 'NotDone')

    ChangeTheProcessBar('Idling in Homepage...')

    Start = time.time()
    while time.time() - Start < TimeToScrollHomePage:
        # move mouse away
        py.moveTo(1700 + random.randint(-20, 20), 500 +
                  random.randint(-40, 40), random.uniform(1, 2), py.easeOutQuad)
        scrollpage()
        WaitChance = random.randint(1, 3)

        if WaitChance == 2:
            ChangeTheProcessBar(
                'Reading Posts,pushing more buttun and right buttun')
            HumanLikeWait(random.randint(10, 15), 30, 500)
            time.sleep(random.uniform(0.5, 1.1))
            N_ClickingMore = ClickMore()+N_ClickingMore
            N_postChnage = MovePostRight()+N_postChnage

        LikingChance = random.randint(1, 3)
        if LikingChance != 3:
            time.sleep(random.uniform(0.6, 1.1))
            LikePose = py.locateOnScreen(
                'images/like_button.png', region=(550, 100, 800, 920), confidence=0.9)  # ?????????????????????
            if LikePose != None:
                time.sleep(random.uniform(0.2, 0.8))
                HumanLikeMove(LikePose[0]+random.randint(10, 20),
                              LikePose[1]+random.randint(10, 20))
                # chime.success()  # ??
                time.sleep(random.uniform(0.4, 0.7))
                py.click()
                N_LikedPost = N_LikedPost + 1
                time.sleep(random.uniform(0.4, 0.8))
                py.moveTo(1700 + random.randint(-20, 20), 500 +
                          random.randint(-40, 40), random.uniform(1, 2), py.easeOutQuad)

                CommentChance = random.randint(1, 10)  # chance of comment
                if CommentChance == 10:
                    time.sleep(random.uniform(0.2, 0.8))
                    HumanLikeMove(LikePose[0]+60, LikePose[1]+10)
                    time.sleep(random.uniform(0.2, 0.8))
                    py.click()
                    HumanLikeMove(1470, 384)
                    i = 0
                    for _ in range(3):
                        if validity.Post() == True:
                            N_LikedCommentsN, N_ReplysN, N_CommentsN = InsidePost()
                            N_LikedComments = N_LikedComments + N_LikedCommentsN
                            N_Replys = N_Replys + N_ReplysN
                            N_Comments = N_Comments + N_CommentsN
                        else:
                            ChangeTheProcessBar(
                                'Cannot see the openned post;solution=wait 4 seconds')
                            time.sleep(4)
                            i += 1
                        if i == 4:
                            ChangeTheProcessBar(
                                'Something is wrong, try again')
                            time.sleep(1)
                            return (N_Replys, N_LikedComments, N_LikedPost, N_Comments, N_ClickingMore, N_postChnage, time.time() - Start, 'NotOkay')

    return (N_Replys, N_LikedComments, N_LikedPost, N_Comments, N_ClickingMore, N_postChnage, time.time() - Start, 'Okay')


def InsidePost():
    ChanceOFLikingsInPost, ChanceOfCommentInPost = 6, 4
    N_comments, N_Replys, N_LikedComments = 0, 0, 0
    ChangeTheProcessBar('Liking commenters...')
    for _ in range(random.randint(2, 3)):

        HumanLikeMove(1300 + random.randint(-30, 30),
                      240 + random.randint(-30, 300))
        time.sleep(random.uniform(0.6, 1))

        MorePlus = py.locateOnScreen(
            'images/moreplus.png', region=(1000, 700, 300, 150), confidence=0.8)
        time.sleep(random.uniform(0.4, 0.8))

        if MorePlus != None:
            MorePlus = py.center(MorePlus)
            HumanLikeMove(MorePlus[0]+5, MorePlus[1]+5)
            time.sleep(random.uniform(0.4, 0.8))
            py.click()
            time.sleep(random.randint(3, 5))
            HumanLikeMove(1400 + random.randint(-30, 30),
                          240 + random.randint(-30, 300))
            time.sleep(random.uniform(0.4, 0.8))
        else:
            time.sleep(random.uniform(5, 10))
            ChangeTheProcessBar('Pretending to read Comments...')
            # like
            likers = py.locateAllOnScreen(
                'images/heartCommenters.png', region=(1000, 150, 700, 800), confidence=0.8)
            time.sleep(random.uniform(1, 1.5))
            if likers != None:
                for pos in likers:
                    time.sleep(random.uniform(1, 3))
                    # chance of liking comments for each person in one page
                    chance = random.randint(1, ChanceOFLikingsInPost)
                    if chance == 1:
                        likers = py.center(pos)
                        HumanLikeMove(pos[0]+10, pos[1]+10)
                        time.sleep(random.uniform(0.2, 0.4))
                        py.click()
                        # chime.success()  # ??
                        # HumanLikeClick()
                    N_LikedComments += 1
                N_Replys, N_comments = writecomment(
                    ChanceOfCommentInPost)
                Humanlikescroll(random.randint(-430, -300))
            else:
                return N_LikedComments, N_Replys, N_comments
    time.sleep(random.uniform(0.3, 0.7))
    py.press("Esc")
    time.sleep(random.uniform(0.3, 0.7))
    py.press("Esc")
    time.sleep(random.uniform(0.3, 0.7))
    py.press("Esc")
    time.sleep(random.uniform(0.3, 0.7))
    return N_LikedComments, N_Replys, N_comments


def writecomment(ChanceOfCommentInPost):
    CommentsReplay = ['عالی بود', 'موافقم', 'like', '<3', '🙊']
    CommentsInPost = ['چه پست قشنگی', '🙊', '😍😍😍😍', '👌🏻👌🏼👌🏽👌🏾',
                      'Big Like', '❤️', 'زیبا زیبا زیبا', 'کاش میشد...ا', '💋']

    N_Replys, N_comments = 0, 0

    time.sleep(random.uniform(0.6, 1))
    Smilyface = py.locateCenterOnScreen(
        'images/Smaily_face_shape.png', region=(950, 900, 600, 200), confidence=0.9)
    if Smilyface != None:  # start commenting
        time.sleep(random.uniform(1, 2))
        Temp = random.randint(1, ChanceOfCommentInPost)
        if Temp == 1:
            py.moveTo(Smilyface[0]+100, Smilyface[1],
                      random.uniform(0.8, 1.3), py.easeInElastic)
            time.sleep(random.uniform(0.4, 0.8))
            py.click()
            NumCom = random.randint(0, len(CommentsInPost)-1)
            pyperclip.copy(CommentsInPost[NumCom])
            with py.hold('ctrl'):
                py.press(['v'])
            time.sleep(random.uniform(0.8, 1.2))
            py.press('Enter')
            time.sleep(0.4)
            py.press('Enter')
            N_comments += 1
    time.sleep(random.uniform(0.6, 1))

    Replay = py.locateAllOnScreen(
        'images/Replay.png', region=(1150, 150, 300, 800), confidence=0.9)
    if Replay != None:  # start commenting
        for pos in Replay:
            time.sleep(random.uniform(1, 2))
            Temp = random.randint(1, ChanceOfCommentInPost*2)
            if Temp == 1:
                B = py.center(pos)
                py.moveTo(B[0]+10, B[1]+10, 1)
                time.sleep(random.uniform(0.4, 0.8))
                py.click()
                time.sleep(random.uniform(0.4, 0.8))
                py.moveTo(1300+random.randint(0, 100),
                          980+random.randint(0, 5), 2)
                py.click()
                time.sleep(random.uniform(0, 1))
                NumCom = random.randint(0, len(CommentsReplay)-1)
                pyperclip.copy(CommentsInPost[NumCom])
                with py.hold('ctrl'):
                    py.press(['v'])
                time.sleep(random.uniform(0.8, 1.2))
                py.press('Enter')
                time.sleep(0.4)
                py.press('Enter')
                N_Replys += 1

    return N_Replys, N_comments


def Flag_manager():
    PostFlag = 0
    DoNothingFlag = 0
    StoryFlag = 0
    chance = random.randint(1, 8)
    if chance == 1:
        StoryFlag = 0
    elif (chance == 2) or (chance == 3) or (chance == 4) or (chance == 5):
        DoNothingFlag = 1
    else:
        PostFlag = 1
    return StoryFlag, DoNothingFlag, PostFlag


def ProcessBar():
    global root
    global NewProcess
    root = t.Tk()
    root.wm_attributes("-topmost", 1)
    root.geometry('300x100+0+900')
    Title = t.Label(root, text='Processing...')
    Title.pack()
    pb = ttk.Progressbar(root, length=200, mode='indeterminate')
    pb.pack()
    pb.start()
    NewProcess = t.Label(root, text='')
    NewProcess.pack_forget()
    root.update()
    # bb = t.Label(root, text='salam %d' % a)
    return


def ChoosePost(postNum):
    HumanLikeMove(800, 782)
    HumanLikeClick()
    time.sleep(1)
    for _ in range(postNum):
        time.sleep(random.uniform(0.5, 0.8))
        py.press('Right')


class validity():

    def homepage():
        LoopCount = 0
        while LoopCount != 6:
            ChangeTheProcessBar('Checking validity Of homepage')
            Homepagevalidity1 = py.locateCenterOnScreen(
                'images/ReadHeartCommentForwards.png', region=(450, 450, 1000, 600), confidence=0.9)
            time.sleep(0.8)
            Homepagevalidity2 = py.locateCenterOnScreen(
                'images/like_button.png', region=(450, 450, 1000, 600), confidence=0.9)
            time.sleep(0.7)
            Homepagevalidity3 = py.locateCenterOnScreen(
                'images/LikeFowardsButtun.png', region=(450, 450, 1000, 600), confidence=0.9)
            if (Homepagevalidity1 == None) and (Homepagevalidity2 == None) and (Homepagevalidity3 == None):
                py.moveTo(1700 + random.randint(-20, 20), 500 +
                          random.randint(-40, 40), random.uniform(1, 2), py.easeOutQuad)
                ChangeTheProcessBar('Cannot See the Homepage')
                time.sleep(1)
                ChangeTheProcessBar('Waiting For Loading')
                time.sleep(5)
                LoopCount += 1
            else:
                return True
            if LoopCount == 3:
                ChangeTheProcessBar('Last Try...')
                EnterUrl('www.Instagram.com')
        return False

    def targetpage(TargetPage):
        ChangeTheProcessBar('Checking validity of Target page')
        py.moveTo(1600, 155, random.uniform(1, 2), py.easeInOutQuad)
        time.sleep(random.uniform(0.5, 1))
        py.drag(-800, 0, 0.6, button='left')
        time.sleep(random.uniform(0.5, 1))
        with py.hold('ctrl'):
            py.press(['c'])
        py.moveTo(1682, 187, 1)
        time.sleep(0.6)
        py.click()
        ret = subprocess.getoutput("powershell.exe -Command Get-Clipboard")
        NumberOfLikes = ret.split()
        for i in NumberOfLikes:
            if i == TargetPage:
                return True
        ChangeTheProcessBar('Cannot See The Target Page :(')
        time.sleep(1)
        return False

    def Post():
        ChangeTheProcessBar('Checking validity Of Opened Post')
        time.sleep(1)
        Homepagevalidity = py.locateCenterOnScreen(
            'images/Smaily_face_shape.png', region=(800, 750, 800, 300), confidence=0.8)
        if Homepagevalidity == None:
            ChangeTheProcessBar('Cannot See the Post')
            time.sleep(1)
            return False
        else:
            return True

    def FollowingV():
        ChangeTheProcessBar('Cheking Validity of following...')
        time.sleep(1)
        Homepagevalidity = py.locateCenterOnScreen(
            'images/followingValidity.png', region=(700, 300, 500, 500), confidence=0.9)
        if Homepagevalidity == None:
            ChangeTheProcessBar('Cannot See The Target Page to follow :(')
            time.sleep(1)
            return False
        else:
            return True

    def StoryV():
        ChangeTheProcessBar('Cheking Validity of Story page...')
        time.sleep(1)
        Homepagevalidity = py.locateCenterOnScreen(
            'images/validityStory.png', region=(1700, 95, 220, 80), confidence=0.9)
        if Homepagevalidity == None:
            ChangeTheProcessBar('Cannot See the Story page????')
            time.sleep(1)
            return False
        else:
            return True


if __name__ == "__main__":
    global Followed
    global root
    time.sleep(5)
    # initiate the parameteres
    ProcessBar()
    ChanceOFLikingsInPost = 4
    ChanceOfCommentInPost = 5
    FollowInHour = 2
    Situation = ''
    postnum = 0

    TargetPage = 'mode___rooz'

    # flags
    N_Replys, N_LikedComments, N_LikedPost, N_Comments, N_ClickingMore, N_postChnage = 0, 0, 0, 0, 0, 0
    LikingStatus = 'NotDone'
    TNumberOfLikedComments = 0
    TNumLikedPost = 0
    TNumberOfComments = 0
    TNumberOfComments = 0
    NumberOflikedStory = 0
    temp = 1
    PostFlag = 0
    StoryFlag = 0
    DoNothingFlag = 0
    donothing = 0
    T = 0
    FlagEndOfPost = 0

    while True:
        c = 1
        start1 = time.time()
        FollowFlag = 1
        followed_page = 0
        while time.time()-start1 < 900:

            if FollowFlag == 1:
                i = 0
                while FollowInHour - followed_page > 0:
                    if FlagEndOfPost == 1:
                        postnum += 1
                    # followSituation = 'NotDone'
                    # while (followSituation == 'NotDone'):
                    EnterUrl('www.instagram.com')
                    OpenTargetpage(TargetPage)
                    ChoosePost(postnum)
                    cc = FollowInHour - followed_page
                    followed, followSituation, FlagEndOfPost = FollowingPost(
                        cc)
                    if i == 4:
                        ChangeTheProcessBar('Cannot Open Following page')
                        time.sleep(4)
                        print('Cannot open following page')
                        sys.exit()
                    i += 1
                    followed_page = followed + followed_page
                    T = T + followed_page  # total number of follows
                    print("Total Number of followed page is/hour=", T)

                FollowFlag = 0
                tt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print('Followed finished at: %s' % tt)
                print('Number of followed page hourly: %d' % followed_page)
                homebuttom()

            elif PostFlag == 1:
                i = 0
                timeInHomepage = random.randint(300, 350)
                while LikingStatus == 'NotDone' and timeInHomepage > 10:
                    ChangeTheProcessBar('Liking posts...')
                    EnterUrl('www.Instagram.com')
                    time.sleep(random.uniform(1.2, 1.8))
                    py.press('Enter')

                    (N_Replys, N_LikedComments, N_LikedPost, N_Comments, N_ClickingMore, N_postChnage, RtimeInHomepage, Situation) = HomePageManager(
                        timeInHomepage)  # time in seconds
                    timeInHomepage = timeInHomepage - RtimeInHomepage

                    TNumberOfLikedComments = TNumberOfLikedComments+N_LikedComments
                    TNumLikedPost = TNumLikedPost+N_LikedPost
                    TNumberOfComments = TNumberOfComments+N_Comments
                    TNumberOfComments = TNumberOfComments+N_Replys
                    if i == 10:
                        ChangeTheProcessBar('Cannot open Homepage')
                        time.sleep(4)
                        print('Cannot open Homepage')
                        sys.exit()
                    print(i)
                    i += 1
                PostFlag = 0

            elif StoryFlag == 1:
                EnterUrl('www.Instagram.com')
                ChangeTheProcessBar('Cheking stories...')
                NumberOflikedStory = LikingStories()
                StoryFlag = 0

            elif DoNothingFlag == 3:
                DoNothingFlag = 0
                # donothing = random.randint(30, 60)*10
                donothing = random.randint(15, 25)*10
                for i in range(1, donothing):
                    NewProcess.pack_forget()
                    NewProcess = t.Label(
                        root, text='waiting... \n %d / %d Seconds' % (i, donothing))
                    NewProcess.pack()
                    root.update()
                    time.sleep(1)

            StoryFlag, DoNothingFlag, PostFlag = Flag_manager()  # ???????????????????????
        print('Times is:')
        print(time.time()-start1)
        print('Number of followed pages: %d' % T)
        print('Number of Liked Comments is = %d ' % TNumberOfLikedComments)
        print('Number of Liked Posts Is = %d ' % TNumLikedPost)
        print('Number of  Comments Under Posts is = %d ' %
              TNumberOfComments)
        print('Number of  Replays is = %d ' % TNumberOfComments)
