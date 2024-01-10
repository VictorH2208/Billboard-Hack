import numpy as np
from numpy.linalg import inv, norm
from scipy.linalg import null_space

def dlt_homography(I1pts, I2pts):
    """
    Find perspective Homography between two images.

    Given 4 points from 2 separate images, compute the perspective homography
    (warp) between these points using the DLT algorithm.

    Parameters:
    ----------- 
    I1pts  - 2x4 np.array of points from Image 1 (each column is x, y).
    I2pts  - 2x4 np.array of points from Image 2 (in 1-to-1 correspondence).

    Returns:
    --------
    H  - 3x3 np.array of perspective homography (matrix map) between image coordinates.
    A  - 8x9 np.array of DLT matrix used to determine homography.
    """
    #--- FILL ME IN ---

    # Create empty palceholder matrix for A
    A = np.empty((0, 9))

    # Update A matrix by creating the A_i for each set of points first following the equation given using np.vstack that stack the A_i vertically
    for i in range(4):
        A_i = np.array([[-I1pts[0, i], -I1pts[1, i], -1, 0, 0, 0, I2pts[0, i] * I1pts[0, i], I2pts[0, i] * I1pts[1, i], I2pts[0, i]],
                       [0, 0, 0, -I1pts[0, i], -I1pts[1, i], -1, I2pts[1, i] * I1pts[0, i], I2pts[1, i] * I1pts[1, i], I2pts[1, i]]])
        A = np.vstack((A, A_i))

    # Find the null space of A to give H because Ah = 0
    h = null_space(A)[:, -1]

    # Reshape h to 3x3 matrix while at the same time dividing by h[-1] to normalize the matrix
    H = np.reshape(h/h[-1], (3,3))

    #------------------
    return H, A