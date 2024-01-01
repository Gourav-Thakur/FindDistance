import cv2 as cv
from detectAruco import detectAruco
from findPos import findPos
import json

if __name__=="__main__":

    b = 300

    myjson = open('calibration.json', 'r')
    jsondata = myjson.read()

    obj = json.loads(jsondata)
    cameraMatrix = obj['cameraMatrix']

    # The path of both images, path1-left image; path2-right image

    path1 = "Images/Aruco/img120Left.jpg"
    path2 = "Images/Aruco/img120Right.jpg"

    img1 = cv.imread(path1)
    img2 = cv.imread(path2)

    d1 = detectAruco(img1)
    d2 = detectAruco(img2)

    coor1 = tuple(d1[30])
    coor2 = tuple(d2[30])
    aruco30 = [coor1, coor2]

    coordinate = findPos(aruco30, cameraMatrix, b)

    print()
    print("Depth - ", int(coordinate[2]/10), "cm.")
    print("x-coor : ", int(coordinate[0]/10), "cm.")
    print("y-coor : ", int(coordinate[1]/10), "cm.")
    print()

