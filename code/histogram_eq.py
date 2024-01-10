import numpy as np

def histogram_eq(I):
    """
    Histogram equalization for greyscale image.

    Perform histogram equalization on the 8-bit greyscale intensity image I
    to produce a contrast-enhanced image J. Full details of the algorithm are
    provided in the Szeliski text.

    Parameters:
    -----------
    I  - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).

    Returns:
    --------
    J  - Contrast-enhanced greyscale intensity image, 8-bit np.array (i.e., uint8).
    """
    #--- FILL ME IN ---

    # Verify I is grayscale.
    if I.dtype != np.uint8:
        raise ValueError('Incorrect image format!')
    
    histogram = np.zeros(256)
    # Compute the histogram of I.
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            histogram[I[i,j]] += 1

    total_pixels = I.shape[0] * I.shape[1]
    # Compute the cumulative sum of the histogram using dynamic programming.
    cumulative_sum = np.zeros(256)
    cumulative_sum[0] = histogram[0]/total_pixels*255
    for i in range(1, 256):
        cumulative_sum[i] = histogram[i]/total_pixels*255 + cumulative_sum[i-1]
            
    # Compute the equalized image.
    J = np.zeros(I.shape)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            J[i,j] = round(cumulative_sum[I[i,j]],0)
    #------------------
    return J
