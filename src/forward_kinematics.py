import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics(theta1, theta2, l1, l2):
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    return x1, y1, x2, y2

L1 = 100
L2 = 80
fig = plt.figure(figsize=(8, 8))

for i in range(360):
    plt.cla()
    theta1 = np.radians(i)
    theta2 = np.radians(60)
    x1, y1, x2, y2 = forward_kinematics(theta1, theta2, L1, L2)
    plt.axis("equal")
    plt.xlim(-200,200)
    plt.ylim(-200,200)
    plt.grid(True)
    plt.title("2 DOF Robot Arm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot([0, x1], [0, y1], color = 'red')
    plt.plot([x1, x2], [y1, y2], color = 'blue')
    plt.scatter([0, x1, x2], [0, y1, y2], color='black')
    plt.pause(0.02)