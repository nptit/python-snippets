__author__ = 'qxu'


# given a point [x,y] and a vector [[x1,y1],[x2,y2]]
# find whether the point is on the the vector (0),
# to the right (1), or to the left (-1)
def point_vs_vector(point, vector):
    # transform the random vector (p1, p2) into y axis (0, px)
    # move first point of the vector to origin

    p1,p2=vector
    # shift x1, y1 to origin, ax, ay are new end point for vector
    ax = p2[0]-p1[0]
    ay = p2[1]-p1[1]
    # px,py are new coordinates of point after origin change
    px= point[0]-p1[0]
    py= point[1]-p1[1]
    # calculate distance between ax,ay and origin
    dist=(ax**2+ay**2)**0.5
    # calculate rotation matrix
    ct = ay/dist
    st = ax/dist
    r11,r12,r21,r22= ct, -st, st,ct
    #print ax,ay,dist,r11,r12,r21,r22
    # calculate new point position using rotation matrix
    pxp=px*ct-st*py
    pyp=px*st+ct*py # not needed here
    print pxp,pyp
    if abs(pxp)<1.e-8:
        return 0
    elif pxp<0:
        return -1
    else:
        return 1

vector = [[0, 0], [1, 1]]
point = 0, 1
#print type(point)
vector=[[-5506, 6535], [-3907, -5901]]
point=[-547567, 4222339]
print point_vs_vector(point,vector)