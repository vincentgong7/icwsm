'''
Created on 22 Sep 2017

@author: vgong
'''

import icwsm17.entity.ExperimentProfile as EP
import icwsm17.mfs.toolbox as tb

class case1_ep(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @classmethod
    def get_case1_ep(cls):
        ep = EP.ExperimentProfile()
        
        ep.cell_points_list.append([[52.380853, 4.898841], [52.378196, 4.907432], [52.377343, 4.906678], [52.380259, 4.898109]])
        ep.cell_points_list.append([[52.379857, 4.925105], [52.379209, 4.928704], [52.378781, 4.928566], [52.379371, 4.924914]])
        ep.cell_points_list.append([[52.379352, 4.924892], [52.377850, 4.933742], [52.377177, 4.933332], [52.378710, 4.924574]])
        ep.cell_points_list.append([[52.375891, 4.929162], [52.374704, 4.936065], [52.374124, 4.935806], [52.375251, 4.928784]])
        
        ep.cell_area = [6.12*10000,1.38*10000,4.80*10000,3.41*10000]
        
        ep.cell_half_length = [328,127,309,243] # the half length of each cells
        
                # config of the experiment
        ep.start_ts = tb.date2ts('2015-08-19 00:00:00') 
        ep.end_ts = tb.date2ts('2015-08-23 00:00:00')
        ep.bin_ts = 60*60  # the bin timestamp size, here per hour, in seconds
        ep.delta_tm = 30 # in minutes
        ep.delta_ts = ep.delta_tm*60 # in seconds, 0.5h
        
        return ep
