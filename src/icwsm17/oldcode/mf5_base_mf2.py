'''
Created on 15 Feb 2017

@author: vgong
'''

# coding: utf-8

# In[2]:

# common functions
from datetime import datetime as dt1
import datetime as dt2
import time

# parse date from text based on standard format
def my_date_parse_withtimezone(str):
#     str = "2015-08-23 08:40:19+02"
    format = "%Y-%m-%d %H:%M:%S+02"
    t = dt1.strptime(str, format)
    return t

def my_date_parse(str):
#     str = "2015-08-23 08:40:19"
#     format = "%Y-%m-%d %H:%M:%S"
#     t = dt1.strptime(str."+02", format)
    t = my_date_parse_withtimezone(str+"+02")
    return t

# parse a python date fram a timestamp text
def ts2date(ts):
    t = dt1.fromtimestamp(ts)
#   if the ts requires adjustment
#     adjust_timezone = dt2.timedelta(hours = 2)
#     t = t + adjust_timezone
    return t
# print(ts2date(1.4399e+09))


# common function: write line to a file from a list
def write_to_file(data_list, file):
    with open(file, 'w') as f_w:
        for line in data_list:
            f_w.write("{0}".format(line))
    print("done.")

def mywritelines2file(data_list, file):
    with open(file, 'w') as f_w:
        for line in data_list:
            f_w.write("{0}\n".format(line))
    print("done.")

    
def printlist(a_list):
    for item in a_list:
        print('{}\n'.format(item))
    
def textdate2ts(strdate):
    date = my_date_parse(strdate)
    return round(time.mktime(date.timetuple()))


def date2ts(strdate):
    return textdate2ts(strdate)

# print(textdate2ts('2015-08-18 12:13:20'))
# print(ts2date(1439900000).strftime("%Y-%m-%dT%H:%M:%S"))


# In[4]:

# test: parse the text id from exponent

# id = round(1.4399e+09)

# print('{:d}'.format(id))


# In[5]:

# camera
# parse data from raw camera csv: cam_id, ts, dir1, dir2
# then write data to parsed data csv: cam_id, update_date, dir1, dir2


def parse_cam_raw(file):
    data_list = []
    with open(file, "r") as f_r:
        # cam_id, update_ts, count_dir1, count_dir2
        # 1.3458e+09,1.4399e+09,7,1
        for line in f_r:
            #print (line)
            strs = line.split(",")

            cam_id = round(float(strs[0]))
            update_dt = ts2date(round(float(strs[1])))

            #print("a={0},b={1}".format(a, b))
            newline = "{0},{1},{2},{3}".format(cam_id, update_dt.strftime("%Y-%m-%dT%H:%M:%S"), strs[2], strs[3])

            #print(newline)

            data_list.append(newline)
    return data_list
                
def main_parse_cam_raw():
    cam_raw_data_file = "/root/icwsm17/sail15/sensor/original/camera_data.csv"
    data_list = parse_cam_raw(cam_raw_data_file)
    print(len(data_list))
    cam_parsed_data_file = "/root/icwsm17/sail15/sensor/process_data/camera_data_parsed.csv"
    write_to_file(data_list,cam_parsed_data_file)
    
# main_parse_cam_raw()



# In[6]:

# wifi
# parse data from raw wifi csv: a_ts,b_ts,a_id,b_id,tt,update_ts
# then write data to parsed data csv: a_ts,b_ts,a_id,b_id,tt,update_ts

def parse_wifi_raw(file):
    data_list = []
    with open(file, "r") as f_r:
        # a_ts,b_ts,a_id,b_id,tt,update_ts
        # all in integer
        for line in f_r:
            #print (line)
            strs = line.split(",")

            a_ts = strs[0]
            b_ts = strs[2]
            a_id = strs[3]
            b_id = strs[4]
            tt = strs[5]
            update_ts = strs[6]
            
            #print("a={0},b={1}".format(a, b))
            newline = "{0},{1},{2},{3}\n".format(a_id, b_id, a_ts.strftime("%Y-%m-%dT%H:%M:%S"), b_ts.strftime("%Y-%m-%dT%H:%M:%S"), tt)
#           print(newline)
            data_list.append(newline)
    return data_list


def main_parse_wifi_raw():
    wifi_raw_data_file = "/root/icwsm17/sail15/sensor/original/wifi_data.csv"
    data_list = parse_wifi_raw(wifi_raw_data_file)
    print(len(data_list))
    wifi_parsed_data_file = "/root/icwsm17/sail15/sensor/process_data/wifi_data_parsed.csv"
    write_to_file(data_list,wifi_parsed_data_file)

# main_parse_wifi_raw()


# In[7]:

# Cell configuration

class Cell(object):
    # cell_name;cam_id_list;wifi_pair;area(ha)
    def __init__(self, cell_name, cam_id_list, wifi_pair, area):
        self.cell_name = cell_name
        self.cam_id_list = cam_id_list
        self.wifi_pair = wifi_pair
        self.area = area
    
    def __str__(self):
        #print("a={0},b={1}".format(a, b))
        return "cell_name={0},cameras={1},wifi_pair={2},area={3}".format(self.cell_name, self.cam_id_list, self.wifi_pair, self.area)

def init_cells():
    cell_list = []
    cell_top = Cell("cell_top",[7.552e+08],[26,1308],1.38)
    cell_list.append(cell_top)
    cell_mid = Cell("cell_mid",[1.8679e+09],[34,1329],1.39)
    cell_list.append(cell_mid)
    cell_left = Cell("cell_left",[8.08e+08],[1298,19],1.50)
    cell_list.append(cell_left)
    cell_right = Cell("cell_left",[6.7575e+08,4.7924e+08],[40,21],1.11)
    cell_list.append(cell_right)
    return cell_list

# cells = init_cells()
# for c in cells:
#     print(c)

# print(cells[0].cell_name)


# In[8]:

class Cam(object):
# cam_id, update_ts, count_dir1, count_dir2
# 1345800000,2015-08-18 12:13:20,7,1
    def __init__(self, cam_id, cam_date, cam_dir1, cam_dir2):
        self.cam_id = cam_id
        self.date = my_date_parse(cam_date)
        self.ts = textdate2ts(cam_date)
        self.dir1 = int(cam_dir1)
        self.dir2 = int(cam_dir2)
    
    def __str__(self):
        #print("a={0},b={1}".format(a, b))
        return "cam_id={0},date={1},ts={2},dir1={3},dir2={4}".format(self.cam_id, self.date, self.ts, self.dir1, self.dir2)

def read_cam_parse(file):
    cam_list = []
    with open(file, "r") as f_r:
        # cam_id, update_ts, count_dir1, count_dir2
        # 1.3458e+09,1.4399e+09,7,1
        for line in f_r:
#             print (line)
            strs = line.split(",")
            if(len(strs)<4):
                continue
#             print(len(strs))
            cam = Cam(strs[0], strs[1], strs[2], strs[3])
            cam_list.append(cam)
            
    return cam_list


def test_cam_pares_item(file):
    cam_list = read_cam_parse(file)
    print(len(cam_list))
    print(cam_list[0])

# test_cam_pares_item("/root/icwsm17/sail15/sensor/process_data/camera_data_parsed.csv")


# In[9]:

# test: datetime comparion
# import math

# t1 = my_date_parse("2015-08-23 08:40:19")
# t2 = my_date_parse("2015-08-23 10:40:19")

# t3 = my_date_parse("2015-08-23 09:40:19")

# t4 = t3 + dt2.timedelta(minutes = 30)

# print(t1 < t4 < t2)

# print((t2 - t1).seconds/60)


# math.ceil((t2 - t1).seconds/(60*100))


# print(time.mktime(t1.timetuple()))

# print(textdate2ts("2015-08-23 08:40:19"))



# In[10]:

# camera, calculate the #camera_total for a given cell

# this should be rephrased
def camera_total_4_cam(startdate, enddate, interval, cam, cam_data_list):
    # text to date and to ts
    start_ts = textdate2ts(startdate)
    end_ts = textdate2ts(enddate)
    
    # calculate steps
    steps = math.ceil((end_ts - start_ts)/(60*interval))
    
    # query
    cam_total_list = []
    for s in range(steps):
        start_step_ts = start_ts + s*interval*60
        end_step_ts = start_step_ts + interval*60
        
        total_list = [c.dir1+c.dir2 for c in cam_data_list if c.cam_id == cam and c.ts >= start_step_ts and c.ts < end_step_ts] 
        # add all rather than len
        total = len(total_list)
        print(total_list)
        print(total)
        cam_total_list.append(total)

    
    return cam_total_list


