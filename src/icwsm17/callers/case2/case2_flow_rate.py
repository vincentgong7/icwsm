'''
Created on 22 Sep 2017

@author: vgong
'''
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

class case2_flow_rate(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def cal_rate(self, dic):
        
        folder = dic["folder"]
        cam_df = pd.read_csv(folder + "/" + dic["cam"], index_col = 0)
#         print(cam_df)
        
        ba_df = pd.read_csv(folder + "/" + dic["before_after"], index_col = 0)
#         print(ba_df)
        
        df=pd.DataFrame()
        df["before_rate"] = cam_df["cam_in_flow"] / ba_df["before"]
        df["after_rate"] = cam_df["cam_out_flow"] / ba_df["after"]
        
        print(df)
        df.to_csv(folder+"/flow_rate_30_mins.txt")
        return df
        
        
    def sum_rate_by_hours(self,dic,df_o):
        
        before = df_o["before_rate"].values
        after = df_o["after_rate"].values
#         
#         be_short_rate = np.ones(len(before)/dic["sum_hours"])
#         af_short_rate = np.ones(len(before)/dic["sum_hours"])
#         be_sum, af_sum = 0
#         for i in range(0, len(before)/dic["sum_hours"]):
#             for t in range(0, dic["sum_hours"]):
#                 pos = i* dic["sum_hours"] + t
#                 be_sum = be_sum + before[pos]
#                 af_sum = af_sum + after[pos]
#             be_sum = be_sum/dic["sum_hours"] 
#             af_sum = af_sum/dic["sum_hours"]
        
        '''6hours'''    
        
        be_short_rate = []
        af_short_rate = []
        
        
        print(df_o.before_rate[0:12].mean())
        
        for i in range(0, len(before), dic["sum_hours"]):

            be_mean = df_o.before_rate[i:i+dic["sum_hours"]].mean()
            af_mean = df_o.after_rate[i:i+dic["sum_hours"]].mean()
         
            for j in range(0,dic["sum_hours"],2):
                be_short_rate.append(be_mean)
                af_short_rate.append(af_mean)

        print(be_short_rate)
        print(af_short_rate)
        
        df = DataFrame({"before_rate":be_short_rate, "after_rate": af_short_rate})
        df.to_csv(dic["folder"]+"/flow_rate.txt")
        
        return 0
        
def main():        
    
    c2fr = case2_flow_rate()
    dic = {}
    dic["folder"] = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1/rate'
    dic["cam"] = 'case_2_mf_flow_cam.txt'
    dic["before_after"] = 'case_2_mf_flow_before_after.txt'
    dic["sum_hours"] = 6 *2 #'''because per 0.5hour'''
    
    df_ori = c2fr.cal_rate(dic)
    df = c2fr.sum_rate_by_hours(dic, df_ori)
    
    
    return 0




if __name__ == '__main__': main()