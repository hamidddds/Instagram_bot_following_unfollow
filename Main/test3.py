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


def calculate_duration(start_point, end_point, min_duration=1, max_duration=10):
    """
    Calculate duration based on the distance between start and end points.
    """
    distance = np.linalg.norm(np.array(end_point) - np.array(start_point))
    # Adjust the scaling factor as needed to fit your desired range of duration
    duration = min_duration + \
        (max_duration - min_duration) * (distance / 1000.0)
    return duration


def move_mouse_human_like(start_point, end_point, steps=1000, max_shake_deviation=1.2):

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

    # Move the mouse along the path
    mouse = Controller()

    # Divide the steps into three segments
    segment1 = steps // 3
    segment2 = 2 * steps // 3

    # Speed adjustment factors for each segment
    intervals = [0.5, 0.8, 1.5]

    # Calculate base intervals
    base_intervals = [duration / (9 * segment1), duration / (
        9 * (segment2 - segment1)), duration / (9 * (steps - segment2))]

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


# Example usage:
start = (0, 0)
end = (1000, 1000)
# Adjust the number of steps and shake deviation
move_mouse_human_like(start, end)
