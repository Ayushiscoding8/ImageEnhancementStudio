# Image Enhancement Studio

A small VITyarthi Computer Vision project built with Python, OpenCV, NumPy, and Streamlit.

## Overview
Image Enhancement Studio demonstrates classical image processing techniques on a user-provided image. It provides brightness and contrast adjustment, Gaussian noise reduction, CLAHE local contrast enhancement, grayscale conversion, Canny edge detection, and basic intensity statistics.

## Three Functional Modules
1. **Preprocessing** — image upload, validation, and resizing.
2. **Enhancement** — brightness/contrast, Gaussian blur, and CLAHE.
3. **Analysis** — grayscale conversion, Canny edge detection, and image statistics.

## Technologies
- Python 3
- OpenCV
- NumPy
- Streamlit

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
streamlit run app.py
```

## Project Structure
```text
ImageEnhancementStudio/
├── app.py
├── requirements.txt
├── README.md
├── statement.md
└── modules/
    ├── __init__.py
    ├── preprocessing.py
    ├── enhancement.py
    └── analysis.py
```

## Testing
Test with JPG, JPEG, and PNG images. Try different brightness/contrast values and toggle Gaussian Blur and CLAHE. Verify grayscale, edge-map, and statistics outputs.

## VITyarthi Alignment
The project focuses on static-image processing topics, especially image enhancement, filtering, histogram-based processing, and edge detection. It does not use video processing, motion analysis, or 3D vision as core features.

## Author
Ayush Makhija 
24BAI10283
