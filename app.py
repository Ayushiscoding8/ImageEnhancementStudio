import streamlit as st

from modules.preprocessing import load_image, resize_image
from modules.enhancement import (
    adjust_brightness_contrast,
    reduce_noise,
    enhance_contrast,
)
from modules.analysis import (
    convert_grayscale,
    detect_edges,
    calculate_statistics,
)

st.set_page_config(page_title="Image Enhancement Studio", page_icon="🖼️", layout="wide")
st.title("🖼️ Image Enhancement Studio")
st.caption("Classical Computer Vision using Python and OpenCV")

uploaded_file = st.sidebar.file_uploader(
    "Upload an image", type=["jpg", "jpeg", "png"]
)

if uploaded_file is None:
    st.info("Upload an image from the sidebar to begin.")
    st.stop()

try:
    image = resize_image(load_image(uploaded_file))

    st.sidebar.header("Enhancement Controls")
    brightness = st.sidebar.slider("Brightness", -100, 100, 0)
    contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0, 0.1)
    apply_blur = st.sidebar.checkbox("Apply Gaussian Blur")
    apply_clahe = st.sidebar.checkbox("Apply CLAHE")

    enhanced = adjust_brightness_contrast(image, brightness, contrast)
    if apply_blur:
        enhanced = reduce_noise(enhanced)
    if apply_clahe:
        enhanced = enhance_contrast(enhanced)

    grayscale = convert_grayscale(enhanced)
    edges = detect_edges(enhanced)

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    st.subheader("Processed Results")
    col1, col2 = st.columns(2)
    with col1:
        st.image(enhanced, caption="Enhanced Image", use_container_width=True)
    with col2:
        st.image(grayscale, caption="Grayscale Image", use_container_width=True)

    st.subheader("Canny Edge Detection")
    st.image(edges, caption="Detected Edges", use_container_width=True)

    st.subheader("Image Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Original")
        st.json(calculate_statistics(image))
    with col2:
        st.write("Enhanced")
        st.json(calculate_statistics(enhanced))

    st.success("Image processing completed successfully.")
except Exception as error:
    st.error(f"Processing error: {error}")
