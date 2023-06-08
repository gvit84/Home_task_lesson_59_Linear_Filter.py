import cv2

def median_sobel(image_path):
    img = cv2.imread(image_path)
    cv2.imshow('original', img)

    img_sobel = cv2.Sobel(img, ddepth=-1, dx=1, dy=0, ksize=3)
    cv2.imshow("sobel", img_sobel)

    img_median = cv2.medianBlur(img, 3)
    cv2.imshow("median", img_median)

    cv2.waitKey(0)

image_path = 'D:/MyPycharmProjects/Data_science_lesson59_Linear_Filter/noisekoala.jpeg'
median_sobel(image_path)
