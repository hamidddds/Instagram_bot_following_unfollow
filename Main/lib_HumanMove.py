
import pyautogui as py
from pyclick import HumanClicker, HumanCurve
import random
import time
import numpy as np
import time
from scipy.special import comb
from pynput.mouse import Controller


def bezier_curve(t, points):
    """
    Generate a Bezier curve for parameter t in the range [0, 1].
    Points is a list of control points.
    """
    n = len(points) - 1
    curve = np.zeros((len(t), 2))
    for i in range(n + 1):
        binom = comb(n, i)
        curve += binom * (t[:, None] ** i) * \
            ((1 - t[:, None]) ** (n - i)) * points[i]
    return curve


def add_shake_to_path(path, max_deviation=5):
    """
    Add shake to the path by introducing random noise with a maximum deviation.
    """
    # Generate random noise
    noise = np.random.uniform(-max_deviation, max_deviation, size=path.shape)
    return path + noise


def calculate_duration(start_point, end_point, min_duration=1, max_duration=8):
    """
    Calculate duration based on the distance between start and end points.
    """
    distance = np.linalg.norm(np.array(end_point) - np.array(start_point))
    # Adjust the scaling factor as needed to fit your desired range of duration
    duration = min_duration + \
        (max_duration - min_duration) * (distance / 1000.0)
    return duration


def HumanLikeMove(coordinate, steps=1000, max_shake_deviation=1.2):
    end_point = coordinate
    x = coordinate[0]
    y = coordinate[1]
    mouse = Controller()
    start_point = mouse.position  # Get the current mouse position

    # Calculate the duration based on distance
    duration = calculate_duration(start_point, end_point)

    # Generate control points for the Bezier curve
    control_points = np.array([
        start_point,
        (start_point[0] + (end_point[0] - start_point[0]) / 2, start_point[1] +
         (end_point[1] - start_point[1]) / 3 + np.random.randint(-100, 100)),
        (start_point[0] + (end_point[0] - start_point[0]) / 2, start_point[1] +
         2 * (end_point[1] - start_point[1]) / 3 + np.random.randint(-100, 100)),
        end_point
    ])

    # Generate the Bezier curve
    t = np.linspace(0, 1, steps)
    path = bezier_curve(t, control_points)

    # Add controlled shake to the path
    path_with_shake = add_shake_to_path(
        path, max_deviation=max_shake_deviation)

    # Ensure the last point is exactly the end_point
    path_with_shake[-1] = end_point

    # Divide the steps into three segments
    segment1 = steps // 3
    segment2 = 2 * steps // 3

    # Speed adjustment factors for each segment
    intervals = [0.5, 0.8, 1.5]

    # Calculate base intervals
    base_intervals = [
        duration / (9 * segment1),
        duration / (9 * (segment2 - segment1)),
        duration / (9 * (steps - segment2))
    ]

    # Move the mouse in segments with varying speed
    for i in range(segment1):
        mouse.position = (path_with_shake[i][0], path_with_shake[i][1])
        time.sleep(base_intervals[0] * intervals[0])

    for i in range(segment1, segment2):
        mouse.position = (path_with_shake[i][0], path_with_shake[i][1])
        time.sleep(base_intervals[1] * intervals[1])

    for i in range(segment2, steps):
        mouse.position = (path_with_shake[i][0], path_with_shake[i][1])
        time.sleep(base_intervals[2] * intervals[2])

    # Manually set the final position to ensure accuracy
    mouse.position = end_point


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
        py.scroll(x1+random.randint(0, 15))

    Chance = random.randint(1, 3)
    if Chance == 1:

        scroll_fake = random.randint(100, 200)
        py.scroll(scroll_fake)
        time.sleep(random.uniform(1, 2))
        py.scroll(-scroll_fake+random.randint(0, 20))


def HumanLikeKeyboard(word):
    time.sleep(1)
    i = 0
    for _ in range(len(word)):
        b = random.uniform(0.09, 0.3)
        time.sleep(b)
        py.write(word[i])
        i += 1


def scrollpage():
    c = random.randint(400, 1000)
    Humanlikescroll(-c)
    Wait = random.randint(0, 2)
    time.sleep(Wait)


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
