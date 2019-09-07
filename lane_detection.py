#python program for lane detection
import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(lane_image):
  ''' In this function , the image is converted into a gray scale image. This is followed by median blurring
  to smoothen the image. The final operation is canny edge detection and the reultant image is returned.'''
  gray=cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
  blur=cv2.medianBlur(gray, 5)
  canny= cv2.Canny(blur , 50 , 150 )
  return canny

def display(image, lines):
  '''In this function the detected lines are drwan on the original image(i.e draw lane lines) '''
  
  if lines is not None:
    for line in lines:
      x1,y1,x2,y2 = line.reshape(4)
      cv2.line(lane_image, (x1,y1) , (x2,y2) , (0 , 0, 255) , 8)
  return lane_image

def interest(lane_image):
  ''' In this function the first operation includes the location of the co-ordinate ppoints which in this case is a triangle.
  The co-ordinates were located by plotting using matplotlib.pyplot(not a part of the main code). A dark image was then superimposed with the triangular area
  using the fillPoly command. The masked image was obtained by performing bit wise and operation between the canny edged image and the superimposed image.
  White corresponds to 1 and black corresponds to zero. The masked image was returned.'''
  area=np.array([[(200,700) , (1100,700) , (550,250)]])
  mask = np.zeros_like(lane_image)
  cv2.fillPoly(mask,area , 255)  
  masked_image= cv2.bitwise_and(mask, result)
  return masked_image



image=cv2.imread("test_image.jpg")
lane_image=np.copy(image)
result= canny(lane_image)
result1=interest(result)
lines= cv2.HoughLinesP(result1 , 2, np.pi/180 , 100 , np.array([]) , minLineLength =40 , maxLineGap = 5) #using hough lines to detect the possible lines
line_image = display(lane_image,lines)
cv2.imshow('INTEREST' , lane_image)
cv2.waitKey(0)