def test_camera_total_4_cam(startdate, enddate, interval, cam, cam_data_list):
    result = camera_total_4_cam(startdate, enddate, interval, cam, cam_data_list)
#     print(len(result))
#     print(result)

def caculate_total_4_camlist(startdate, enddate, interval, cam_list, cam_data_list):
    camlist_total_list = []
    values = []
    for cam in cam_list:
        values = values + camera_total_4_cam(startdate, enddate, interval, cam, cam_data_list)
    camlist_total_list = values / len(cam_list)
    return camlist_total_list

def camera_total_4_cell(startdate, enddate, interval, cell, cam_data_list):
    cam_id_list = cell.cam_id_list
    cam_total_list = caculate_total_4_camlist(startdate, enddate, interval, cam_id_list, cam_data_list)
    return cam_total_list


# AMS Sail 2015: Aug 19th - 24th (18h)
# startdate = "2015-08-22 12:13:20"
# enddate = "2015-08-22 13:13:20"
# interval = 10
# cam_data_list = read_cam_parse("/root/icwsm17/sail15/sensor/process_data/camera_data_parsed.csv")

# test_camera_total_4_cam(startdate,enddate,5,"6.7575e+08",cam_data_list)


# cells = init_cells()
# camera_total=[]
# for c in cells:
#     print(c)
#     t = camera_total_4_cell(startdate, enddate, interval, c, cam_data_list)
#     camera_total.append(t)

# print(len(camera_total))

    


# In[11]:

import scipy.stats
# scipy.stats.norm(100, 12).pdf(98)


# for i in range(0,5):
#     print(i)


# In[12]:

# db tool


#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2
    

def querydb(sql):
    try:
        connect_str = "dbname='icwsm17' user='postgres' host='localhost' password='postgres' port='5432'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
#         cursor.execute("SELECT id, a_ts, b_ts, a_id, b_id, tt, update_ts FROM public.wifi_data limit 10;")
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('Affected: {0}. Returned len(rows): {1}'.format(cursor.rowcount, len(rows)))
#         print(len(rows))
        return rows
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

# querydb("SELECT id, a_ts, b_ts, a_id, b_id, tt, update_ts FROM public.wifi_data limit 10;")
# querydb("select ST_Within(ST_MakePoint(5.072972,52.429900),ST_GeomFromText('POLYGON((4.728759 52.278174,5.079162 52.278174,5.079162 52.431064,4.728759 52.431064,4.728759 52.278174))'))")


# In[ ]:




# In[12]:

# draw histogram of wifi speed of cells

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


wifi_speed_cell_file = []
wifi_speed_cell_file.append('/root/icwsm17/sail15/sensor/data/wifi_speed_cell1.csv.txt')
wifi_speed_cell_file.append('/root/icwsm17/sail15/sensor/data/wifi_speed_cell2.csv.txt')
wifi_speed_cell_file.append('/root/icwsm17/sail15/sensor/data/wifi_speed_cell3.csv.txt')
wifi_speed_cell_file.append('/root/icwsm17/sail15/sensor/data/wifi_speed_cell4.csv.txt')


def read_speed(file):
    data_list = []
    with open(file, "r") as f_r:
        # speed
        # all in double
        next(f_r) # skip the header
        for line in f_r:
            line = line.replace('"','')
#             print (line)
            data_list.append(line)
    
    
    return data_list


# data_list = read_speed('/root/icwsm17/sail15/sensor/data/wifi_speed_cell4.csv.txt')


def wifi_speed_cell(filepath, cell_number):
    data_list = read_speed(filepath)
    data = np.array(data_list).astype(np.float)
    mean = np.mean(data)
    median = np.median(data)
    sd = np.std(data)
    title = 'Histogram of Speed of Paired Wifi Device from Cell No.{0}\n mean={1}, median = {2}, sd={3}\n'.format(cell_number,mean,median,sd)
    draw_hist(data,'Speed','Probability',title)
    
    
def draw_hist(data, xlabel, ylabel, title):    
    num_bins = 50
    # the histogram of the data
    n, bins, patches = plt.hist(data, bins='auto', normed=1, facecolor='white', alpha=0.5)
    # add a 'best fit' line
    # y = mlab.normpdf(bins, mu, sigma)
    # plt.plot(bins, y, 'r--')
#     plt.xlabel('Speed')
#     plt.ylabel('Probability')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.title(title)

    # Tweak spacing to prevent clipping of ylabel
#     plt.subplots_adjust(left=0.15)
    plt.show()

def cell_speed_cdf(cell_id, np_bins, speed):
    result_list = cell_speed_cdf_mainpart(cell_id, np_bins)
    bin_edges = result_list[0]
    cdf = result_list[1]
    
    min_s = bin_edges[0]
    max_s = bin_edges[np_bins-1]
    
#     print(min_s)
#     print(max_s)
    
    bin_size = (max_s - min_s) / np_bins
    ii = round(speed/bin_size)
    
    cdf_value = 0.00
    if ii==0:
        cdf_value = 0
    elif 1<=ii<np_bins:
        cdf_value = cdf[ii]
    elif ii>=np_bins:
        cdf_value = 1
    
    print('speed = {}, ii = {}, value = {:.2f}'.format(speed, ii, cdf_value))
    return cdf_value
    
    
def cell_speed_cdf_mainpart(cell_id, np_bins):
#     num_bins = 4 * 24
    
    data_list = read_speed(wifi_speed_cell_file[cell_id])
    data = np.array(data_list).astype(np.float)
    data_size=len(data)
    
    # the histogram of the data
    counts, bin_edges = np.histogram(data, bins=np_bins, density = False)
    counts=counts.astype(float)/data_size
#     print(sum(counts))
#     print(len(data))
#     print(counts)
    
    # cdf
    cdf = np.cumsum(counts)
    
    # And finally plot the cdf
#     plt.plot(bin_edges[1:], cdf)
#     plt.show()
    
    return([bin_edges, cdf])
    

def cell_speed_query_outlier(cell_id, np_bins, outlier_scope):
    result_list = cell_speed_cdf_mainpart(cell_id, np_bins)
    bin_edges = result_list[0]
    cdf = result_list[1]
    
    i=0
    for val in cdf:
        if val>= outlier_scope:
#             print('The outlier: {}, {}'.format(i,val))
            print('The probability of the users\' speed larger than {} is {}'.format(bin_edges[i-1],cdf[i-1]))
            break;
        i=i+1
    
    return bin_edges[i-1]
    
def wifi_speed_allcell():
    wifi_speed_cell('/root/icwsm17/sail15/sensor/data/wifi_speed_cell1.csv.txt',1)
    wifi_speed_cell('/root/icwsm17/sail15/sensor/data/wifi_speed_cell2.csv.txt',2)
    wifi_speed_cell('/root/icwsm17/sail15/sensor/data/wifi_speed_cell3.csv.txt',3)
    wifi_speed_cell('/root/icwsm17/sail15/sensor/data/wifi_speed_cell4.csv.txt',4)


# for faster running, run this code to generate the list first
def batch_cell_speed_cdf(np_bins):
    cdf_list = []
    for cell_id in range(0,4):
        result_list = cell_speed_cdf_mainpart(cell_id, np_bins)
        bin_edges = result_list[0]
        cdf = result_list[1]
    
        min_s = bin_edges[0]
        max_s = bin_edges[np_bins-1]

        bin_size = (max_s - min_s) / np_bins    
        
        cdf_list.append([bin_size, cdf, np_bins])
    return cdf_list

# -----start for faster running, run this code to generate the list first------
np_bins_speed_cdf = 200
speed_cdf_list = batch_cell_speed_cdf(np_bins_speed_cdf)
# -----end for faster running, run this code to generate the list first-----


    
    
# wifi_speed_cell('/root/icwsm17/sail15/sensor/data/wifi_speed_cell4.csv.txt',4)
#wifi_speed_allcell()


