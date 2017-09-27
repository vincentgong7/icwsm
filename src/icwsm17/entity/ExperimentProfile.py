'''
Created on 18 Sep 2017

@author: vgong
'''

import icwsm17.mfs.toolbox as tb

class ExperimentProfile(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        read from config files
        '''
        self.cell_points_list = []
        # cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise

        # this is the terrain of Zuidplein Amsterdam
        self.cell_points_list.append([[52.340821, 4.872787], [52.340840, 4.873365], [52.339472, 4.873540], [52.33945, 4.87278]])
        
        # this is the terrains of Sail event
#         self.cell_points_list.append([[52.380853, 4.898841], [52.378196, 4.907432], [52.377343, 4.906678], [52.380259, 4.898109]])
#         self.cell_points_list.append([[52.379857, 4.925105], [52.379209, 4.928704], [52.378781, 4.928566], [52.379371, 4.924914]])
#         self.cell_points_list.append([[52.379352, 4.924892], [52.377850, 4.933742], [52.377177, 4.933332], [52.378710, 4.924574]])
#         self.cell_points_list.append([[52.375891, 4.929162], [52.374704, 4.936065], [52.374124, 4.935806], [52.375251, 4.928784]])
        
        # cell area, 1 ha = 10000 m2
        self.cell_area = [0.640*10000]
#         self.cell_area = [6.12*10000,1.38*10000,4.80*10000,3.41*10000]
        
        # the half length of each cells
        self.cell_half_length = [72]
#         self.cell_half_length = [328,127,309,243] # the half length of each cells

        
        # config of the experiment
        self.start_ts = tb.date2ts('2016-04-26 00:00:00') 
        self.end_ts = tb.date2ts('2016-04-29 00:00:00')
        self.bin_ts = 60*60  # the bin timestamp size, here per hour, in seconds
        self.delta_tm = 30 # in minutes
        self.delta_ts = self.delta_tm*60 # in seconds, 0.5h
        
        
        