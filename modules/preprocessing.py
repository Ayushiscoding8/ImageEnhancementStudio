import cv2
import numpy as np


def load_image(uploaded_file):
    """Decode an uploaded image and return RGB data."""
    file_bytes = uploaded_file.getvalue()
    array = np.frombuffer(file_bytes, dtype=np.uint8)
    image_bgr = cv2.imdecode(array, cv2.IMREAD_COLOR)

    if image_bgr is None:
        raise ValueError("Invalid image file.")

    return cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)


def resize_image(image, max_width=1000):
    """Resize large images while preserving aspect ratio."""
    height, width = image.shape[:2]

    if width <= max_width:
        return image

    scale = max_width / width
    new_size = (int(width * scale), int(height * scale))
    return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
