'''__author__ = "Swarup Maity"
__copyright__ = "Copyright (c) 2024 Swarup Maity"
__verision__ = "1.0"'''

import cv2 as cv
from tkinter import filedialog
import os
import numpy as np

def get_image_file(directory):
    """Get a list of image files in the specified directory."""
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist")
    
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and any(f.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png'])]
    return image_files


def ratio_test(matches):
    return [m for m, n in matches if m.distance < 0.7 * n.distance]



def process_image_pair(image_files, directory):

    for l_img in range(len(image_files)-1):
         
         img_i = image_files[l_img]
         img_j = image_files[l_img + 1] 

         image_path1 = os.path.join(directory, img_i)
         image_path2 = os.path.join(directory, img_j)

         gray_img1 = cv.imread(image_path1, 0)
         gray_img2 = cv.imread(image_path2, 0)

         # # nfeature parameter will limit the kepoints computation
         sift = cv.xfeatures2d.SIFT_create(nfeatures=1000)

         # Detect feature from the image
         keypoints1, descriptors1 = sift.detectAndCompute(gray_img1, None)
         keypoints2, descriptors2 = sift.detectAndCompute(gray_img2, None)
        
         # Keypoints matching
         flann = cv.FlannBasedMatcher()
         matches = flann.knnMatch(descriptors1, descriptors2, k=2)

         #ratio test
         good_matches = ratio_test(matches)

         MIN_MATCH_COUNT = 10
         if len(good_matches) > MIN_MATCH_COUNT:
                 # compute Homography matrix (Fij)

                 points_i = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
                 points_j = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

                 H, _ = cv.findHomography(points_i, points_j, cv.RANSAC, 5.0)
                 result = cv.warpPerspective(gray_img1, H, (gray_img1.shape[1], gray_img2.shape[0]))

                 otsu_threshold, image_result = cv.threshold(result, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
                
                 number_of_white_pix = cv.countNonZero(image_result)

                 # Total pixel count
                 total_pix = result.shape[0] * result.shape[1]

                 area = (number_of_white_pix/total_pix)*100
                 print("Threshold and Area:", (otsu_threshold, area))
         else:
              raise ValueError("Not found enough good matches ")


def main():        
   
    directory = filedialog.askdirectory(title="select image folder:")
    img_list = get_image_file(directory)

    process_image_pair(img_list, directory)
    

if __name__ =="__main__":
    main()