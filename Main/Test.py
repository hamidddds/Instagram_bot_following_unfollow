import pyautogui as py


Others = py.locateCenterOnScreen(r'C:\Users\hamid\Desktop\Instagram Code\InstagramCode\Main\Images\others.png',
                                 region=(1000, 800, 600, 200), confidence=0.7)
print(Others)
