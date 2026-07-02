import numpy as np
import matplotlib.pyplot as plt
from forward_kinematics import fk
from inverse_kinematics import ik
from image_processing import get_all_contours


points = [
    (100, 50),
    (100, 120),
    (40, 120),
    (40, 50),
    (100, 50)
]

L1 = 100
L2 = 80

fig = plt.figure(figsize=(8, 8))

theta1_current = 0
theta2_current = 0
Kp = 0.1
tolerance = np.radians(0.5)
trail = []


for point in points:
    x, y = point
    theta1_target, theta2_target = ik(x, y, L1, L2)
    if theta1_target is None or theta2_target is None:
        print(f"Point {point} is unreachable.")
        continue

    for frame in range(300):
        error1 = theta1_target - theta1_current
        error2 = theta2_target - theta2_current
        theta1_current += error1 * Kp
        theta2_current += error2 * Kp
        plt.cla()
        x1, y1, x2, y2 = fk(theta1_current, theta2_current, L1, L2)
        plt.axis("equal")
        plt.xlim(-200,200)
        plt.ylim(-200,200)
        plt.grid(True)
        plt.title("2 DOF Robot Arm")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.plot([p[0] for p in trail], [p[1] for p in trail], color='orange', linewidth=2)
        plt.scatter(x, y, color='green', marker='x')
        plt.plot([0, x1], [0, y1], color = 'red')
        plt.plot([x1, x2], [y1, y2], color = 'blue')
        plt.scatter([0, x1, x2], [0, y1, y2], color='black')
        plt.pause(0.02)
        if abs(error1) < tolerance and abs(error2) < tolerance:
            break
        dist = np.sqrt((x2 - x)**2 + (y2 - y)**2)
        trail.append((x2, y2))
        if dist < 2:
            print("Target reached!")
            break
        