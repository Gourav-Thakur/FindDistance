def findPos(arucoPositions, cameraMatrix, b):
    fx = cameraMatrix[0, 0]
    fy = cameraMatrix[1, 0]
    ox = cameraMatrix[0, 2]
    oy = cameraMatrix[1, 2]

    _3dPos = []

    for arucoPos in arucoPositions:
        x_2d = arucoPos[0]
        y_2d = arucoPos[1]

        