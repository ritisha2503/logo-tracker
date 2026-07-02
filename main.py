import numpy as np
import matplotlib.pyplot as plt
from src.forward_kinematics import fk
from src.inverse_kinematics import ik
from src.image_processing import get_all_contours
from src.trajectory_following import move_to

all_contours = get_all_contours("src/kgp_logo.png")

L1 = 100
L2 = 100

fig = plt.figure(figsize=(8, 8))

theta1_current = 0
theta2_current = 0
Kp = 0.7
tolerance = np.radians(0.5)
trail = [[]]
i = 0

for i, contour in enumerate(all_contours):

    if len(contour) < 2:
        continue

    # Move to the first point WITHOUT drawing
    x, y = contour[0]

    theta1_current, theta2_current, trail = move_to(
        x, y,
        pen_down=False,
        theta1_current=theta1_current,
        theta2_current=theta2_current,
        trail=trail,
        L1=L1,
        L2=L2,
        Kp=Kp,
        tolerance=tolerance
    )

    # Draw the contour
    for point in contour[1:]:

        x, y = point

        theta1_current, theta2_current, trail = move_to(
            x, y,
            pen_down=True,
            theta1_current=theta1_current,
            theta2_current=theta2_current,
            trail=trail,
            L1=L1,
            L2=L2,
            Kp=Kp,
            tolerance=tolerance
        )

    print(f"Completed contour {i+1}/{len(all_contours)}")
    trail.append([])