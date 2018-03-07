'''
Created on 1 Nov 2017

@author: vgong
'''


import pandas as pd
import numpy as np
from icwsm17.callers.case1.case1_ep import case1_ep  as ce1

class Density_Calculation(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    
def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    dc = Density_Calculation()
    case1_ep = ce1.get_case1_ep()
    
    folder = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/1101-v1/case1-algorithm/tem_data"
    camera_folder = "{}/camera".format(folder)
    wifi_folder = "{}/wifi".format(folder)
    
    df_cam_all_day = pd.read_csv(camera_folder+"/cam_all_by_day_cell_4.txt")
    print(df_cam_all_day)
    
    df_wifi_all_day = pd.read_csv(wifi_folder + "/wifi_all_by_day_cell_4.txt")
    print(df_wifi_all_day)

    df_rate_per_day = pd.DataFrame()
    df_rate_per_day["rate_day"] = df_cam_all_day["total"]/df_wifi_all_day["total"]
    print(df_rate_per_day)
    
    rate_per_hour = []
    for day in range(0,4):
        for hour in range(0,24):
            rate_hour = df_rate_per_day['rate_day'].iloc[day]
            rate_per_hour.append(rate_hour)
    
    print("The rate per hour.")
    print(rate_per_hour)
    
    
    df_rate_per_day.to_csv(folder + "/rate_day_cell_4.txt")
    
#     now, prepare the wifi data
    df_left_in = pd.read_csv(wifi_folder + "/cell_4_left_in", index_col = 0)
    df_right_in = pd.read_csv(wifi_folder + "/cell_4_right_in", index_col = 0)
    df_left_out = pd.read_csv(wifi_folder + "/cell_4_left_out", index_col = 0)
    df_right_out = pd.read_csv(wifi_folder + "/cell_4_right_out", index_col = 0)
    
    df_in = pd.DataFrame()
    df_in["wifi_in"] = df_left_in["total"] + df_right_in["total"]
#     print(df_in)
    
    df_out = pd.DataFrame()
    df_out["wifi_out"] = df_left_out["total"] + df_right_out["total"]
#     print(df_out)
    
    df_wifi_cell_4 = pd.DataFrame()
    df_wifi_cell_4["ts_hour"] = df_left_in["ts_hour"]
    df_wifi_cell_4["wifi_in"] = df_in["wifi_in"]
    df_wifi_cell_4["wifi_out"] = df_out["wifi_out"]
#     df_wifi_cell_4["stay"] = df_wifi_cell_4["wifi_in"] - df_wifi_cell_4["wifi_out"]
    
    
    df_wifi_cell_4["wifi_in_cumsum"] = np.cumsum(np.nan_to_num(df_wifi_cell_4["wifi_in"].values), dtype=int)
    df_wifi_cell_4["wifi_out_cumsum"] = np.cumsum(np.nan_to_num(df_wifi_cell_4["wifi_out"].values), dtype=int)
    
    df_wifi_cell_4["stay"] = df_wifi_cell_4["wifi_in_cumsum"] - df_wifi_cell_4["wifi_out_cumsum"]
#     print(df_wifi_cell_4)


#     last_stay = 0
#     v_stay = []
#     for i in range(len(df_wifi_cell_4.index)):
#         if(df_wifi_cell_4['wifi_in'].iloc[i]!=None and df_wifi_cell_4['wifi_out'].iloc[i]!=None):
#             v_in = df_wifi_cell_4['wifi_in'].iloc[i]
#             v_out = df_wifi_cell_4['wifi_out'].iloc[i]
# #             stay = v_in - v_out + last_stay
#             stay = v_in
#             v_stay.append(stay)
#             last_stay = stay
    
#     print(v_stay)
#     df_wifi_cell_4["stay"] = v_stay
    
    df_wifi_cell_4["rate"] = rate_per_hour[0:92]
#     
    cell_4_area = case1_ep.cell_area[3]
    df_wifi_cell_4["density"] = df_wifi_cell_4["stay"] * df_wifi_cell_4["rate"] / cell_4_area
    df_wifi_cell_4["density_in"] = df_wifi_cell_4["wifi_in"] * df_wifi_cell_4["rate"] / cell_4_area
    df_wifi_cell_4["density_out"] = df_wifi_cell_4["wifi_out"] * df_wifi_cell_4["rate"] / cell_4_area
    
    print(df_wifi_cell_4)
    
    print()
    print("Density:")
    print()
#     for i in range(len(df_wifi_cell_4["density"].values)):
#         print(df_wifi_cell_4["density"][i])
        
#     for i in range(len(df_wifi_cell_4["density_in"].values)):
#         print(df_wifi_cell_4["density_in"][i])

    for i in range(len(df_wifi_cell_4["density_out"].values)):
        print(df_wifi_cell_4["density_out"][i])
            
    '''calculate number of people stay considering people entered before'''
    
    
if __name__ == '__main__': main()