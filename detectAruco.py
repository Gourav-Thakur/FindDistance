import cv2 as cv
import numpy as np

arucoDictType = cv.aruco.DICT_5X5_100
arucoDict = cv.aruco.getPredefinedDictionary(arucoDictType)
arucoParams = cv.aruco.DetectorParameters()

def detectAruco(img):
    arucoDictType = cv.aruco.DICT_5X5_100
    arucoDict = cv.aruco.getPredefinedDictionary(arucoDictType)
    arucoParams = cv.aruco.DetectorParameters()
    (corners, ids, rejected) = cv.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
    
    markersPos = {}

    if len(corners) > 0:
        ids = ids.flatten()

        for (markerCorner, markerId) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            cx = (topLeft[0] + bottomRight[0])/2.0
            cy = (topLeft[1] + bottomRight[1])/2.0

            markersPos[markerId] = [cx, cy]
    
    return markersPos

def showAruco(path):
    img = cv.imread(path)
    print(detectAruco(img))

if __name__ == "__main__":
    showAruco("Image/Aruco/ArucoMarker.jpeg")