'''
Created on 18 Sep 2017

@author: vgong
'''

class DBDetail(object):
    '''
    classdocs
    '''


    def __init__(self, cam_table = 'case2sensor.v_cam_data_cell', paired_wifi_table = 'case2sensor.v_cam_data_cell', twitter_table='case2smd.v_twitter_geo_is', inst_table='case2smd.v_inst_geo_is'):
        '''
        Constructor
        next version: read property file automatically
        '''
        self.cam_table = cam_table
        self.paired_wifi_table = paired_wifi_table
        self.twitter_table = twitter_table
        self.inst_table = inst_table