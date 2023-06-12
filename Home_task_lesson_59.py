import cv2
import numpy as np

def median_sobel(image_path):
     img = cv2.imread(image_path)
     cv2.imshow('original', img)

     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
     sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
     sobel_x = np.abs(sobel_x)
     sobel_y = np.abs(sobel_y)
     sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
     sobel_combined = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
     cv2.imshow('sobel', sobel_combined)
     img_median = cv2.medianBlur(img, 3)
     cv2.imshow("median", img_median)
     cv2.waitKey(0)

image_path = 'D:/MyPycharmProjects/Data_science_lesson59_Linear_Filter/noisekoala.jpeg'
median_sobel(image_path)
