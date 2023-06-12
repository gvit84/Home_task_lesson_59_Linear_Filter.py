import cv2
import numpy as np

def median_sobel(image_path):
     img = cv2.imread(image_path)
     cv2.imshow('original', img)

     img_median = cv2.medianBlur(img, 3)
     cv2.imshow("median", img_median)

     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     kernel_x = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
     kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
     edges_x = cv2.filter2D(gray, -1, kernel_x)
     edges_y = cv2.filter2D(gray, -1, kernel_y)
     edges = edges_x + edges_y
     cv2.imshow("sobel", edges)

     cv2.waitKey(0)

image_path = 'D:/MyPycharmProjects/Data_science_lesson59_Linear_Filter/noisekoala.jpeg'
median_sobel(image_path)




