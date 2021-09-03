import interface
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import io
from urllib.request import urlopen
import cv2
from collections import deque 
  

   
# default called trackbar function  
def setValues(x): 
   print("") 
   
  

cv2.namedWindow("Color detectors") 
cv2.createTrackbar("Upper Hue", "Color detectors", 
                   131, 180, setValues) 
cv2.createTrackbar("Upper Saturation", "Color detectors", 
                   255, 255, setValues) 
cv2.createTrackbar("Upper Value", "Color detectors",  
                   125, 255, setValues) 
cv2.createTrackbar("Lower Hue", "Color detectors", 
                   108, 180, setValues) 
cv2.createTrackbar("Lower Saturation", "Color detectors",  
                   137, 255, setValues) 
cv2.createTrackbar("Lower Value", "Color detectors",  
                   49,255, setValues) 
  


# The kernel to be used for dilation purpose 
kernel = np.ones((5,5), np.uint8)
#uint8 => 8 bit unsigned integer => 0-255
#np.ones => returns an array filled with ones
#(5,5) size of array here 2d array of 5column 5row

interface.top.update()
# Loading the default webcam of PC. 
cap = cv2.VideoCapture(0)


canvas = None
x1,y1=0,0



# Keep looping 
while True: 
      
    # Reading the frame from the camera 
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Tracking", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Flipping the frame to see same side of yours 

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    if canvas is None:
       canvas = np.zeros_like(frame)

    # Getting the updated positions of the trackbar 
    # and setting the HSV values 
    u_hue = cv2.getTrackbarPos("Upper Hue", 
                               "Color detectors") 
    u_saturation = cv2.getTrackbarPos("Upper Saturation", 
                                      "Color detectors") 
    u_value = cv2.getTrackbarPos("Upper Value", 
                                 "Color detectors") 
    l_hue = cv2.getTrackbarPos("Lower Hue", 
                               "Color detectors") 
    l_saturation = cv2.getTrackbarPos("Lower Saturation", 
                                      "Color detectors") 
    l_value = cv2.getTrackbarPos("Lower Value", 
                                 "Color detectors") 
    Upper_hsv = np.array([u_hue, u_saturation, u_value]) 
    Lower_hsv = np.array([l_hue, l_saturation, l_value]) 
   
    # Identifying the pointer by making its  
    # mask 
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv) 
    Mask = cv2.erode(Mask, kernel, iterations = 2) 
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel) 
    Mask = cv2.dilate(Mask, kernel, iterations = 2) 
   
    # Find contours for the pointer after  
    # idetifying it
    #cnts => all the contours found
    #_ => hierarchy of the contours
    cnts, _ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)
    #three arguments 1.source image 2.contour retrieval mode 3.contour approximation method => cv2.CHAIN_APPROX_SIMPLE => instead of showing the full boundary shows only the end points to save 
    #cv2_RETR_EXTERNAL gives "outer" contours, so if you have (say) one contour enclosing another (like concentric circles), only the outermost is given.

    # Ifthe contours are formed 
    #drawing contours
    if len(cnts) > 0:
          
        # sorting the contours to find biggest area  
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
          
        # Get the radius of the enclosing circle 
        # around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
          
        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        if(x1==0 and y1==0):
           x1,y1=cX,cY
        else:
           #canvas=cv2.line(canvas,(x1,y1),(cX,cY),[255,255,255],4)
           interface.myCanvas.create_line(x1, y1, cX, cY,fill="#000000")
        x1,y1=cX,cY
    else:
       x1,y1=0,0
     
    frame=cv2.add(frame,canvas)
    interface.top.update()     
        
        
        
       
   
    # Show all the windows 
    cv2.imshow("Tracking", frame) 
    cv2.imshow("mask", Mask) 
    # If the 'q' key is pressed then stop the application  
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and all resources 
cap.release() 
cv2.destroyAllWindows() 
