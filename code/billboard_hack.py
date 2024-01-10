# Billboard hack script file.
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq

def billboard_hack():
    """
    Hack and replace the billboard!

    Parameters:
    ----------- 

    Returns:
    --------
    Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
    """
    # Bounding box in Y & D Square image.
    bbox = np.array([[404, 490, 404, 490], [38,  38, 354, 354]])

    # Point correspondences.
    Iyd_pts = np.array([[416, 485, 488, 410], [40,  61, 353, 349]])
    Ist_pts = np.array([[2, 218, 218, 2], [2, 2, 409, 409]])

    Iyd = imread('../billboard/yonge_dundas_square.jpg')
    Ist = imread('../billboard/uoft_soldiers_tower_dark.png')

    Ihack = np.asarray(Iyd)
    Ist = np.asarray(Ist)

    #--- FILL ME IN ---

    # Let's do the histogram equalization first.
    J = histogram_eq(Ist)

    # Compute the perspective homography we need...
    H, A = dlt_homography(Iyd_pts, Ist_pts)

    #create bounds from IYDS
    bounds = Path([(416, 40), (485, 61), (488, 353), (410, 349)])

    # Loop through the pixels in the bounding box
    for i in range(404, 490):
        for j in range(38, 354):
            # Check if the current pixel is within the bounds of the bounding box
            if bounds.contains_points([(i,j)]):
                # Perform the warp using the homography
                pt = H @ np.array([i,j,1])
                pt = pt / pt[2]
                # Rehape to (2,1) as before it is (2,)
                pt = np.reshape([pt[0], pt[1]], (2,1))

                # Perform the bilinear interpolation in the YD image for all three channels
                for k in range(3):
                    Ihack[j][i][k] = bilinear_interp(J, pt)

    #------------------
    # import matplotlib.pyplot as plt
    # plt.imshow(Ihack)
    # plt.show()
    # imwrite(Ihack, 'billboard_hacked.png');

    return Ihack

if __name__ == "__main__":
    billboard_hack()
