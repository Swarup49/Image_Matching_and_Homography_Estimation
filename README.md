Image Matching and Homography Estimation

Overview

This Python script performs image matching and homography estimation using the SIFT (Scale-Invariant Feature Transform) algorithm and RANSAC (Random Sample Consensus) for robust estimation. The code reads a directory of images, detects keypoints and computes descriptors using SIFT, matches keypoints between consecutive images, and estimates the homography matrix. Finally, it computes the area of overlap between images based on the homography transformation.

Features

Keypoint detection and descriptor computation using SIFT.
Keypoint matching using the FLANN (Fast Approximate Nearest Neighbor) algorithm.
Robust homography estimation using RANSAC.
Calculation of the area of overlap between images.

Requirements

Python 3.x
OpenCV (cv2) library
numpy library
tkinter library (for file dialog)

Usage

Clone the repository or download the image_matching_homography.py file.
Ensure you have the necessary libraries installed (opencv-python, numpy).
Run the script using Python:
python image_matching_homography.py
When prompted, select the directory containing the images you want to process.
The script will process each pair of consecutive images in the directory, compute the homography matrix, and print the threshold and area of overlap for each pair.

Note

Ensure that the images in the directory are named sequentially for accurate pairing (e.g., image1.jpg, image2.jpg, etc.).

License

This project is licensed under the MIT License - see the LICENSE file for details.

Author
Swarup Maity
