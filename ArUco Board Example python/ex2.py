# -*- coding: utf-8 -*-


import numpy as np
import sys
import imutils
import cv2, PIL
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import cv2.aruco as aruco

total = 0
cap = cv2.VideoCapture(0)

while(total < 1000):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    
    #print(frame.shape) #480x640
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()

    #print(parameters)

    '''    detectMarkers(...)
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''
        #lists of ids and the corners beloning to each id
    corners, idss, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    gray = aruco.drawDetectedMarkers(gray, corners)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, idss)
    # verify *at least* one ArUco marker was detected
    if len(corners) > 0 and len(frame) > 0:
        total = total + 1
        print(idss , "\n")
        # flatten the ArUco IDs list
        ids = idss.flatten()
        
    
        for(markerCorner, markerID) in zip(corners, ids):
            
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            
            # draw the bounding box of the ArUCo detection
            cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
            # compute and draw the center (x, y)-coordinates of the
            # ArUco marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
            # draw the ArUco marker ID on the frame
            print(markerID , "\n")
            cv2.putText(frame, str(markerID),
                        (topLeft[0], topLeft[1] - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 0), 2)
    '''size_of_marker =  0.0145 # side lenght of the marker in meter
    rvecs,tvecs, trash = aruco.estimatePoseSingleMarkers(corners, size_of_marker , mtx, dist)'''     
    #It's working.
    # my problem was that the cellphone put black all around it. The alrogithm
    # depends very much upon finding rectangular black blobs

            

    
    #print(rejectedImgPoints)
    # Display the resulting frame

    cv2.imshow("ArUco Board",frame)
    

            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()