import tensorflow as tf
import numpy as np
import math
import cv2

# Assumes 255 is the max pixel val
def psnr(reference, image):
    mse = np.mean((image - reference) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

# Wrapper for tensorflow's psnr func to provide max value
def tf_psnr(y_true, y_pred):
    return tf.image.psnr(y_true, y_pred, max_val=1.0)

def tf_ssim(y_true, y_pred):
    return tf.image.ssim(y_true, y_pred, max_val=1.0)
