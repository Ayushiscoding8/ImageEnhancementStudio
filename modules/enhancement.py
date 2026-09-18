import cv2
import numpy as np


def adjust_brightness_contrast(image, brightness=0, contrast=1.0):
    """Apply a linear brightness/contrast transformation."""
    result = image.astype(np.float32)
    result = result * contrast + brightness
    return np.clip(result, 0, 255).astype(np.uint8)


def reduce_noise(image):
    """Reduce small-scale noise using Gaussian smoothing."""
    return cv2.GaussianBlur(image, (5, 5), 0)


def enhance_contrast(image):
    """Improve local luminance contrast with CLAHE."""
    lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_l = clahe.apply(l_channel)

    enhanced_lab = cv2.merge((enhanced_l, a_channel, b_channel))
    return cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2RGB)