# cell_speed_query_outlier(0,200,0.68268949)
# cell_speed_cdf(0,200,5)


# In[14]:

# query and export the wifi flow per hour
# start_ts = 1439942400, Wed, 19 Aug 2015 00:00:00 GMT
# end_ts = 1440374400, Mon, 24 Aug 2015 00:00:00 GMT


def calculate_cell123_wifi_flow_perhour():
    start_ts = 1439942400
    end_ts = 1440374400
    hours = round((end_ts - start_ts)/3600)


    result_list=['ts,cell_1,cell_2,cell_3'] 
    for i in range(1,hours):
        sql = "SELECT cell_id, count(id) FROM public.v_cell_wifi_flow_direction where flow_direction = '->' and b_ts > 1439942400 + 3600*{} and b_ts < 1439942400 + 3600*{} group by cell_id order by cell_id;".format(i-1,i)
    #     print(sql)
        rows = querydb(sql)
    #     print(len(rows))
        if(len(rows)<3):
            continue
    #     print(rows[0][0])
    #     print(rows[0][1])
        ts = 1439942400 + 3600*i
        line = '{},{},{},{}'.format(ts,rows[0][1],rows[1][1],rows[2][1])
        result_list.append(line)

    mywritelines2file(result_list, '/root/icwsm17/sail15/sensor/data/cell_123_wifi_flow_perhours.txt')
    print(len(result_list))

    print('done')
    return result_list


# calculate_cell123_wifi_flow_perhour()


# In[15]:

# start_ts = 1439942400
# end_ts = 1440374400
# hours = round((end_ts - start_ts)/3600)

# print(hours)


# In[16]:

import math

# query, calculate and export the cell flow for bondaries without camera

# query the wifi_flow_per_hour

def calculate_cell123_flow_perhour():

    # penetration: Ruijterkade, Sumatrakade, Javakade
    penetration = []
    penetration.append(['Ruijterkade', 'Sumatrakade', 'Javakade'])
    penetration.append([58.20,152.31,153.75,317.29,92.39])
    penetration.append([12.37,12.55,13.14,17.75,8.58])
    penetration.append([31.94,34.50,31.68,40.90])

    print(len(penetration[1]))
    cell_1_rate = penetration[1]
    cell_2_rate = penetration[2]
    cell_3_rate = penetration[3]    
    
# start_ts = 1439942400, Wed, 19 Aug 2015 00:00:00 GMT
# end_ts = 1440374400, Mon, 24 Aug 2015 00:00:00 GMT
    start_ts = 1439942400
    end_ts = 1440374400
    hours = round((end_ts - start_ts)/3600)


    result_list=['ts,cell_1,cell_2,cell_3'] 
    flow=['ts,cell_1,cell_2,cell_3']
    
    for i in range(1,hours):
        sql = "SELECT cell_id, count(id) FROM public.v_cell_wifi_flow_direction where flow_direction = '->' and b_ts > 1439942400 + 3600*{} and b_ts < 1439942400 + 3600*{} group by cell_id order by cell_id;".format(i-1,i)
    #     print(sql)
        rows = querydb(sql)
    #     print(len(rows))
        if(len(rows)<3):
            continue
    #     print(rows[0][0])
    #     print(rows[0][1])
        ts = 1439942400 + 3600*i
        
        # check which day the ts belong to
        day = math.floor(i/24)

        flow_cell_1, flow_cell_2, flow_cell_3 = 0,0,0
        if(len(cell_1_rate) >= day+1):
            flow_cell_1 = cell_1_rate[day] * rows[0][1]
        if(len(cell_2_rate) >= day+1):
            flow_cell_2 = cell_2_rate[day] * rows[1][1]
        if(len(cell_3_rate) >= day+1):
            flow_cell_3 = cell_3_rate[day] * rows[2][1]
        
        flow.append([flow_cell_1,flow_cell_2,flow_cell_3])
        # multiply to the certain penetration rate of that cell of that day. 
        
        line = '{},{},{},{}'.format(ts,flow_cell_1,flow_cell_2,flow_cell_3)
        result_list.append(line)
    
    mywritelines2file(result_list, '/root/icwsm17/sail15/sensor/data/cell_123_flow_perhours.txt')
    print(len(result_list))
    
    print('done')
    return flow

# cell_flow = calculate_cell123_flow_perhour()
# print(len(cell_flow))


# In[17]:

# calculate the extended coordinates and area

import math


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
    
    
    
    
cell_points_list = []
# cell_points_list.append([y1,x1],[y2,x2],[y3,x3],[y4,x4]), the left-top is point1, clockwise
cell_points_list.append([[52.380853, 4.898841], [52.378196, 4.907432], [52.377343, 4.906678], [52.380259, 4.898109]])
cell_points_list.append([[52.379857, 4.925105], [52.379209, 4.928704], [52.378781, 4.928566], [52.379371, 4.924914]])
cell_points_list.append([[52.379352, 4.924892], [52.377850, 4.933742], [52.377177, 4.933332], [52.378710, 4.924574]])
cell_points_list.append([[52.375891, 4.929162], [52.374704, 4.936065], [52.374124, 4.935806], [52.375251, 4.928784]])    
    
# extend_line(200, 52.378196, 4.907432, 52.380853, 4.898841)
# extend_line(200, 52.380853, 4.898841, 52.378196, 4.907432)

# print(cell_extend(cell_points_list[0], 100))
# print(cell_b1_extend(cell_points_list[3], 100))

# print(cell_b2_extend(cell_points_list[3], 100))

# print(cell_b1b2_extend(cell_points_list[3], 300))
# print(cell_b1_extend_area(cell_points_list[2], 300))
# print(cell_b2_extend_area(cell_points_list[2], 300))


# In[18]:

# common for membership function


cell_points_list = []
# cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
cell_points_list.append([[52.380853, 4.898841], [52.378196, 4.907432], [52.377343, 4.906678], [52.380259, 4.898109]])
cell_points_list.append([[52.379857, 4.925105], [52.379209, 4.928704], [52.378781, 4.928566], [52.379371, 4.924914]])
cell_points_list.append([[52.379352, 4.924892], [52.377850, 4.933742], [52.377177, 4.933332], [52.378710, 4.924574]])
cell_points_list.append([[52.375891, 4.929162], [52.374704, 4.936065], [52.374124, 4.935806], [52.375251, 4.928784]]) 



def transfer_coords(coords):
    # [[y1,x1],[y2,x2],[y3,x3],[y4,x4]] the point1 is in left-top, clockwise
    #'4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    # x1 y1, x2 y2, x3 y3, x4 y4
    
    line = '{} {},{} {},{} {},{} {},{} {}'.format(coords[0][1],coords[0][0],coords[1][1],coords[1][0],coords[2][1],coords[2][0],coords[3][1],coords[3][0],coords[0][1],coords[0][0])
    return line


# In[19]:

# mf1

#querydb("select ST_Within(ST_MakePoint(5.072972,52.429900),ST_GeomFromText('POLYGON((4.728759 52.278174,5.079162 52.278174,5.079162 52.431064,4.728759 52.431064,4.728759 52.278174))'))")




def get_twitter_posts(area_str):
    
#     area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    sql_fields = 'id, userid, ts, latitude, longitude, post_content, gender, age, uclass'
    sql_table_name = 'public.twitter_geo_is_data_user'
    
    sql = "SELECT {} FROM {} as t1 where ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))'));".format(sql_fields,sql_table_name,area_str)
    rows = querydb(sql)
    return rows

def get_inst_posts(area_str):
    
#     area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    sql_fields = 'id, userid, ts, latitude, longitude, post_content, gender, age, uclass'
    sql_table_name = 'public.inst_geo_is_data_user'
    
    sql = "SELECT {} FROM {} as t1 where ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))'));".format(sql_fields,sql_table_name,area_str)
    rows = querydb(sql)
    return rows

# area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
# get_twitter_posts(area_str)


#mf1


#given a cell, [start_ts, end_ts], return all posts in the cell



def membership_fun1_twitter(cell_coord_list, start_ts, end_ts):
    
    #cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
    #area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    area_str = transfer_coords(cell_coord_list)
    sql_fields = 'count(distinct userid) as num'
    sql_table_name = 'public.twitter_geo_is_data_user'
    sql = "SELECT {} FROM {} as t1 where {} <= t1.ts and t1.ts <={} and ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))'));".format(sql_fields,sql_table_name,start_ts,end_ts,area_str)
    rows = querydb(sql)
    return rows[0]


