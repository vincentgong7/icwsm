'''
Created on 16 Sep 2017

@author: vgong
'''
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

class MF_flow_rate_calculator(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def generate_flow_in_out_from_cam(self, a_up_in, a_down_out, f_up_out, f_down_in):
        df = pd.DataFrame({'a_up_in': a_up_in,
                           'a_down_out': a_down_out,
                           'f_up_out': f_up_out,
                           'f_down_in': f_down_in
                           })
        
        df['cam_flow_in'] = df['a_up_in'] + df['f_down_in']
        df['cam_flow_out'] = df['a_down_out'] + df['f_up_out']
        
        result = df[['cam_flow_in', 'cam_flow_out']]
        
#         print(result)
        return result
    
    def generate_smd_in_out(self, smd_in, smd_out):
        df = pd.DataFrame({'smd_in': smd_in,
                           'smd_out': smd_out})
        
#         print(df)
        result = df
        return result
    
    def generate_flow_rate(self, cam_flow, smd_flow):
#         df = pd.concat([cam_flow['cam_flow_in'], cam_flow['cam_flow_out'], smd_flow['smd_in'], smd_flow['smd_out']], axis=1, keys=['cam_flow_in', 'cam_flow_out', 'smd_in', 'smd_out'])
        df = pd.concat([cam_flow,  smd_flow], axis=1)

        df['flow_in_rate'] = df['cam_flow_in'] / df['smd_in']
        df['flow_out_rate'] = df['cam_flow_out'] / df['smd_out']
#         print(df)
#         
        result = df[['flow_in_rate','flow_out_rate']]
#         print(result)
        return result
     
     
    def cal_based_on_in_out(self, folder):
         
        a_up_in = np.load("{}/cam_count_gap_30mins_A_up_in.txt.npy".format(folder))
        a_down_out = np.load("{}/cam_count_gap_30mins_A_down_out.txt.npy".format(folder))
        f_up_out = np.load("{}/cam_count_gap_30mins_F_up_out.txt.npy".format(folder))
        f_down_in = np.load("{}/cam_count_gap_30mins_F_down_in.txt.npy".format(folder))
        smd_in = np.load("{}/mf_probability_cell_0_before.txt.npy".format(folder))
        smd_out = np.load("{}/mf_probability_cell_0_after.txt.npy".format(folder))
        
        mfrc = MF_flow_rate_calculator()
        cam_flow = mfrc.generate_flow_in_out_from_cam(a_up_in, a_down_out, f_up_out, f_down_in)
        smd_flow = mfrc.generate_smd_in_out(smd_in, smd_out)
        flow_rate = mfrc.generate_flow_rate(cam_flow, smd_flow)
         
        return flow_rate
    
    @classmethod
    def cal_based_on_all(cls, folder):
        
        a_all = np.load("{}/cam_count_A.txt.npy".format(folder))
        f_all = np.load("{}/cam_count_F.txt.npy".format(folder))
        cam_all = a_all + f_all
        
        before = np.load("{}/mf_probability_cell_0_before.txt.npy".format(folder))
        after = np.load("{}/mf_probability_cell_0_after.txt.npy".format(folder))
        
        rate_before = cam_all / before
        rate_after = cam_all / after
        
#         df = DataFrame({'cam_all': cam_all})
        df_rate = DataFrame({'flow_rate_before': rate_before,
                             'flow_rate_after': rate_after})
        
        print(df_rate)
        return df_rate
    
    @classmethod
    def cal_based_on_all_dataframe(cls, folder):
        
        df_cal = pd.DataFrame()
        
        a_all = pd.read_csv("{}/cam_count_A.txt".format(folder))
        f_all = pd.read_csv("{}/cam_count_F.txt".format(folder))
        df_cal["cam_total"] = a_all["A"] + f_all["F"]
        
        before = pd.read_csv("{}/mf_probability_cell_0_before.txt".format(folder))
        after = pd.read_csv("{}/mf_probability_cell_0_after.txt".format(folder))
        
        df_cal["before"] = before["before"]
        df_cal["after"] = after["after"]
        
        df_cal["flow_before_rate"] = df_cal["cam_total"] / df_cal["before"]
        df_cal["flow_after_rate"] = df_cal["cam_total"] / df_cal["after"]
        
#         df = DataFrame({'cam_all': cam_all})
        df_rate = DataFrame({'flow_rate_before': df_cal["flow_before_rate"].values,
                             'flow_rate_after': df_cal["flow_after_rate"].values})
        
        print(df_rate)
        return df_rate
    
    @classmethod
    def rate_30min_to_per_hour(self, result_df):
        before = result_df.flow_rate_before.values
        after = result_df.flow_rate_after.values
        
        before_result = []
        for i in range(0,len(before),2):
            x = before[i]
            y = before[i+1]
            z = (x+y)/2
            before_result.append(z)
        
        after_result = []
        for i in range(0,len(after),2):
            x = after[i]
            y = after[i+1]
            z = (x+y)/2
            after_result.append(z)
            
        result_df = pd.DataFrame({"flow_rate_before":before_result,
                                  "flow_rate_after":after_result})
        
        
        return result_df
    
    
    
def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    folder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0919-v3/rate'
    output_file = "{}/flow_rate_30min.txt".format(folder)
    
    result_df = MF_flow_rate_calculator.cal_based_on_all_dataframe(folder)

    print("Start saving the result.------------------------------------------------------")
    result_df.to_csv(output_file)
    print("Done.------------------------------------------------------")
    
#     read_df = pd.read_csv(output_file, index_col=0)
#     print(read_df)
    
    '''------option: in case need to transfer per 30mins to per hour--------'''
    output_file_per_hour = MF_flow_rate_calculator.rate_30min_to_per_hour(result_df)
    output_file_per_hour.to_csv("{}{}".format(output_file[:-9],"per_hour.txt"))
    print(output_file_per_hour)
    
    return 0


if __name__ == '__main__': main()
