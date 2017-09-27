'''
Created on 15 Feb 2017

@author: vgong
'''

import pandas as pd
import numpy as np




def load_data():
    differ_flow_data = np.load('/Users/vgong/Documents/workspaces/workspace20170116/ICWSM17/icwsm_data/flow/all_cell_diff_flow.data.npy')
    mf3_ra_before_after_data = np.load('/Users/vgong/Documents/workspaces/workspace20170116/ICWSM17/icwsm_data/mf3/mf3_ra_before_after/mf3_ra_before_after.data.npy')
    return [differ_flow_data, mf3_ra_before_after_data]




if __name__ == '__main__':

# load the data
    differ_flow_data, mf3_ra_before_after_data = load_data()
#     print('differ_flow_data: {}'.format(differ_flow_data.shape))
#     print('mf3_ra_before_after_data: {}'.format(mf3_ra_before_after_data.shape))
 
#  clean the data: filter the flow <= 0
    differ_flow_data[differ_flow_data <= 0] = 1
#     print(differ_flow_data[0])

# build panel
    flow_pal = pd.Panel(differ_flow_data)
    sm_pal = pd.Panel(mf3_ra_before_after_data)
    

    
# calculate c
    c_pal = flow_pal.divide(sm_pal,2)
    c_pal.set_axis(0,['cell_0','cell_1','cell_2','cell_3'])
    c_pal.set_axis(1,['before','after'])
    
#     print(c_pal['cell_0'].head())
    
    
    
    # or do it through numpy
    # c_array = differ_flow_data / mf3_ra_before_after_data
    

    def fun_p1(s):
        return s.max()
    
    xp = c_pal.apply(fun_p1, axis = 1)
    
#     print(xp['cell_0'].head())
#     print(c_pal['cell_0'].shape)
    print(c_pal.shape)
    
    print('axis = 0, result = {}'.format(c_pal.apply(fun_p1, axis = 0).shape))
    
    print('axis = 1, result = {}'.format(c_pal.apply(fun_p1, axis = 1).shape))
    
    print('axis = 2, result = {}'.format(c_pal.apply(fun_p1, axis = 2).shape))
    
    def fun_p2(s):
        s_tmp = s[0]+s[1]
        return s.size
    
    print(c_pal['cell_0'])
    xf = c_pal.apply(fun_p2, axis = 2)
    print(xf)
# shorten the c value from 96h to 24h by calling a function
    
    
    
    