'''
Created on 14 Feb 2017

@author: vgong
'''
from math import radians, cos, sin, asin, sqrt

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