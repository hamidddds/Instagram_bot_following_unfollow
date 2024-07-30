import time
import random
import lib_HumanMove as hu
from PIL import ImageGrab  # Required for screen capture
start_time = time.time()
time.sleep(1)
end_time = time.time()

time.sleep(random.uniform(0.8, 1.2))
hu.HumanLikeMove(1000+random.randint(-10, 10),
                 550+random.randint(-20, 20),)
time.sleep(random.uniform(0.8, 1.2))
NowScroll = random.randint(-500, -300)
hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
time.sleep(random.uniform(0.8, 1.2))
im1 = ImageGrab.grab(bbox=(765, 377, 1130, 755))
im1.save('endofthepost_image__after.jpg')
