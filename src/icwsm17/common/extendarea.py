'''
Created on 14 Feb 2017

@author: vgong
'''
import math

# cell_points_list = []
# # cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
# cell_points_list.append([[52.380853, 4.898841], [52.378196, 4.907432], [52.377343, 4.906678], [52.380259, 4.898109]])
# cell_points_list.append([[52.379857, 4.925105], [52.379209, 4.928704], [52.378781, 4.928566], [52.379371, 4.924914]])
# cell_points_list.append([[52.379352, 4.924892], [52.377850, 4.933742], [52.377177, 4.933332], [52.378710, 4.924574]])
# cell_points_list.append([[52.375891, 4.929162], [52.374704, 4.936065], [52.374124, 4.935806], [52.375251, 4.928784]]) 


def extend_line(ext_l, y1,x1,y2,x2):
    ext_l = ext_l * 0.00001
    
    l = math.hypot(x2 - x1, y2 - y1)
    h = (x2-x1)*ext_l/l
    f = (y2-y1)*ext_l/l
    
    x3 = x2+h
    y3 = y2+f
    
#     print('y3,x3={},{}'.format(y3,x3))
    
    return [y3, x3]


    
def cell_b1_extend(coord_list, dist):
#     coord_list = [52.380853, 4.898841, 52.378196, 4.907432, 52.377343, 4.906678, 52.380259, 4.898109]
#     [y1,x1,y2,x2,y3,x3,y4,x4]
    
#   get the left-top new extended point
    new_point1 = extend_line(dist, coord_list[1][0], coord_list[1][1], coord_list[0][0], coord_list[0][1])
#   get the left-bottom new extended point
    new_point4 = extend_line(dist, coord_list[2][0], coord_list[2][1], coord_list[3][0], coord_list[3][1])

    return [new_point1, new_point4]
    

    
def cell_b2_extend(coord_list, dist):
#     coord_list = [52.380853, 4.898841, 52.378196, 4.907432, 52.377343, 4.906678, 52.380259, 4.898109]
#     [y1,x1,y2,x2,y3,x3,y4,x4]
    
#   get the right-top new extended point
    new_point2 = extend_line(dist, coord_list[0][0], coord_list[0][1], coord_list[1][0], coord_list[1][1])
#   get the right-bottom new extended point
    new_point3 = extend_line(dist, coord_list[3][0], coord_list[3][1], coord_list[2][0], coord_list[2][1])

    return [new_point2, new_point3]    


def cell_b1b2_extend(coord_list, dist):
    p1p4 = cell_b1_extend(coord_list, dist)
    p2p3 = cell_b2_extend(coord_list, dist)
    
    return [p1p4[0], p2p3[0], p2p3[1], p1p4[1]]


def cell_b1_extend_area(coord_list, dist):
    p1p4 = cell_b1_extend(coord_list, dist)
    return [p1p4[0], coord_list[0], coord_list[3], p1p4[1]]


def cell_b2_extend_area(coord_list, dist):
    p2p3 = cell_b2_extend(coord_list, dist)
    return [coord_list[1], p2p3[0], p2p3[1], coord_list[2]]


# enlarge area for gps resolution    
def cell_extend(coord_list, dist):
#     coord_list = [52.380853, 4.898841, 52.378196, 4.907432, 52.377343, 4.906678, 52.380259, 4.898109]
#     [y1,x1,y2,x2,y3,x3,y4,x4]
#     [00,11,22,33,44,55,66,77]

    new_point1 = extend_line(dist, coord_list[2][0], coord_list[2][1], coord_list[0][0], coord_list[0][1])
    new_point2 = extend_line(dist, coord_list[3][0], coord_list[3][1], coord_list[1][0], coord_list[1][1])    
    new_point3 = extend_line(dist, coord_list[0][0], coord_list[0][1], coord_list[2][0], coord_list[2][1])    
    new_point4 = extend_line(dist, coord_list[1][0], coord_list[1][1], coord_list[3][0], coord_list[3][1])
    
    return [new_point1, new_point2, new_point3, new_point4]

    
def transfer_coords(coords):
    # [[y1,x1],[y2,x2],[y3,x3],[y4,x4]] the point1 is in left-top, clockwise
    #'4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    # x1 y1, x2 y2, x3 y3, x4 y4
    
    line = '{} {},{} {},{} {},{} {},{} {}'.format(coords[0][1],coords[0][0],coords[1][1],coords[1][0],coords[2][1],coords[2][0],coords[3][1],coords[3][0],coords[0][1],coords[0][0])
    return line
