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

    path1 = "Images/Aruco/img120Left.jpg"
    path2 = "Images/Aruco/img120Right.jpg"

    img1 = cv.imread(path1)
    img2 = cv.imread(path2)

    d1 = detectAruco(img1)
    d2 = detectAruco(img2)

    coor1 = tuple(d1[30])
    coor2 = tuple(d2[30])
    aruco30 = [coor1, coor2]

    print()
    print("Depth - ", (findPos(aruco30, cameraMatrix, b))[2])
    print()

    # print(type(coor))

    # cv.circle(img, coor, 20, (255, 0, 0), -1)
    # cv.imshow("hhiii", img)
    # cv.waitKey(2000)
