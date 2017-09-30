'''
Created on 24 Sep 2017

@author: vgong
'''
import pandas as pd
import icwsm17.measure.metric as MT

class measure(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def mf_flow_mae_cal(self, dic):
        df_flows = pd.read_csv(dic["mf_flow_dfs_file"], index_col = 0)
#         print(df_flows)
        df_sensor = pd.read_csv(dic["mf_sensor_density_file"], index_col = 0)
        df_sensor_list = df_sensor.sensor_density[dic["hours_start"]:dic["hours_end"]].values
        
        col_list = list(df_flows.columns.values)
        
        df_mae = pd.DataFrame(index = ['d_min','d_max','d_mean','d_median','d_std'])
#         df_mae.set_index()
        for col in col_list:
            est_list = df_flows[col][dic["hours_start"]:dic["hours_end"]].values
            df_mae[col] = MT.Metric.error_metric(df_sensor_list, est_list)
        
        print(df_mae)
        return df_mae

    def mf_speed_mae_cal(self,dic):
        df_speed = pd.read_csv(dic["mf_speed_dfs_file"], index_col = 0)
#         print(df_flows)
        df_sensor = pd.read_csv(dic["mf_sensor_density_file"], index_col = 0)
        df_sensor_list = df_sensor.sensor_density[dic["hours_start"]:dic["hours_end"]].values
        
        col_list = list(df_speed.columns.values)
        
        df_mae = pd.DataFrame(index = ['d_min','d_max','d_mean','d_median','d_std'])
#         df_mae.set_index()
        for col in col_list:
            est_list = df_speed[col][dic["hours_start"]:dic["hours_end"]].values
            df_mae[col] = MT.Metric.error_metric(df_sensor_list, est_list)
        
        print(df_mae)
        return df_mae 
    
    def mf_flow_mape_cal(self, dic):
        df_flows = pd.read_csv(dic["mf_flow_dfs_file"], index_col = 0)
#         print(df_flows)
        df_sensor = pd.read_csv(dic["mf_sensor_density_file"], index_col = 0)
        df_sensor_list = df_sensor.sensor_density[dic["hours_start"]:dic["hours_end"]].values
        
        col_list = list(df_flows.columns.values)
        
        df_mape = pd.DataFrame(index = ['mape'])
#         df_mae.set_index()
        for col in col_list:
            est_list = df_flows[col][dic["hours_start"]:dic["hours_end"]].values
            df_mape[col] = MT.Metric.error_percentage(df_sensor_list, est_list)
        
        print(df_mape)
        return df_mape
    
    
    def mf_speed_mape_cal(self,dic):
        df_speed = pd.read_csv(dic["mf_speed_dfs_file"], index_col = 0)
#         print(df_flows)
        df_sensor = pd.read_csv(dic["mf_sensor_density_file"], index_col = 0)
        df_sensor_list = df_sensor.sensor_density[dic["hours_start"]:dic["hours_end"]].values
        
        col_list = list(df_speed.columns.values)
        
        df_mape = pd.DataFrame(index = ['mape'])
#         df_mae.set_index()
        for col in col_list:
            est_list = df_speed[col][dic["hours_start"]:dic["hours_end"]].values
            df_mape[col] = MT.Metric.error_percentage(df_sensor_list, est_list)
        
        print(df_mape)
        return df_mape
        
    def mf_flow_spearman_cal(self,dic):
        df_flows = pd.read_csv(dic["mf_flow_dfs_file"], index_col = 0)
#         print(df_flows)
        df_sensor = pd.read_csv(dic["mf_sensor_density_file"], index_col = 0)
        df_sensor_list = df_sensor.sensor_density[dic["hours_start"]:dic["hours_end"]].values
        
        col_list = list(df_flows.columns.values)
        
        df_spearman = pd.DataFrame(index = ['correlation','p_value'])
#         df_mae.set_index()
        for col in col_list:
            est_list = df_flows[col][dic["hours_start"]:dic["hours_end"]].values
            df_spearman[col] = MT.Metric.spearmanr_metric(df_sensor_list, est_list)
        
        print(df_spearman)
        return df_spearman
    
    
    def mf_speed_spearman_cal(self,dic):
        df_speed = pd.read_csv(dic["mf_speed_dfs_file"], index_col = 0)
#         print(df_flows)
        df_sensor = pd.read_csv(dic["mf_sensor_density_file"], index_col = 0)
        df_sensor_list = df_sensor.sensor_density[dic["hours_start"]:dic["hours_end"]].values
        
        col_list = list(df_speed.columns.values)
        
        df_spearman = pd.DataFrame(index = ['correlation','p_value'])
#         df_mae.set_index()
        for col in col_list:
            est_list = df_speed[col][dic["hours_start"]:dic["hours_end"]].values
            df_spearman[col] = MT.Metric.spearmanr_metric(df_sensor_list, est_list)
        
        print(df_spearman)
        return df_spearman 
    
def main():
    
    m = measure()
    output_folder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1/case2'
    
    dic = {}
    flow_folder = 'mf_flow_all_deltaT'
    speed_folder = 'mf_speed_all_deltaT'
    
    dic["mf_flow_dfs_file"] = "{}/{}/mf_flow_per_hour_deltaT.txt".format(output_folder,flow_folder)
    dic["mf_speed_dfs_file"] = "{}/{}/mf_speed_all.txt".format(output_folder,speed_folder)
    dic["mf_sensor_density_file"] = "{}/sensor/sensor_density_per_hour.txt".format(output_folder)
    dic["hours_start"] = 0
    dic["hours_end"] = 60
    
    '''MAE:'''
#     flow_mae_full_df = m.mf_flow_mae_cal(dic)
#     flow_mae_full_df.to_csv("{}/{}/flow_mae_full_df.txt".format(output_folder,flow_folder))
#     
#     speed_mae_full_df = m.mf_speed_mae_cal(dic)
#     speed_mae_full_df.to_csv("{}/{}/speed_mae_full_df.txt".format(output_folder,speed_folder))
    
    '''MAPE:'''
    flow_mape_full_df = m.mf_flow_mape_cal(dic)
    flow_mape_full_df.to_csv("{}/{}/flow_mape_full_df.txt".format(output_folder,flow_folder))
     
    speed_mape_full_df = m.mf_speed_mape_cal(dic)
    speed_mape_full_df.to_csv("{}/{}/speed_mape_full_df.txt".format(output_folder,speed_folder))    
    
    
    
    
    '''Spearman'''
    
#     flow_spearman_full_df = m.mf_flow_spearman_cal(dic)
#     flow_spearman_full_df.to_csv("{}/{}/flow_spearman_full_df.txt".format(output_folder,flow_folder))
#     
#     speed_spearman_full_df = m.mf_speed_spearman_cal(dic)
#     speed_spearman_full_df.to_csv("{}/{}/speed_spearman_full_df.txt".format(output_folder,speed_folder))
    

    return 0






if __name__ == '__main__': main()