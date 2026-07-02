import numpy as np

def ik(x, y, L1, L2):
    r = np.sqrt(x**2 + y**2)
    D = (r**2 - L1**2 - L2**2) / (2 * L1 * L2)
    if abs(D) > 1:
        return None, None
    
    D = np.clip(D, -1, 1)
    theta2 = np.arctan2(-np.sqrt(1 - D**2), D)

    theta1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))
    return theta1, theta2