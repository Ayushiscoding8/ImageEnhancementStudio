import cv2


def convert_grayscale(image):
    """Convert RGB image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def detect_edges(image):
    """Detect edges using Canny edge detection."""
    gray = convert_grayscale(image)
    return cv2.Canny(gray, threshold1=100, threshold2=200)


def calculate_statistics(image):
    """Return basic grayscale intensity statistics."""
    gray = convert_grayscale(image)
    return {
        "Mean Intensity": round(float(gray.mean()), 2),
        "Minimum Intensity": int(gray.min()),
        "Maximum Intensity": int(gray.max()),
        "Standard Deviation": round(float(gray.std()), 2),
    }
