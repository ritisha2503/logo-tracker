import matplotlib.pyplot as plt
from src.forward_kinematics import fk
from src.inverse_kinematics import ik

def move_to(x, y, pen_down,
            theta1_current, theta2_current,
            trail,
            L1, L2,
            Kp, tolerance):

    theta1_target, theta2_target = ik(x, y, L1, L2)

    if theta1_target is None or theta2_target is None:
        print(f"Point ({x}, {y}) is unreachable.")
        return theta1_current, theta2_current, trail

    frame = 0
    while True:

        error1 = theta1_target - theta1_current
        error2 = theta2_target - theta2_current

        theta1_current += error1 * Kp
        theta2_current += error2 * Kp

        x1, y1, x2, y2 = fk(theta1_current, theta2_current, L1, L2)

        # Only draw when pen is down
        if pen_down:
            trail[-1].append((x2, y2))

        plt.cla()
        plt.axis("equal")
        plt.xlim(-200, 200)
        plt.ylim(-200, 200)
        # plt.grid(True)

        plt.title("2 DOF Robot Arm")
        # plt.xlabel("X")
        # plt.ylabel("Y")

        for contour_trail in trail:
            if len(contour_trail) > 1:
                plt.plot([p[0] for p in contour_trail],
                         [p[1] for p in contour_trail],
                         color="orange",
                         linewidth=2)

        plt.scatter(x, y, color="green", marker="x")

        plt.plot([0, x1], [0, y1], color="red")
        plt.plot([x1, x2], [y1, y2], color="blue")

        plt.scatter([0, x1, x2],
                    [0, y1, y2],
                    color="black")

        plt.pause(0.001)

        dist = ((x2 - x)**2 + (y2 - y)**2)**0.5
        if dist < 1:
            break

        frame += 1
        if frame > 300:
            break

    return theta1_current, theta2_current, trail