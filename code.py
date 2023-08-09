import cv2
import numpy as np

webcam = cv2.videoCapture(0)
while(1):
  #reading the video from webcam in image frames
  _, imageFrame = webcam.read()
  
  #convert the image frame in BGR to HSV color space
  hsvFrame = cv2.cvtColor(imageFrame , cv2.COLOR_BGR2HSV)
  
  #set range for red color and define mask
  red_lower = np.array([136,87,111] , np.uint8)
  red_upper = np
  array([180,255,255] , np.uint8)
  red_mask = cv2.inRange(hsvFrame , red_lower , red_upper)

  #set range for green colour and define mask
  green_lower = np.array([25, 52, 72], np.uint8)
  green_upper = np.array([102, 255, 255], np.uint8)
  green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
  
  # Set range for blue color and define mask
  blue_lower = np.array([94, 80, 2], np.uint8)
  blue_upper = np.array([120, 255, 255], np.uint8)
  blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

  kernal = np.ones((5,5) , "uint8")

  #dilation for red colour:
  red_mask = cv2.dilate(red_mask , kernal)
  #masking for only the needed portion of the image:
  res_red = cv2.bitwise_and(imageFrame , imageFrame , mask = red_mask)


  #dilation for blue color:
  blue_mask = cv2.dilate(blue_mask , kernal)
  #masking for only the needed portion of the image:
  res_blue = cv2.bitwise_and(imageFrame , imageFrame , mask = blue_mask)

  #dilation for green color:
  green_mask = cv2.dilate(green_mask , kernal)
  #masking for only the needed portion of the image:
  res_green = cv2.bitwise_and(imageFrame , imageFrame , mask = green_mask)

#creating contours for red colour:
  contours , hierarchy = cv2.findContours(red_mask , cv2.RETR_TREE ,     cv2.CHAIN_APPROX_SIMPLE)

#creating an area for the contours:
  for pic , contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x , y , w , h = cv2.boundingRect(contour)
      imageFrame = cv2.rectangle(imageFrame , (x,y) ,(x+w , y+h),     (0,0,255) , 2)
      cv2.putText(imageFrame , "Red colour" , (x,y) ,   cv2.FONT_HERSHEY_SIMPLEX , 1.0 , (0,0,255))

#creating contours for green colour:
  contours , hierarchy = cv2.findContours(green_mask , cv2.RETR_TREE ,   cv2.CHAIN_APPROX_SIMPLE)

#creating an area for the contours:
  for pic , contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x , y , w , h = cv2.boundingRect(contour)
      imageFrame = cv2.rectangle(imageFrame , (x,y) ,(x+w , y+h), (0,255,0) , 2)
      cv2.putText(imageFrame , "Red colour" , (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 1.0 , (0,255,0))

#creating contours for blue colour:
  contours , hierarchy = cv2.findContours(blue_mask , cv2.RETR_TREE ,   cv2.CHAIN_APPROX_SIMPLE)

#creating an area for the contours:
  for pic , contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
      x , y , w , h = cv2.boundingRect(contour)
      imageFrame = cv2.rectangle(imageFrame , (x,y) ,(x+w , y+h), (255,0,0) , 2)
      cv2.putText(imageFrame , "Red colour" , (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 1.0 , (255,0,0))

#MAIN
  cv2.imshow("BGR color detection in Real-Time" , imageFrame)
  if cv2.waitKey(10) & 0xFF == ord('q'):
    webcam.release()
    cv2.destroyAllWindows()
    break





  
  

