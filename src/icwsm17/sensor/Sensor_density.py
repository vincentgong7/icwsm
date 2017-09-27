'''
Created on 21 Sep 2017

@author: vgong
'''
import pandas as pd
import numpy as np
import icwsm17.mfs.cell_profile as cp

class Sensor_density(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.df_paired_wifi_flow = None
        self.df_cam_all_flow = None
        self.df_paired_wifi_flow_per_hour = None
        self.gap_hour = 6
        self.area = 0.640*10000
        
    @classmethod    
    def from_filepath(cls, paired_wifi_file, cam_all_flow_file, df_paired_wifi_flow_per_hour_file, gap_hour, area): 
        
        obj = cls()
        obj.df_paired_wifi_flow = pd.read_csv(paired_wifi_file, index_col = 0)
        obj.df_cam_all_flow = pd.read_csv(cam_all_flow_file, index_col = 0)
        obj.df_paired_wifi_flow_per_hour = pd.read_csv(df_paired_wifi_flow_per_hour_file, index_col = 0)
        obj.gap_hour = gap_hour
        obj.area = area
        return obj
    
    def calculate_factor(self, df_cam_all_flow, df_paired_wifi_flow):
        df = pd.DataFrame()
        df["sensor_factor"] = self.df_cam_all_flow["cam_all_flow"] / self.df_paired_wifi_flow["paired_wifi_flow"]
        return df
    
    def adjust_factor(self, np_factor):
        g = self.gap_hour
        len_factor = len(np_factor)
        val = np.ones(g*len_factor)
        
        for i in range(0, len_factor):
            for t in range(0, g):
                position = i*g + t
                val[position] = np_factor[i]
                
        return val
    
    def calculate_density(self, df_factor):
        np_factor = df_factor["sensor_factor"].values
        adjusted_np_factors = self.adjust_factor(np_factor)
        np_pw_hour = self.df_paired_wifi_flow_per_hour["paired_wifi_flow"].values
        
        population = np.ones(len(np_pw_hour))
        for i in range(0,len(np_pw_hour)):
            
            population[i] = np_pw_hour[i] * adjusted_np_factors[i]
            
        
        density = population/self.area
        
        result_df = pd.DataFrame({"sensor_density": density})
        return result_df
    
    def calculate(self):
        
        '''calculate the estimation according to the rate'''
        df_factor = self.calculate_factor(self.df_cam_all_flow, self.df_paired_wifi_flow)
        df_density = self.calculate_density(df_factor)
        
        return df_density
    
        
def main():
    
    folder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0920-v1'
    paired_wifi_file = "{}/paired_wifi_count_gap_360mins.txt".format(folder)
    cam_all_flow_file = "{}/cam_all_flow_gap_360mins.txt".format(folder)
    df_paired_wifi_flow_per_hour_file = "{}/paired_wifi_count_gap_60mins.txt".format(folder)
    gap_hour = 6
    
    sensor_factor = Sensor_density.from_filepath(paired_wifi_file, cam_all_flow_file, df_paired_wifi_flow_per_hour_file, gap_hour, cp.cell_area[0])
    
    df_result = sensor_factor.calculate()
    
    print(df_result)
    output_file = "{}/result/sensor_density_per_hour.txt".format(folder)
    df_result.to_csv(output_file)
    
    return 0



if __name__ == '__main__': main()
