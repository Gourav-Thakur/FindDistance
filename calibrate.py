import cv2 as cv
import numpy as np
import os
import json
import glob

# Termination Criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

cwd = os.getcwd()
calibImgPath = os.path.join(cwd, "Images/Calibration/")
imgList = os.listdir(calibImgPath)

imgList = glob.glob("Images/Calibration/*.jpg")

chessboardSize = (17, 11)
frameSize = (4032, 3024)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 9
objp = objp * size_of_chessboard_squares_mm

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

def calibrate():
    for imgName in imgList:
        # imgPath = os.path.join(calibImgPath, imgName)
        img = cv.imread(imgName)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
    return cameraMatrix

if __name__ == "__main__":
    cameraMatrix = calibrate()
    
    dictionary = {
        "cameraMatrix": cameraMatrix.tolist()
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("calibration.json", "w") as outfile:
        outfile.write(json_object)
    
    print("Calibrated")