def membership_fun1_inst(cell_coord_list, start_ts, end_ts):
    
    #cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
    #area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    area_str = transfer_coords(cell_coord_list)
    sql_fields = 'count(distinct userid) as num'
    sql_table_name = 'public.inst_geo_is_data_user'
    sql = "SELECT {} FROM {} as t1 where {} <= t1.ts and t1.ts <={} and ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))'));".format(sql_fields,sql_table_name,start_ts,end_ts,area_str)
    rows = querydb(sql)
    return rows[0]



# date2ts('2015-08-18 12:13:20')
# # np_users = membership_fun1_twitter(cell_points_list[1],1439856000,1440460800)
# np_users = membership_fun1_twitter(cell_points_list[0],date2ts('2015-08-20 3:13:20'),date2ts('2015-08-20 23:13:20'))
# print(np_users[0])

# np_users = membership_fun1_inst(cell_points_list[0],date2ts('2015-08-19 3:13:20'),date2ts('2015-08-20 23:13:20'))
# print(np_users[0])


# In[20]:

# mf2: enlarge the monitoring area concerning GPS resolution

#     cell_id = 2 # 0-3
#     ext_length = 300
def membership_fun2_twitter(cell_id, ext_length, start_ts, end_ts):
    np_users = membership_fun1_twitter(cell_extend(cell_points_list[cell_id], ext_length), start_ts, end_ts)
    print(np_users[0])
    return np_users[0]

    
def membership_fun2_inst(cell_id, ext_length, start_ts, end_ts):
    np_users = membership_fun1_inst(cell_extend(cell_points_list[cell_id], ext_length), start_ts, end_ts)
    print(np_users[0])
    return np_users[0]  
    
    
# membership_fun2_twitter(2, 113, date2ts('2015-08-19 3:13:20'),date2ts('2015-08-20 23:13:20'))
# membership_fun2_inst(2, 113, date2ts('2015-08-19 3:13:20'),date2ts('2015-08-20 23:13:20'))


# In[21]:

import math
import scipy.stats

# mf2.5-1, the users who posts before stat_ts: the normal distribution with parameter SCALE

cell_half_length = [328,127,309,243] # the half length of each cells


# given: cell, boundary (left or right), platform (twitter or inst), start_ts, end_ts, prior_ts, max_extend_length, bin_length, norm_dis_scale
# output: list[[ts, dist_to_boundary, np_user],...]
def mf2p5_explore_users_before(cell_id, boundary, platform, start_ts, end_ts, prior_ts, max_extend_length, bin_length, norm_dis_scale):
    user_list = [] # store the np_user w.r.t. the distance to the boundary of the cell
    result = 0
    cell = cell_points_list[cell_id]
    
    times = math.floor(max_extend_length/bin_length)+1
    for i in range(0,times):
        print('the {} times.'.format(i))
        
        if('left' == boundary):
            cell = cell_b1_extend_area(cell, bin_length)
        else:
            cell = cell_b2_extend_area(cell, bin_length)
        
        np_user = (0,)
        if('twitter' == platform):
            np_user = membership_fun1_twitter(cell,start_ts-prior_ts,start_ts)[0]
        else:
            np_user = membership_fun1_inst(cell,start_ts-prior_ts,start_ts)[0]
        
        # store the result
        print("number of user at this distance: {}".format(np_user))
        if(np_user >0):
            user_list.append([i*bin_length, np_user])
    
    print('len(user_list) = {}'.format(len(user_list)))
    
    norm_p = scipy.stats.norm(0, norm_dis_scale)
    r =  cell_half_length[cell_id]
    
    for item in user_list:
        dist = item[0] + r
        p = norm_p.cdf(dist+bin_length)-norm_p.cdf(dist) # the probability of the bin in that distance
        result = result + item[1] * p
    
    return result
    
  
# mf2.5-2, the users who posts after stat_ts: the normal distribution with parameter SCALE

cell_half_length = [328,127,309,243] # the half length of each cells


# given: cell, boundary (left or right), platform (twitter or inst), start_ts, end_ts, extra_ts, max_extend_length, bin_length, norm_dis_scale
# output: list[[ts, dist_to_boundary, np_user],...]
def mf2p5_explore_users_after(cell_id, boundary, platform, start_ts, end_ts, extra_ts, max_extend_length, bin_length, norm_dis_scale):
    
    user_list = [] # store the np_user w.r.t. the distance to the boundary of the cell
    result = 0
    cell = cell_points_list[cell_id]
    
    times = math.floor(max_extend_length/bin_length)+1
    for i in range(0,times):
        print('the {} times.'.format(i))
        
        if('left' == boundary):
            cell = cell_b1_extend_area(cell, bin_length)
        else:
            cell = cell_b2_extend_area(cell, bin_length)
        
        np_user = (0,)
        if('twitter' == platform):
            np_user = membership_fun1_twitter(cell,end_ts,end_ts + extra_ts)[0]
        else:
            np_user = membership_fun1_inst(cell,end_ts,end_ts + extra_ts)[0]
        
        # store the result
        print("number of user at this distance: {}".format(np_user))
        if(np_user >0):
            user_list.append([i*bin_length, np_user])
    
    print('len(user_list) = {}'.format(len(user_list)))
    
    norm_p = scipy.stats.norm(0, norm_dis_scale)
    r =  cell_half_length[cell_id]
    
    for item in user_list:
        dist = item[0] + r
        p = norm_p.cdf(dist+bin_length)-norm_p.cdf(dist) # the probability of the bin in that distance
        result = result + item[1] * p
        print(('dist: {}, p = {}, result = {}').format(dist, p, result))
    
    return result


# cell_id = 0
# start_ts = date2ts('2015-08-20 3:13:20')
# end_ts = date2ts('2015-08-20 23:13:20')
# prior_ts = 24* 60 * 60 #  seconds
# extra_ts = 30 * 60 # 30 minutes
# normal_dis_scale = 1000

# num = mf2p5_explore_users_before(cell_id, 'right', 'inst', start_ts, end_ts, prior_ts, 500, 100, normal_dis_scale)        
# print(num)

# num = mf2p5_explore_users_after(cell_id, 'right', 'inst', start_ts, end_ts, extra_ts, 500, 100, normal_dis_scale)        
# print(num) 

# cell = cell_b2_extend_area(cell_points_list[cell_id], 512)
# np_users = membership_fun1_inst(cell,start_ts - prior_ts, start_ts)
# np_users = membership_fun1_inst(cell, end_ts, end_ts + extra_ts)
# print(np_users[0])


# In[10]:

# import scipy.stats
# norm_p = scipy.stats.norm(4000/3)
# prob = norm_p.cdf(4000)
# print(prob)


# In[24]:

# new version of the membership function
from math import radians, cos, sin, asin, sqrt
import scipy.stats

def mf2p5v2_mf_np_users(platform, timeing, cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, norm_dis_scale):
    
    cell = cell_points_list[cell_id]
    area = cell_b1b2_extend(cell, max_length)
    
    if timeing == 'before':
        rows = mf2p5v2_crawl_user(platform, area, start_ts - prior_ts, start_ts, 'order by ts desc')
    else: # timeing == 'after'
        rows = mf2p5v2_crawl_user(platform, area, end_ts, end_ts + prior_ts, 'order by ts')
    
#     print('number of posts (rows) got: {}'.format(len(rows)))
    
    norm_p = scipy.stats.norm(0, norm_dis_scale)
    r =  cell_half_length[cell_id]
    
    result = 0
    for row in rows:
#         [(634399970880323584, 914877410, 1440094914, 52.378458, 4.906394),
#          (634399970880323584, 914877410, 1440094914, 52.378458, 4.906394)]

#         print(row)
        
        dist = calculate_distance(row[4],row[3], cell_id) # par: x, y, cell_id
        dist = dist - r
        
#         print(dist)
        prob = norm_p.cdf(dist)
#         print('prob: {}'.format(prob))
        result = result + prob
#     print(result)
    return result




