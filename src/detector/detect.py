import cv2
import numpy as np
import matplotlib.pyplot as plt


def detect_color(raw_img_path,rgb_values,gray_color_img_path,final_img_path):

    img_bgr=cv2.imread(raw_img_path)
    img=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)
    b,g,r=rgb_values[::-1]
    bgr = np.uint8([[[b,g,r]]])
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    lowerLimit = hsv[0][0][0] - 10, 100, 100
    upperLimit = hsv[0][0][0] + 10, 255, 255
    print(np.array(upperLimit,dtype=np.uint8),np.array(lowerLimit,dtype=np.uint8))
    inrange_img=cv2.inRange(img,np.array(lowerLimit,dtype=np.uint8),np.array(upperLimit,dtype=np.uint8))
    cv2.imwrite(gray_color_img_path,inrange_img)
    bgr_color_detected_img=cv2.bitwise_and(img_bgr,img_bgr,mask=inrange_img)
    cv2.imwrite(final_img_path,bgr_color_detected_img)
if __name__=="__main__":
    detect_color("baloon.png",(0,255,255),"gray.png")