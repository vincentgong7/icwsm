'''
Created on 30 May 2017

@author: vgong
'''

import time
import math
from datetime import datetime as dt1
from math import radians, cos, sin, asin, sqrt
import scipy.stats

def transfer_coords(coords):
    # [[y1,x1],[y2,x2],[y3,x3],[y4,x4]] the point1 is in left-top, clockwise
    #'4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    # x1 y1, x2 y2, x3 y3, x4 y4
    
    line = '{} {},{} {},{} {},{} {},{} {}'.format(coords[0][1],coords[0][0],coords[1][1],coords[1][0],coords[2][1],coords[2][0],coords[3][1],coords[3][0],coords[0][1],coords[0][0])
    return line

def my_date_parse_withtimezone(date_str):
#     date_str = "2015-08-23 08:40:19+02"
    date_format = "%Y-%m-%d %H:%M:%S+02"
    t = dt1.strptime(date_str, date_format)
    return t

def my_date_parse(date_str):
#     date_str = "2015-08-23 08:40:19"
#     format = "%Y-%m-%d %H:%M:%S"
#     t = dt1.strptime(str."+02", format)
    t = my_date_parse_withtimezone(date_str+"+02")
    return t

def textdate2ts(strdate):
    date = my_date_parse(strdate)
    return round(time.mktime(date.timetuple()))

def date2ts(strdate):
    return textdate2ts(strdate)

def printlist(a_list):
    for item in a_list:
        print('{}\n'.format(item))

def mywritelines2file(data_list, file):
    with open(file, 'w') as f_w:
        for line in data_list:
            f_w.write("{0}\n".format(line))
    print("done.")


def mf_result_list_transfer(result_list):
    print_list = []
    for item in result_list:
        line = '{},{},{},{},{},{}'.format(item[0],item[1],item[2],item[3],item[4],item[5])
        print_list.append(line)
    return print_list

def mf_prob_result_list_transfer(result_list):
    print_list = []
    for item in result_list:
        line = '{},{},{},{},{}'.format(item[0],item[1],item[2],item[3],item[4])
        print_list.append(line)
        
    return print_list


def mf_prob_result_list_original_transfer(result_list):
    print_list = []
    np_line = len(result_list[0])
    for i in range (0,np_line):
        print(i)
        print(result_list[0][i])
        print(result_list[1][i])
        print(result_list[2][i])
        print(result_list[3][i])
        print(result_list[4][i])
        
        line = '{},{},{},{},{}'.format(result_list[0][i],result_list[1][i],result_list[2][i],result_list[3][i],result_list[4][i])
        print_list.append(line)
#     for item in result_list:
#         line = '{},{},{},{},{}'.format(item[0],item[1],item[2],item[3],item[4])
#         print_list.append(line)
    return print_list

def result_list_transfer(result_list):
    print_list = []
    for item in result_list:
        line = '{}'.format(item)
        print_list.append(line)
    return print_list


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
    
 
def calculate_distance(x, y, cell):
    # cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise    
#     cell = cell_points_list[cell_id]
    
    cell_x = 0.5 * (cell[0][1] + cell[2][1])
    cell_y = 0.5 * (cell[0][0] + cell[2][0])
    
    distance = coordinates_dis_calculater(x, y, cell_x, cell_y)
    
    return distance


def coordinates_dis_calculater(lon1, lat1, lon2, lat2):
    
#     o_lon1, o_lat1, o_log2, o_lat2 = lon1, lat1, lon2, lat2
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    distance = 6367 * c * 1000

#     distance = math.sqrt((lon2 - lon1)**2 + (lat2 - lat1)**2)
#     print('lon1 = {}, lat1 = {}, lon2 = {}, lat2 = {}. Distance: {}'.format(o_lon1, o_lat1, o_log2, o_lat2, distance))
    
    return distance


def my_file_reader(filepath):
    line_list = []
    with open(filepath, "r") as f:
#         next(f)
        for line in f:
            #print (line)
            line_list.append(line)
#     print(len(line_list))
    return line_list



# expts = date2ts('2016-04-26 08:20:28') 
# print(expts)



