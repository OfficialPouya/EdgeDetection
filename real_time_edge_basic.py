import cv2  
import numpy as np 
  
cap = cv2.VideoCapture(1) 
  
while(1): 
  
    ret, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([30,150,50]) 
    upper_red = np.array([255,255,180]) 
    
    mask = cv2.inRange(hsv, lower_red, upper_red) 
    res = cv2.bitwise_and(frame,frame, mask= mask) 
  
    # Display an original image 

    cv2.imshow('Original',frame)
    cv2.resizeWindow('Original', 800, 800)
    edges = cv2.Canny(frame,150,150) 
    cv2.imshow('Edges',edges) 
    cv2.resizeWindow('Edges', 800, 800)
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  