# for the mf3_v2
def mf3v2_mf_np_users(platform, timeing, cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length):
    
    cell = cell_points_list[cell_id]
    area = cell_b1b2_extend(cell, max_length)
    np_bins_speed_cdf = 200
    
    delta_ts = prior_ts
    
    if timeing == 'before':
        rows = mf2p5v2_crawl_user(platform, area, start_ts - prior_ts, start_ts, 'order by ts desc')
        delta_ts = prior_ts
    else: # timeing == 'after'
        rows = mf2p5v2_crawl_user(platform, area, end_ts, end_ts + prior_ts, 'order by ts')
        delta_ts = extra_ts
    
#     print('number of posts (rows) got: {}'.format(len(rows)))
    
    r =  cell_half_length[cell_id]
    
    result = 0
    for row in rows:
#         [(634399970880323584, 914877410, 1440094914, 52.378458, 4.906394),
#          (634399970880323584, 914877410, 1440094914, 52.378458, 4.906394)]

#         print(row)

        dist = calculate_distance(row[4],row[3], cell_id) # par: x, y, cell_id
        dist = dist - r

        delt_speed = dist/delta_ts
        p = 1 - cell_speed_cdf(cell_id, np_bins_speed_cdf, delt_speed)
        print('The probability is: {:.2f}'.format(p))
        result = result + p
        
        print('prob: {}, total: {}'.format(p, result))
    return result




# for the mf3_v2, dedicated for left, right and radiation direction crawl
def mf3v2_mf_np_users_direction(platform, timeing, direction, cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length):
    
    cell = cell_points_list[cell_id]
    
    if direction == 'left':
        area = cell_b1_extend_area(cell, max_length)
    elif direction == 'right':
        area = cell_b2_extend_area(cell, max_length)
    elif direction == 'bidirection':
        area = cell_b1b2_extend(cell, max_length)
    elif direction == 'radiation':
        area = cell_extend(cell, max_length)
    else:
        area = cell_extend(cell, max_length)
    
    np_bins_speed_cdf = 200
    
    delta_ts = prior_ts
    
    if timeing == 'before':
        rows = mf2p5v2_crawl_user(platform, area, start_ts - prior_ts, start_ts, 'order by ts desc')
        delta_ts = prior_ts
    else: # timeing == 'after'
        rows = mf2p5v2_crawl_user(platform, area, end_ts, end_ts + prior_ts, 'order by ts')
        delta_ts = extra_ts
    
#     print('number of posts (rows) got: {}'.format(len(rows)))
    
    r =  cell_half_length[cell_id]
    
    result = 0
    for row in rows:
#         [(634399970880323584, 914877410, 1440094914, 52.378458, 4.906394),
#          (634399970880323584, 914877410, 1440094914, 52.378458, 4.906394)]

#         print(row)

        dist = calculate_distance(row[4],row[3], cell_id) # par: x, y, cell_id
        dist = dist - r

        delt_speed = dist/delta_ts
        
#  start calculate the probability
        bin_size = speed_cdf_list[cell_id][0]
        mf4_cdf = speed_cdf_list[cell_id][1]
        np_bins = speed_cdf_list[cell_id][2]
        
        ii = round(delt_speed/bin_size)
        cdf_value = 0.00
        if ii==0:
            cdf_value = 0
        elif 1<=ii<np_bins:
            cdf_value = mf4_cdf[ii]
        elif ii>=np_bins:
            cdf_value = 1
        print('speed = {}, ii = {}, value = {:.2f}'.format(delt_speed, ii, cdf_value))        
                
# end of probability calculation        
        
        
#         p = 1 - cell_speed_cdf(cell_id, np_bins_speed_cdf, delt_speed)
        p = 1 - cdf_value
        
#         print('The probability is: {:.2f}'.format(p))
        result = result + p
        
        print('prob: {}, total: {}'.format(p, result))
    return result






#  this one is only used to calculate np_user, and export demographic data
def mf2p5v2_crawl_user(platform, cell_coord_list, start_ts, end_ts, orderby_c):
    
#     cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
#     area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    area_str = transfer_coords(cell_coord_list)   
    
    sql_fields = 'distinct userid, id, ts, latitude, longitude, gender, age, uclass '
    sql_table_name = 'public.{}_geo_is_data_user'.format(platform)
    sql = "SELECT {} FROM {} as t1 where {} <= t1.ts and t1.ts <={} and ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))')) {};".format(sql_fields,sql_table_name,start_ts,end_ts,area_str, orderby_c)
    
#     print(sql)
    
    rows = querydb(sql)
    return rows


# this is for content or topic
# it crawl all the posts during [s,e] with prob
def mf2p5v2_crawl_user(platform, cell_coord_list, start_ts, end_ts, orderby_c):
    
#     cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
#     area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    area_str = transfer_coords(cell_coord_list)   
    
    sql_fields = 'userid, id, ts, latitude, longitude, post_content'
    sql_table_name = 'public.{}_geo_is_data_user'.format(platform)
    sql = "SELECT {} FROM {} as t1 where {} <= t1.ts and t1.ts <={} and ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))')) {};".format(sql_fields,sql_table_name,start_ts,end_ts,area_str, orderby_c)
    
#     print(sql)
    
    rows = querydb(sql)
    return rows




# this is just for future use
def mf2p5v2_crawl_general(cell_coord_list, start_ts, end_ts, select_c, from_c, where_c, groupby_c, orderby_c):
    
#     cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
#     area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
    area_str = transfer_coords(cell_coord_list)   
    
#     select_c = 'id, userid, ts, latitude, longitude'
#     from_c = 'public.{}_geo_is_data_user'.format(platform)

    if where_c:
        where_c = '({}) and '.format(where_c)
    
    if groupby_c:
        groupby_c = ' group by {} '.format(groupby_c)
    
    if orderby_c:
        orderby_c = ' order by {} '.format(orderby_c)
    
    sql = "SELECT {} FROM {} as t1 where {} {} <= t1.ts and t1.ts <={} and ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))')) {} {};".format(select_c,from_c,start_ts,where_c,end_ts,area_str,groupby_c,orderby_c)
    
    print(sql)
    
    rows = querydb(sql)
    return rows



# select_clause, where_clause, orderby_clause

def calculate_distance(x, y, cell_id):
    # cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise    
    cell = cell_points_list[cell_id]
    
    cell_x = 0.5 * (cell[0][1] + cell[2][1])
    cell_y = 0.5 * (cell[0][0] + cell[2][0])
    
    distance = coordinates_dis_calculater(x, y, cell_x, cell_y)
    
    return distance


def coordinates_dis_calculater(lon1, lat1, lon2, lat2):
    
    o_lon1, o_lat1, o_log2, o_lat2 = lon1, lat1, lon2, lat2
    
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

# 4.91201019287109,52.3762893676758,4.9027595,52.379098
# coordinates_dis_calculater(4.91201019287109,52.3762893676758,4.9027595,52.379098)



#Your statements here

# start_ts = date2ts('2015-08-20 20:13:20')
# end_ts = date2ts('2015-08-20 23:13:20')
# mf2p5v2_mf_np_users('inst', 'after', 0, start_ts, end_ts, 1800, 1800, 700, 2*30*60/3)
# mf3v2_mf_np_users('inst', 'after', 0, start_ts, end_ts, 1800, 1800, 700)
# platform, timeing, cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, norm_dis_scale






# In[ ]:

# import math
import scipy.stats

# mf3-1, the users who posts before stat_ts: the probability based on speed distribution


cell_half_length = [328,127,309,243] # the half length of each cells
np_bins_speed_cdf = 100

# given: cell, boundary (left or right), platform (twitter or inst), start_ts, end_ts, prior_ts, max_extend_length, bin_length, norm_dis_scale
# output: list[[ts, dist_to_boundary, np_user],...]
def mf3_explore_users_before(cell_id, boundary, platform, start_ts, end_ts, prior_ts, max_extend_length, bin_length):
    
    user_list = [] # store the np_user w.r.t. the distance to the boundary of the cell
    result = 0
    cell = cell_points_list[cell_id]
    
    times = math.floor(max_extend_length/bin_length)+1
    for i in range(0,times):
        print('the {} times.'.format(i))
        
        if('left' == boundary):
            cell = cell_b1_extend_area(cell, bin_length)
        else:
            cell = cell_b2_extend_area(cell, bin_length)
        
        np_user = (0,)
        if('twitter' == platform):
            np_user = membership_fun1_twitter(cell,start_ts-prior_ts,start_ts)[0]
        else:
            np_user = membership_fun1_inst(cell,start_ts-prior_ts,start_ts)[0]
        
        # store the result
        print("number of user at this distance: {}".format(np_user))
        if(np_user >0):
            user_list.append([i*bin_length, np_user])
    
    print('len(user_list) = {}'.format(len(user_list)))
    
    
    for item in user_list:
        dist = item[0]
