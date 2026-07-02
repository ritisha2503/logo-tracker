# 2-DOF Robot Arm Logo Tracer

A Python simulation of a 2-DOF planar robotic manipulator that traces the IIT Kharagpur logo using image processing, inverse kinematics, and proportional control.

## Features

- Forward Kinematics (FK)
- Inverse Kinematics (IK)
- Proportional (P) Controller
- Smooth trajectory following
- Image processing using OpenCV
- Automatic contour extraction from images
- Robot animation using Matplotlib

---

## Project Structure

```
.
├── main.py
├── src
|   ├── forward_kinematics.py
|   ├── inverse_kinematics.py
|   ├── trajectory_following.py
|   ├── image_processing.py
|   └──  kgp_logo.png
└── README.md
```

---

## Working

The project follows the pipeline:

```
Image
   ↓
Grayscale
   ↓
Binary Threshold
   ↓
Contour Extraction
   ↓
Coordinate Transformation
   ↓
Inverse Kinematics
   ↓
Proportional Controller
   ↓
Forward Kinematics
   ↓
Robot Animation
```

---

## Forward Kinematics

For a two-link planar manipulator,

\[
x_1=L_1\cos\theta_1
\]

\[
y_1=L_1\sin\theta_1
\]

\[
x=x_1+L_2\cos(\theta_1+\theta_2)
\]

\[
y=y_1+L_2\sin(\theta_1+\theta_2)
\]

---

## Inverse Kinematics

The joint angles are computed using

\[
D=\frac{x^2+y^2-L_1^2-L_2^2}{2L_1L_2}
\]

\[
\theta_2=\operatorname{atan2}\left(-\sqrt{1-D^2},D\right)
\]

\[
\theta_1=\operatorname{atan2}(y,x)-\operatorname{atan2}(L_2\sin\theta_2,L_1+L_2\cos\theta_2)
\]

---

## Requirements

Install the required libraries:

```bash
uv add -r requirements.txt
```

---

## Running the Project

```bash
python main.py
```

---

## Concepts Used

- Robotics
- Forward Kinematics
- Inverse Kinematics
- Feedback Control
- Image Processing
- Contour Detection
- Trajectory Planning

---

## Video Demonstration


---

## Challenges

- Implementing inverse kinematics correctly.
- Converting image coordinates to robot coordinates.
- Selecting suitable contour retrieval methods.
- Tuning the proportional controller.
- Handling contour traversal and pen-up/pen-down behavior.

---

## Future Improvements

- PID control instead of P control.
- Better pen-up/pen-down implementation.
- Contour optimization for smoother trajectories.
- Real-time visualization using Pygame.
- Hardware implementation on a physical 2-DOF robot.

---

## Demo

The robot extracts contours from the IIT Kharagpur logo and traces them using inverse kinematics and closed-loop control, producing a complete animated drawing.