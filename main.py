import numpy as np
import matplotlib.pyplot as plt

L1 = 100
L2 = 80

def forward_kinematics(theta1, theta2):
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    return x1, y1, x2, y2

def inverse_kinematics(x, y):
    r = np.sqrt(x**2 + y**2)
    D = (r**2 - L1**2 - L2**2) / (2 * L1 * L2)
    if abs(D) > 1:
        return None, None
    
    D = np.clip(D, -1, 1)
    theta2 = np.arctan2(-np.sqrt(1 - D**2), D)

    theta1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))
    return theta1, theta2

fig = plt.figure(figsize=(8, 8))

theta1_target, theta2_target = inverse_kinematics(50, 50)

theta1_current = 0
theta2_current = 0
Kp = 0.5
dt = 0.02
tolerance = np.radians(0.5)


for frame in range(500):
    error1 = theta1_target - theta1_current
    error2 = theta2_target - theta2_current
    theta1_current += error1 * Kp * dt
    theta2_current += error2 * Kp * dt
    plt.cla()
    x1, y1, x2, y2 = forward_kinematics(theta1_current, theta2_current)
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
    if abs(error1) < tolerance and abs(error2) < tolerance:
        break