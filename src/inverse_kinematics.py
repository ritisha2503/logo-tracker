import numpy as np

L1 = 100
L2 = 80

def inverse_kinematics(x, y):
    r = np.sqrt(x**2 + y**2)
    D = (r**2 - L1**2 - L2**2) / (2 * L1 * L2)

    theta2 = np.arctan2(-np.sqrt(1 - D**2), D)

    phi = np.arctan2(y, x)
    beta = np.arccos((L1**2 + r**2 - L2**2)/(2*L1*r))

    theta1 = phi - beta
    return theta1, theta2