'''
Created on 15 Sep 2017

@author: vgong
'''
import numpy as np
from icwsm17.mfs.MF_probability import MF_probability
import icwsm17.entity.DBSource as DBS
import icwsm17.entity.ExperimentProfile as EP
import pandas as pd

class MF_flow(object):
    '''
    classdocs
    '''


    def __init__(self, dbs, ep, data_folder, flow_rate_file):
        '''
        Constructor
        '''
        self.dbs = dbs
        self.ep = ep
        self.data_folder = data_folder
        self.flow_rate_file = flow_rate_file
    
    def cal_mf_prob(self):
        # run mf_prob to get the data in array

        mf_strategy = MF_probability.from_dbs_ep(self.dbs, self.ep)
        pedestrian_speed = 3  # the pedestrian speed is normally below 7.
        max_length = pedestrian_speed * self.ep.delta_ts  # e.g. 3 * (30*60), delta_t_ts is in seconds
        mf_prob_result = []
        for cell_id in range(0, 1):
            result_list = mf_strategy.call_membership_fun_probability(cell_id, self.ep.start_ts, self.ep.end_ts, self.ep.bin_ts, self.ep.delta_ts, max_length)
            result_array = np.asarray(result_list)
            result_array = np.transpose(result_array)
            '''result_list = [sequence, before, after, basis, total]'''
            df = pd.DataFrame(result_array, columns = ['sequence', 'before', 'after', 'basis', 'total'])
            print("Start saving the result.------------------------------------------------------")
            df.to_csv("{}/mf_flow_tmp_mf_prob_cell_{}.txt".format(self.data_folder, cell_id))
            print("Done.------------------------------------------------------")
            mf_prob_result.append(df)
            
    
        return mf_prob_result
    
    
    def cal_flow_rate(self):
        flow_rate_df =  pd.read_csv(self.flow_rate_file, index_col=0)
        return flow_rate_df
    
    
    def call_x(self):
        
        self.data_folder
        
        
        
        
    
        return 0
    
    
    def call_x_auto(self):
        # run mf_prob to get the data in list in DataFrame
        mf_prob_df_result = self.cal_mf_prob()
        # run mf_prob_before and after to get the
        flow_rate_df_result = self.cal_flow_rate()
        
        # change delta_t, before change, flow_in_out cam and smd change, flow rate, MF_flow_before_after
        
        
        return 0
    
    
#     def call_calculation(self, mf_prob_celldata_file, flow_rate_file):
#         
#         mf_prob_data = np.load(mf_prob_celldata_file)
#         flow_rate_df =  pd.read_csv(flow_rate_file, index_col=0)
#         
#         #build df with mf_prob_data: before, after, basis
#         mf_prob_df = pd.DataFrame(mf_prob_data, columns = ['sequence', 'before', 'after', 'basis', 'total'])
# #         print(mf_prob_df)
#         #build new df column in mf_prob_data through calculation with flow rate
#         df = pd.concat([mf_prob_df,  flow_rate_df], axis=1)
#         
#         print(df)
#         
#         # result = value column of calculation
#         # for x row in mf_prob, the before_rate is 2x-1, the after_rate is 2x+2
#         
#         return 0
    
    
    
def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    dbs = DBS.DBSource('icwsm17', 'postgres', 'localhost', 'postgres', '9634')
    data_folder = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0918-v1"
    flow_rate_file = "{}/flow_rate_60min.txt".format(data_folder)
    ep = EP.ExperimentProfile()
    
    mf_strategy = MF_flow(dbs, ep, data_folder, flow_rate_file)
    result = mf_strategy.call_x()
    print("Start saving the result.------------------------------------------------------")
    result.to_csv("{}/mf_flow_gap_{}.txt".format(data_folder,ep.delta_tm))
    print("Done.------------------------------------------------------")

if __name__ == '__main__': main()