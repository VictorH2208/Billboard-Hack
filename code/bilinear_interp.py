import numpy as np
from numpy.linalg import inv

def bilinear_interp(I, pt):
    """
    Performs bilinear interpolation for a given image point.

    Given the (x, y) location of a point in an input image, use the surrounding
    4 pixels to conmpute the bilinearly-interpolated output pixel intensity.

    Note that images are (usually) integer-valued functions (in 2D), therefore
    the intensity value you return must be an integer (use round()).

    This function is for a *single* image band only - for RGB images, you will 
    need to call the function once for each colour channel.

    Parameters:
    -----------
    I   - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).
    pt  - 2x1 np.array of point in input image (x, y), with subpixel precision.

    Returns:
    --------
    b  - Interpolated brightness or intensity value (whole number >= 0).
    """
    #--- FILL ME IN ---
    if pt.shape != (2, 1):
        raise ValueError('Point size is incorrect.')

    #Get neighboring pixel locations
    x1 = np.floor(pt[0].item(0)).astype(int)
    x2 = x1 + 1
    y1 = np.floor(pt[1].item(0)).astype(int)
    y2 = y1 + 1

    #Generate A matrix
    A = np.array([[1, x1, y1, x1*y1],
                [1, x1, y2, x1*y2],
                [1, x2, y1, x2*y1],
                [1, x2, y2, x2*y2]])

    #Solve for weights
    x = np.array([1, pt[0].item(0), pt[1].item(0), pt[0].item(0)*pt[1].item(0)])
    w = inv(A).T@x

    # #New intensity is w * Intensity and round to integer
    b = round(w[0]*I[y1, x1] + w[1]*I[y2, x1] + w[2]*I[y1, x2] + w[3]*I[y2, x2], 0)
    #------------------

    return b