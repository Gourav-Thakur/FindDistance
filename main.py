import cv2 as cv
from detectAruco import detectAruco
from findPos import findPos
import json

def main():
    b = 300

    myjson = open('calibration.json', 'r')
    jsondata = myjson.read()

    obj = json.loads(jsondata)
    cameraMatrix = obj['cameraMatrix']

    # The path of both images, path1-left image; path2-right image

    path1 = "Images/Aruco/left.jpeg"
    path2 = "Images/Aruco/right.jpeg"

    img1 = cv.imread(path1)
    img2 = cv.imread(path2)

    d1 = detectAruco(img1)
    d2 = detectAruco(img2)
    # print(d1)
    # print(d2)
    key1 = list(d1.keys())
    key2 = list(d2.keys())

    key1.sort()
    key2.sort()
    print(key1, key2)
    if len(key1)<2 or len(key2)<2:
        print("All markers not detected...")
        return

    coor1l = tuple(d1[key1[0]])
    coor1r = tuple(d2[key2[0]])

    aruco30 = [coor1l, coor1r]

    coordinate1 = findPos(aruco30, cameraMatrix, b)

    coor2l = tuple(d1[key1[1]])
    coor2r = tuple(d2[key2[1]])

    aruco = [coor2l, coor2r]

    coordinate2 = findPos(aruco, cameraMatrix, b)

    distance = (coordinate1[0]-coordinate2[0])**2 + (coordinate1[1]-coordinate2[1])**2 + (coordinate1[2] - coordinate2[2])**2
    distance = distance**0.5

    print("-"*10)
    print("Coodinates of aruco-", key1[0])
    print("\tx-", int(coordinate1[0]/10), "cm.")
    print("\ty-", int(coordinate1[1]/10), "cm.")
    print("\tz-", int(coordinate1[2]/10), "cm.")
    print("-"*10)
    print("Coodinates of aruco-", key1[1])
    print("\tx-", int(coordinate2[0]/10), "cm.")
    print("\ty-", int(coordinate2[1]/10), "cm.")
    print("\tz-", int(coordinate2[2]/10), "cm.")
    print("-"*10)
    print()
    print("Distance between them -", int(distance)/10, "cm.")
    print("-"*10)
    print()

if __name__=="__main__":
    main()
    

