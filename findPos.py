def findPos(arucopos, cameraMatrix, b):
    f_x = cameraMatrix[0][0]
    f_y = cameraMatrix[1][1]
    o_x = cameraMatrix[0][2]
    o_y = cameraMatrix[1][2]

    _3dPos = []

    u_l = arucopos[0][0]
    v_l = arucopos[0][1]

    u_r = arucopos[1][0]
    v_r = arucopos[1][1]

    x = b*(u_l - o_x)/(u_l - u_r)
    y = b*f_x*(v_l - o_y)/(f_y*(u_l - u_r))
    z = b*f_x/(u_l - u_r)

    _3dPos.append(x)
    _3dPos.append(y)
    _3dPos.append(z)
    
    # print("u_l-", u_l)
    # print("u_r-", u_r)
    # print("f_y-", f_y)

    return _3dPos

        