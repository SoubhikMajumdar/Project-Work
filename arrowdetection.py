# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:54:01 2019

@author: Soubhik Majumdar
"""

# OpenCV program to perform Edge detection in real time 
# import libraries of python OpenCV  
# where its functionality resides 
import cv2  
  
# np is an alias pointing to numpy library 
import numpy as np 
  
  
# capture frames from a camera 
cap = cv2.VideoCapture(0) 
  
l=0;
# loop runs if capturing has been initialized 
while(1): 
  
    # reads frames from a camera 
    ret, frame = cap.read() 
  
    # converting BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
      
    # define range of red color in HSV 
    lower_red = np.array([30,150,50]) 
    upper_red = np.array([255,255,180]) 
      
    # create a red HSV colour boundary and  
    # threshold HSV image 
    mask = cv2.inRange(hsv, lower_red, upper_red) 
  
    # Bitwise-AND mask and original image 
    res = cv2.bitwise_and(frame,frame, mask= mask) 
  
    # Display an original image 
    cv2.imshow('Original',frame) 
  
    # finds edges in the input image image and 
    # marks them in the output map edges 
    edges = cv2.Canny(frame,100,200) 
  
    # Display edges in a frame 
    cv2.imshow('Edges',edges)
    
       
    
    
    ################################################################################
    lines = cv2.HoughLines(edges,1,np.pi/180,20)
#create an array for each direction, where array[0] indicates one of the lines and array[1] indicates the other, which if both > 0 will tell us the orientation
    left = [0, 0]
    right = [0, 0]
    up = [0, 0]
    down = [0, 0]
#iterate through the lines that the houghlines function returned
    for object in lines:
        theta = object[0][1]
        rho = object[0][0]
        #cases for right/left arrows
        if ((np.round(theta, 2)) >= 1.0 and (np.round(theta, 2)) <= 1.1) or ((np.round(theta,2)) >= 2.0 and (np.round(theta,2)) <= 2.1):
            if (rho >= 20 and rho <=  30):
                left[0] += 1
            elif (rho >= 60 and rho <= 65):
                left[1] +=1
            elif (rho >= -73 and rho <= -57):
                right[0] +=1
            elif (rho >=148 and rho <= 176):
                right[1] +=1
                            #cases for up/down arrows
        elif ((np.round(theta, 2)) >= 0.4 and (np.round(theta,2)) <= 0.6) or ((np.round(theta, 2)) >= 2.6 and (np.round(theta,2))<= 2.7):
            if (rho >= -63 and rho <= -15):
                up[0] += 1
            elif (rho >= 67 and rho <= 74):
                down[1] += 1
                up[1] += 1
            elif (rho >= 160 and rho <= 171):
                down[0] += 1
                                            
        if left[0] >= 1 and left[1] >= 1:
            print("left")
        elif right[0] >= 1 and right[1] >= 1:
            print("right")
        elif up[0] >= 1 and up[1] >= 1:
            print("up")
        elif down[0] >= 1 and down[1] >= 1:
            print("down")
                                                            
       # print(up, down, left, right)
       # Wait for Esc key to stop 
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break 

  
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  