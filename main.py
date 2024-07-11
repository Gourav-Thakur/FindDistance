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
    
    key1 = list(d1.keys())
    key2 = list(d2.keys())

    key1.sort()
    key2.sort()
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
    print("Distance between them -", round(distance/10, 2), "cm.")
    print("-"*10)
    print()

    # show left image
    cv.circle(img1, tuple(map(int, coor1l)), int(25000//coordinate1[2]), (0, 0, 255), -1)
    cv.circle(img1, tuple(map(int, coor2l)), int(25000//coordinate2[2]), (0, 0, 255), -1)
    # make a double headed arrow from coor1l to coor2l
    cv.arrowedLine(img1, tuple(map(int, coor1l)), tuple(map(int, coor2l)), (0, 0, 255), 10, tipLength=100/coordinate2[2])
    cv.arrowedLine(img1, tuple(map(int, coor2l)), tuple(map(int, coor1l)), (0, 0, 255), 10, tipLength=100/coordinate1[2])
    # add text on the line
    cv.putText(img1, str(round(distance/10, 2))+" cm", (int((coor1l[0]+coor2l[0])/2), int((coor1l[1]+coor2l[1])/2)), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
    cv.imshow("left", img1)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=="__main__":
    main()
    