#     todo: modify
#         p = norm_p.cdf(dist+bin_length)-norm_p.cdf(dist) # the probability of the bin in that distance
#         result = result + item[1] * p
        
        delt_speed = dist/prior_ts
        p = 1 - cell_speed_cdf(cell_id, np_bins_speed_cdf, delt_speed)
        print('The probability is: {:.2f}, users counted: {:.2f}'.format(p, p*item[1]))
        result = result + item[1] * p
        
    return result
    
  
# mf3-2, the users who posts after stat_ts: the probability based on speed distribution. 

cell_half_length = [328,127,309,243] # the half length of each cells


# given: cell, boundary (left or right), platform (twitter or inst), start_ts, end_ts, extra_ts, max_extend_length, bin_length, norm_dis_scale
# output: list[[ts, dist_to_boundary, np_user],...]
def mf3_explore_users_after(cell_id, boundary, platform, start_ts, end_ts, extra_ts, max_extend_length, bin_length):
    
    user_list = [] # store the np_user w.r.t. the distance to the boundary of the cell
    result = 0
    cell = cell_points_list[cell_id]
    
    times = math.floor(max_extend_length/bin_length)+1
    for i in range(0,times):
        print('the {} times.'.format(i))
        
        if('left' == boundary):
            cell = cell_b1_extend_area(cell, bin_length)
        else:
            cell = cell_b2_extend_area(cell, bin_length)
        
        np_user = (0,)
        if('twitter' == platform):
            np_user = membership_fun1_twitter(cell,end_ts,end_ts + extra_ts)[0]
        else:
            np_user = membership_fun1_inst(cell,end_ts,end_ts + extra_ts)[0]
        
        # store the result
        print("number of user at this distance: {}".format(np_user))
        if(np_user >0):
            user_list.append([i*bin_length, np_user])
    
    print('len(user_list) = {}'.format(len(user_list)))
    
    
    for item in user_list:
        dist = item[0]
        #     todo: modify
#         p = norm_p.cdf(dist+bin_length)-norm_p.cdf(dist) # the probability of the bin in that distance
#         print('The probability is: {:.2f}, users counted: {:.2f}'.format(p, p*item[1]))
#         result = result + item[1] * p
#         print(('dist: {}, p = {}, result = {}').format(dist, p, result))
        
        
        delt_speed = dist/extra_ts
        p = 1 - cell_speed_cdf(cell_id, np_bins_speed_cdf, delt_speed)
        print('The probability is: {:.2f}, users counted: {:.2f}'.format(p, p*item[1]))
        result = result + item[1] * p
    
    return result


# cell_id = 0
# start_ts = date2ts('2015-08-20 3:13:20')
# end_ts = date2ts('2015-08-20 23:13:20')
# prior_ts = 30 * 60 #  seconds
# extra_ts = 30 * 60 # 30 minutes

# num = mf3_explore_users_before(cell_id, 'right', 'inst', start_ts, end_ts, prior_ts, 1000, 100, normal_dis_scale)        
# print(num)

# num = mf3_explore_users_after(cell_id, 'right', 'inst', start_ts, end_ts, extra_ts, 500, 100, normal_dis_scale)        
# print(num) 

# cell = cell_b2_extend_area(cell_points_list[cell_id], 512)
# np_users = membership_fun1_inst(cell,start_ts - prior_ts, start_ts)
# np_users = membership_fun1_inst(cell, end_ts, end_ts + extra_ts)
# print(np_users[0])


# In[27]:

# the call-center
# call membership functions

def mf_result_list_transfer(result_list):
    print_list = []
    for item in result_list:
        line = '{},{},{},{},{},{}'.format(item[0],item[1],item[2],item[3],item[4],item[5])
        print_list.append(line)
    return print_list

cell_points_list = []
# cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
cell_points_list.append([[52.380853, 4.898841], [52.378196, 4.907432], [52.377343, 4.906678], [52.380259, 4.898109]])
cell_points_list.append([[52.379857, 4.925105], [52.379209, 4.928704], [52.378781, 4.928566], [52.379371, 4.924914]])
cell_points_list.append([[52.379352, 4.924892], [52.377850, 4.933742], [52.377177, 4.933332], [52.378710, 4.924574]])
cell_points_list.append([[52.375891, 4.929162], [52.374704, 4.936065], [52.374124, 4.935806], [52.375251, 4.928784]]) 

# cell area, 1 ha = 10000 m2
cell_area = [6.12,1.38,4.80,3.41]
# cell_area = [6.12 * 10000,1.38 * 10000,4.80 * 10000,3.41 * 10000]

np_bins_speed_cdf = 200

# call: cell_speed_query_outlier(cell_id,np_bins,0.96)
cell_speed_distribution_outlier = [11.595256916996, 7.1277865612648, 11.46209486166, 10.0632411067193]

result_list = []
def call_membership_fun1(cell_id, record_start_ts, record_end_ts):
#     cell_id = 3 # 0-3 = cell 1-4
#     record_start_ts = date2ts('2015-08-19 00:00:01') 
#     record_end_ts = date2ts('2015-08-20 23:59:59')
    bin_ts = 60 * 60 # the bin timestamp size, here per hour
    
    result_list = [['hour', 'start_ts','end_ts','twitter_density','inst_density', 'total']]
    for i in range(0, round((record_end_ts - record_start_ts) / bin_ts)):
        start_ts = record_start_ts + i * bin_ts
        end_ts = record_start_ts + (i+1) * bin_ts
        
        twitter = membership_fun1_twitter(cell_points_list[cell_id],start_ts,end_ts)[0]
        inst = membership_fun1_inst(cell_points_list[cell_id],start_ts,end_ts)[0]
        total = twitter + inst
        
        # np_users / cell_area = density
        twitter = twitter/cell_area[cell_id]
        inst = inst/cell_area[cell_id]
        total = total/cell_area[cell_id]
        
        result_list.append([i, start_ts,end_ts, twitter, inst, total])
        print('{} times, {} users'.format(i, total))
    
    return result_list

# result_list = call_membership_fun1()


def call_membership_fun2(cell_id, record_start_ts, record_end_ts):
#     cell_id = 3 # 0-3 = cell 1-4
#     record_start_ts = date2ts('2015-08-19 03:13:20') 
#     record_end_ts = date2ts('2015-08-20 23:13:20')
    bin_ts = 60 * 60 # the bin timestamp size, here per hour
    
    ext_length = 120 # the extend_length dealing with GPS resolution
    
    result_list = [['hour', 'start_ts','end_ts','twitter_density','inst_density', 'total']]
    for i in range(0, round((record_end_ts - record_start_ts) / bin_ts)):
        start_ts = record_start_ts + i * bin_ts
        end_ts = record_start_ts + (i+1) * bin_ts

        twitter = membership_fun2_twitter(cell_id, ext_length, start_ts, end_ts)
        inst = membership_fun2_inst(cell_id, ext_length, start_ts, end_ts)
        total = twitter + inst
        
        # np_users / cell_area = density
        twitter = twitter/cell_area[cell_id]
        inst = inst/cell_area[cell_id]
        total = total/cell_area[cell_id]
        
        result_list.append([i, start_ts,end_ts, twitter, inst, total])
        print('{} times, {} users'.format(i, total))
    
    return result_list

# result_list = call_membership_fun2()


