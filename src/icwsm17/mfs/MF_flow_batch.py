'''
Created on 15 Sep 2017

@author: vgong
'''
import numpy as np
from icwsm17.mfs.MF_probability import MF_probability
import icwsm17.entity.DBSource as DBS
import icwsm17.entity.ExperimentProfile as EP
import pandas as pd
import os

class MF_flow_batch(object):
    '''
    classdocs
    '''


    def __init__(self, dbs, ep, mf_prob_folder, mf_flow_folder, mf_flow_rate_file, ):
        '''
        Constructor
        '''
        self.dbs = dbs
        self.ep = ep
        self.mf_prob_folder = mf_prob_folder
        self.mf_flow_folder = mf_flow_folder
        self.mf_flow_rate_file = mf_flow_rate_file
    
    def cal_flow_rate(self):
        flow_rate_df =  pd.read_csv(self.mf_flow_rate_file, index_col=0)
#         flow_rate_array = flow_rate_df.iloc[:,2].values
#         print(flow_rate_df['flow_rate_before'].iloc[20])
        flow_rate_before = flow_rate_df['before_rate'].values
        flow_rate_after = flow_rate_df['after_rate'].values
        return [flow_rate_before, flow_rate_after]
    
    def get_mf_prob_filelist(self):
        '''iterate mf_prob_data'''
        mf_prob_file_path = []
        mf_prob_filename = []
        directory = os.fsencode(self.mf_prob_folder)
        for file in os.listdir(directory):
                filename = os.fsdecode(file)
                if filename.endswith(".txt"):
                    full_filename = "{}/{}".format(self.mf_prob_folder, filename)
#                     print("{}/{}".format(self.mf_prob_folder, filename))
                    mf_prob_file_path.append(full_filename)
                    mf_prob_filename.append(filename)
                    continue
                else:
                    continue
        
        return [mf_prob_filename, mf_prob_file_path]
    
    def calculate_mf_flow(self, flow_rate_array_list, mf_prob_files):
#        flow_rate_array_list =  [flow_rate_before, flow_rate_after]
        flow_rate_before = flow_rate_array_list[0]
        flow_rate_after = flow_rate_array_list[1]
        result_list = []
        
        mf_prob_filename = mf_prob_files[0]
        mf_prob_file_path = mf_prob_files[1]
        
        for f in range(0, len(mf_prob_file_path)):
            filename = mf_prob_filename[f]
            file = mf_prob_file_path[f]
#             print(file)
            df = pd.read_csv(file, index_col=0)
#             print(df)
            
            before_array = df["before"].values
            after_array = df["after"].values
            basis_array = df["basis"]
            
            total_array = []
            
            length = len(basis_array)
            for i in range(length):
                
                if i==0:
                    before_rate = 1
                else:
                    before_rate = flow_rate_before[i-1]
                
                if i+1 == len(flow_rate_after):
                    after_rate = 1
                else:
                    after_rate = flow_rate_after[i+1]
                    
                basis = basis_array[i]
                
                total = before_array[i] * before_rate + after_array[i] * after_rate + basis
                total_array.append(total)
                
            '''modify when multiple cells'''
            total_array = np.asarray(total_array)
            total_array = total_array / self.ep.cell_area[0]
            
            df_total = pd.DataFrame({filename[0:-4]: total_array})
            
            
            df_total.to_csv("{}/mf_flow_{}.txt".format(self.mf_flow_folder, filename[0:-4]), index=0)
            result_list.append(df_total)
            
#         print(result_df) 
        result_df = pd.concat(result_list, axis=1)
        return result_df
            
    def call_x(self):
        '''
        mf_prob_folder
        mf_flow_folder
        mf_flow_rate_file
        '''
        
        flow_rate_array_list = self.cal_flow_rate()
#         [flow_rate_before, flow_rate_after]
        mf_prob_files = self.get_mf_prob_filelist()
        
        result_df = self.calculate_mf_flow(flow_rate_array_list, mf_prob_files)
        
        return result_df
    
    
    
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
    
    case = "case2"
    
    dbs = DBS.DBSource('icwsm17', 'postgres', 'localhost', 'postgres', '9634')
    ep = EP.ExperimentProfile()
    
    '''--------------------------------------------------------------------------------------'''
    folder = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1"
    mf_prob_folder = "{}/{}/mf_prob".format(folder.case)
    mf_flow_folder = "{}/{}/mf_flow".format(folder,case)
    flow_rate_file = "{}/{}/mf_flow/rate/flow_rate.txt".format(folder,case)
    '''--------------------------------------------------------------------------------------'''
    
    mf_strategy = MF_flow_batch(dbs, ep, mf_prob_folder, mf_flow_folder, flow_rate_file)
    result = mf_strategy.call_x()
    print("Start saving the result.------------------------------------------------------")
    result.to_csv("{}/mf_flow_per_hour_gap_{}.txt".format(mf_flow_folder,ep.delta_tm))
    print("Done.------------------------------------------------------")

if __name__ == '__main__': main()