# membership function 2.5: with normal distribution probability, with parameter of scale
def call_membership_fun2p5(cell_id, record_start_ts, record_end_ts):
#     cell_id = 0 # 0-3 = cell 1-4
#     record_start_ts = date2ts('2015-08-22 22:59:59') 
#     record_end_ts = date2ts('2015-08-22 23:59:59')
    bin_ts = 60 * 60 # the bin timestamp size, here per hour
    
    prior_ts = 30 * 60 #  seconds, the prior ts to be considered for each bin_ts
    extra_ts = 30 * 60
    
    max_length = max(prior_ts, extra_ts) * cell_speed_distribution_outlier[cell_id]
    bin_length = 100 # 100 or 50, the unit length to calculate the probability
    
    normal_dis_scale = max_length / 3 # the normal distribution scale parameter

    result_list = [['hour', 'start_ts','end_ts','twitter_density','inst_density', 'total']]
    for i in range(0, round((record_end_ts - record_start_ts) / bin_ts)):
        start_ts = record_start_ts + i * bin_ts
        end_ts = record_start_ts + (i+1) * bin_ts

        left_prior_twitter = mf2p5_explore_users_before(cell_id, 'left', 'twitter', start_ts, end_ts, prior_ts, max_length, bin_length, normal_dis_scale)    
        left_prior_ins = mf2p5_explore_users_before(cell_id, 'left', 'inst', start_ts, end_ts, prior_ts, max_length, bin_length, normal_dis_scale)
        right_prior_twitter = mf2p5_explore_users_before(cell_id, 'right', 'twitter', start_ts, end_ts, prior_ts, max_length, bin_length, normal_dis_scale)  
        right_prior_inst = mf2p5_explore_users_before(cell_id, 'right', 'inst', start_ts, end_ts, prior_ts, max_length, bin_length, normal_dis_scale)

        left_after_twitter = mf2p5_explore_users_after(cell_id, 'left', 'twitter', start_ts, end_ts, extra_ts, max_length, bin_length, normal_dis_scale)
        left_after_inst = mf2p5_explore_users_after(cell_id, 'left', 'inst', start_ts, end_ts, extra_ts, max_length, bin_length, normal_dis_scale)
        right_after_twitter = mf2p5_explore_users_after(cell_id, 'right', 'twitter', start_ts, end_ts, extra_ts, max_length, bin_length, normal_dis_scale)
        right_after_inst = mf2p5_explore_users_after(cell_id, 'right', 'inst', start_ts, end_ts, extra_ts, max_length, bin_length, normal_dis_scale)

        before = left_prior_twitter + left_prior_ins + right_prior_twitter + right_prior_inst
        after = left_after_twitter + left_after_inst + right_after_twitter + right_after_inst

        twitter = left_prior_twitter + right_prior_twitter + left_after_twitter + right_after_twitter
        inst = left_prior_ins + right_prior_inst + left_after_inst + right_after_inst
        
        twitter_mf1 = membership_fun1_twitter(cell_points_list[cell_id],start_ts,end_ts)[0]
        inst_mf2 = membership_fun1_inst(cell_points_list[cell_id],start_ts,end_ts)[0]
        
        total = before + after + twitter_mf1 + inst_mf2
        
        # np_users / cell_area = density
        twitter = twitter/cell_area[cell_id]
        inst = inst/cell_area[cell_id]
        total = total/cell_area[cell_id]
        
        result_list.append([i, start_ts,end_ts, twitter, inst, total])
    
    return result_list

# result_list = call_membership_fun2p5()



# membership function 3: with probability based on speed distribution
def call_membership_fun3(cell_id, record_start_ts, record_end_ts):
    print('Start membership function 3.')
    
#     cell_id = 0 # 0-3 = cell 1-4
#     record_start_ts = date2ts('2015-08-19 00:00:01') 
#     record_end_ts = date2ts('2015-08-22 23:59:59')
    bin_ts = 60 * 60 # the bin timestamp size, here per hour
    
    prior_ts = 30* 60  #  seconds, the prior ts to be considered for each bin_ts
    extra_ts = 30 * 60
    
    max_length = 25200 # 14 * 30 * 60, the 96% of speed distribution
    bin_length = 100 # the unit length to calculate the probability

    result_list = [['hour', 'start_ts','end_ts','twitter_density','inst_density', 'total']]
    for i in range(0, round((record_end_ts - record_start_ts) / bin_ts)):
        start_ts = record_start_ts + i * bin_ts
        end_ts = record_start_ts + (i+1) * bin_ts

        left_prior_twitter = mf3_explore_users_before(cell_id, 'left', 'twitter', start_ts, end_ts, prior_ts, max_length, bin_length)    
        left_prior_ins = mf3_explore_users_before(cell_id, 'left', 'inst', start_ts, end_ts, prior_ts, max_length, bin_length)
        right_prior_twitter = mf3_explore_users_before(cell_id, 'right', 'twitter', start_ts, end_ts, prior_ts, max_length, bin_length)  
        right_prior_inst = mf3_explore_users_before(cell_id, 'right', 'inst', start_ts, end_ts, prior_ts, max_length, bin_length)

        left_after_twitter = mf3_explore_users_after(cell_id, 'left', 'twitter', start_ts, end_ts, extra_ts, max_length, bin_length)
        left_after_inst = mf3_explore_users_after(cell_id, 'left', 'inst', start_ts, end_ts, extra_ts, max_length, bin_length)
        right_after_twitter = mf3_explore_users_after(cell_id, 'right', 'twitter', start_ts, end_ts, extra_ts, max_length, bin_length)
        right_after_inst = mf3_explore_users_after(cell_id, 'right', 'inst', start_ts, end_ts, extra_ts, max_length, bin_length)

        before = left_prior_twitter + left_prior_ins + right_prior_twitter + right_prior_inst
        after = left_after_twitter + left_after_inst + right_after_twitter + right_after_inst

        twitter = left_prior_twitter + right_prior_twitter + left_after_twitter + right_after_twitter
        inst = left_prior_ins + right_prior_inst + left_after_inst + right_after_inst
        
        twitter_mf1 = membership_fun1_twitter(cell_points_list[cell_id],start_ts,end_ts)[0]
        inst_mf1 = membership_fun1_inst(cell_points_list[cell_id],start_ts,end_ts)[0]
        
        total = before + after + twitter_mf1 + inst_mf1
        
        # np_users / cell_area = density
        twitter = twitter/cell_area[cell_id]
        inst = inst/cell_area[cell_id]
        total = total/cell_area[cell_id]
        
        result_list.append([i, start_ts, end_ts, twitter, inst, total])
    
    return result_list



for cell_id in range(0,4):
    
    # cell_id = 0 # 0-3 = cell 1-4
    record_start_ts = date2ts('2015-08-19 00:00:01') 
    record_end_ts = date2ts('2015-08-22 23:59:59')
    

    # cell_id, record_start_ts, record_end_ts
#     run = 'mf2p5'
#     output_file = '/root/icwsm17/sail15/sensor/exp/perhour/sm_density/{}/{}_cell_{}.txt'.format(run, run, cell_id)
    
#     result_list = call_membership_fun2p5(cell_id, record_start_ts, record_end_ts)
    
#     print('\n\n\n !DONE! \n\n\n')
#     printlist(result_list)


#     mywritelines2file(mf_result_list_transfer(result_list), output_file)

      


# In[ ]:




# In[ ]:




# In[ ]:

# new version of membership function: v2p5, v3
import timeit


# membership function 2p5
def call_membership_fun2p5_v2(cell_id, record_start_ts, record_end_ts, delta_t):
    print('Start membership function 2p5 v2.')
    
#     cell_id = 0 # 0-3 = cell 1-4
#     record_start_ts = date2ts('2015-08-19 00:00:01') 
#     record_end_ts = date2ts('2015-08-22 23:59:59')

    bin_ts = 60 * 60 # the bin timestamp size, here per hour
    
#     prior_ts = 30* 60  #  seconds, the prior ts to be considered for each bin_ts
#     extra_ts = 30 * 60
#     max_length = 4000 # 2 * 30 * 60

    prior_ts = delta_t
    extra_ts = delta_t
    
    max_length = 7 * delta_t * 60 # 7 * 30 * 60, the pedestrian speed is normally below 7.

    result_list = [['hour', 'start_ts','end_ts','twitter_density','inst_density', 'total']]
    for i in range(0, round((record_end_ts - record_start_ts) / bin_ts)):
        # per hour
        start_ts = record_start_ts + i * bin_ts
        end_ts = record_start_ts + (i+1) * bin_ts
    
        
#         mf2p5v2_mf_np_users(platform, timeing, cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, norm_dis_scale)
        twitter_before = mf2p5v2_mf_np_users('twitter', 'before', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length/3)
        twitter_after = mf2p5v2_mf_np_users('twitter','before', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length/3)
        inst_before = mf2p5v2_mf_np_users('inst','after', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length/3)
        inst_after = mf2p5v2_mf_np_users('inst','after', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length/3)
        
        twitter_mf1 = membership_fun1_twitter(cell_points_list[cell_id],start_ts,end_ts)[0]
        inst_mf1 = membership_fun1_inst(cell_points_list[cell_id],start_ts,end_ts)[0]
        
        twitter = twitter_before + twitter_after + twitter_mf1
        inst = inst_before + inst_after + inst_mf1
        
        total = twitter_before + twitter_after + twitter_mf1 + inst_before + inst_after + inst_mf1
        
        # np_users / cell_area = density
        twitter = twitter/cell_area[cell_id]
        inst = inst/cell_area[cell_id]
        total = total/cell_area[cell_id]
        
        result_list.append([i, start_ts, end_ts, twitter, inst, total])
    
    return result_list



# start_running = timeit.default_timer()

# for cell_id in range(0,4):    
    
# #     cell_id = 1 # 0-3 = cell 1-4
#     record_start_ts = date2ts('2015-08-19 00:00:01') 
#     record_end_ts = date2ts('2015-08-22 23:59:59')

#     run = 'mf2p5v2'
#     output_file = '/root/icwsm17/sail15/sensor/exp/perhour/sm_density/{}/{}_cell_{}.txt'.format(run, run, cell_id)

#     result_list = call_membership_fun2p5_v2(cell_id, record_start_ts, record_end_ts, 30*60)
#     mywritelines2file(mf_result_list_transfer(result_list), output_file)

    
# print('\n\n\n !DONE! \n\n\n')
# stop_running = timeit.default_timer()

# running_period = stop_running - start_running
# print('running cost(s): {}'.format(running_period))


# In[3]:

# new version of membership function: 3v2
import timeit
import numpy as np

# membership function 3v2
def call_membership_fun3_v2(cell_id, record_start_ts, record_end_ts, delta_t):
    print('Start membership function 3 v2.')
    
#     cell_id = 0 # 0-3 = cell 1-4
#     record_start_ts = date2ts('2015-08-19 00:00:01') 
#     record_end_ts = date2ts('2015-08-22 23:59:59')

    bin_ts = 60 * 60 # the bin timestamp size, here per hour
    
#     prior_ts = 30* 60  #  seconds, the prior ts to be considered for each bin_ts
#     extra_ts = 30 * 60
    
    prior_ts = delta_t
    extra_ts = delta_t
    
    max_length = 7 * delta_t * 60 # 7 * 30 * 60, the pedestrian speed is normally below 7.
    

#   for reading the flow data
#     folder = '/root/icwsm17/sail15/sensor/exp/perhour/sm_density/mf5/flow'
#     all_flow_data = np.load('{}/all_cell_flow.data.npy'.format(folder))
    
    sm_cell_flow_list = []


#       correctly considering direction, timming, and platform -------start------------------------------------     
#     before_left_right_in_list = []
#     after_left_left_out_list = []
#     before_right_left_in_list = []
#     after_right_right_out_list = []
#       correctly considering direction, timming, and platform -------end------------------------------------     
    
    
#       correctly considering timing, and platform -------start------------------------------------      
    all_before_list = []
    all_after_list = []
#       correctly considering timing, and platform -------end------------------------------------  
    
#     result_list = [['hour', 'start_ts','end_ts','twitter_density','inst_density', 'total']]
    for i in range(0, round((record_end_ts - record_start_ts) / bin_ts)):
        # per hour
        start_ts = record_start_ts + i * bin_ts
        end_ts = record_start_ts + (i+1) * bin_ts
    
#       data from progressive crawl
        
#       correctly considering timing, and platform -------start------------------------------------
#         direction: left, right, bidirection, radiation 
        twitter_before = mf3v2_mf_np_users_direction('twitter','before','bidirection',cell_id,start_ts,end_ts,prior_ts,extra_ts,max_length)
        twitter_after = mf3v2_mf_np_users_direction('twitter','after','bidirection',cell_id,start_ts,end_ts,prior_ts,extra_ts,max_length)       
        inst_before = mf3v2_mf_np_users_direction('inst','before','bidirection',cell_id,start_ts,end_ts,prior_ts,extra_ts,max_length)
        inst_after = mf3v2_mf_np_users_direction('inst','after','bidirection',cell_id,start_ts,end_ts,prior_ts,extra_ts,max_length)

#         based on mf1 --- start

#         twiiter_before_redundant = membership_fun1_twitter(cell_points_list[cell_id],start_ts-prior_ts,start_ts)[0]
#         twiiter_after_redundant = membership_fun1_twitter(cell_points_list[cell_id],end_ts,end_ts + extra_ts)[0]
#         inst_before_redundant = membership_fun1_inst(cell_points_list[cell_id],start_ts-prior_ts,start_ts)[0]
#         inst_after_redundant = membership_fun1_inst(cell_points_list[cell_id],end_ts,end_ts + extra_ts)[0]

#         twitter_mf_base = membership_fun1_twitter(cell_points_list[cell_id],start_ts,end_ts)[0]
#         inst_mf_base = membership_fun1_inst(cell_points_list[cell_id],start_ts,end_ts)[0]

#          based on mf1 --- end

#         based on mf2 --- start

        twiiter_before_redundant = membership_fun2_twitter(cell_id, 112, start_ts-prior_ts,start_ts)
        twiiter_after_redundant =  membership_fun2_twitter(cell_id, 112, end_ts,end_ts + extra_ts)
        inst_before_redundant = membership_fun2_inst(cell_id, 112, start_ts-prior_ts,start_ts)
        inst_after_redundant = membership_fun2_inst(cell_id, 112, end_ts,end_ts + extra_ts)
        
#         twitter_mf_base = membership_fun2_twitter(cell_id, 112, start_ts, end_ts)
#         inst_mf_base = membership_fun2_inst(cell_id, 112, start_ts, end_ts)

#         based on mf2 --- end


# sum-up result        
#         twitter = twitter_before + twitter_after + twitter_mf_base - twiiter_before_redundant - twiiter_after_redundant
#         inst = inst_before + inst_after + inst_mf_base - inst_before_redundant - inst_after_redundant
#         
#         total = twitter + inst

        all_before = twitter_before + inst_before - twiiter_before_redundant - inst_before_redundant
        all_after = twitter_after + inst_after - twiiter_after_redundant - inst_after_redundant
        
        # np_users / cell_area = density
#         all_before = all_before/cell_area[cell_id]
#         all_after_list = all_after_list/cell_area[cell_id]        
        
        all_before_list.append(all_before)
        all_after_list.append(all_after)
        
        
        sm_cell_flow_list=[all_before_list,all_after_list]
#       correctly considering timming, and platform -------end------------------------------------  

        
        # np_users / cell_area = density
#         twitter = twitter/cell_area[cell_id]
#         inst = inst/cell_area[cell_id]
        
#         total = twitter + inst
        
#         result_list.append([i, start_ts, end_ts, twitter, inst, total])
        
#   return the additional number of users              
    
    sm_cell_flow_list = np.asarray(sm_cell_flow_list)
    
#     return result_list
    return sm_cell_flow_list



start_running = timeit.default_timer()

# cell_id = 0 # 0-3 = cell 1-4
record_start_ts = date2ts('2015-08-19 00:00:01') 
record_end_ts = date2ts('2015-08-22 23:59:59')

# record_start_ts = date2ts('2015-08-21 11:00:01') 
# record_end_ts = date2ts('2015-08-21 13:59:59')


sm_flow_list = []
run = 'mf5'
output_file = './mf5_sm_flow.data'
for cell_id in range(0,4):    

    result_list = call_membership_fun3_v2(cell_id, record_start_ts, record_end_ts, 30*60)
#     mywritelines2file(mf_result_list_transfer(result_list), output_file)
    sm_flow_list.append(result_list)

np.save(output_file, sm_flow_list)
    
print('\n\n\n !DONE! \n\n\n')
stop_running = timeit.default_timer()

running_period = stop_running - start_running
print('running cost(s): {} s, or {} mins'.format(running_period, running_period/60))





