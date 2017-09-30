'''
Created on 29 Sep 2017

@author: vgong
'''
import pandas as pd
import icwsm17.measure.metric as MT

class Measure(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        
    
    @classmethod
    def mae(cls,dic):
        
        basic_v = MT.Metric.error_metric(dic["sensor_list"], dic["mf_basic_list"])[2]
        gps_v = MT.Metric.error_metric(dic["sensor_list"], dic["mf_gps_list"])[2]
        speed_v = MT.Metric.error_metric(dic["sensor_list"], dic["mf_speed_list"])[2]
        flow_v = MT.Metric.error_metric(dic["sensor_list"], dic["mf_flow_list"])[2]
        
        mae_list = [basic_v,gps_v,speed_v,flow_v]
#         print(mae_list)
        
        return mae_list
    
    
    @classmethod
    def mape(cls,dic):
        
        basic_v = MT.Metric.error_percentage(dic["sensor_list"], dic["mf_basic_list"])
        gps_v = MT.Metric.error_percentage(dic["sensor_list"], dic["mf_gps_list"])
        speed_v = MT.Metric.error_percentage(dic["sensor_list"], dic["mf_speed_list"])
        flow_v = MT.Metric.error_percentage(dic["sensor_list"], dic["mf_flow_list"])
        
        mape_list = [basic_v,gps_v,speed_v,flow_v]
#         print(mape_list)
        
        return mape_list
    

    @classmethod
    def pearsonr(cls,dic):
        
        basic_v = MT.Metric.pearsonr_metric(dic["sensor_list"], dic["mf_basic_list"])
        gps_v = MT.Metric.pearsonr_metric(dic["sensor_list"], dic["mf_gps_list"])
        speed_v = MT.Metric.pearsonr_metric(dic["sensor_list"], dic["mf_speed_list"])
        flow_v = MT.Metric.pearsonr_metric(dic["sensor_list"], dic["mf_flow_list"])
        
        correlation = [basic_v[0],gps_v[0],speed_v[0],flow_v[0]]
        p_value = [basic_v[1],gps_v[1],speed_v[1],flow_v[1]]
        
        pearsonr_list = [correlation,p_value]
#         print(pearsonr_list)
        
        return pearsonr_list

def main():
    
    output_folder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0928-v1/case2_deliverables'
    dic = {}
    dic["output_folder"] = output_folder
    dic["sensor_list"] = pd.read_csv(output_folder+"/sensor_density_per_hour.txt", index_col = 0)["sensor_density"].values
    dic["mf_basic_list"] = pd.read_csv(output_folder+"/mf_basic.txt", index_col = 0)["density_basic"].values
    dic["mf_gps_list"] = pd.read_csv(output_folder+"/mf_gps.txt", index_col = 0)["density_gps"].values
    dic["mf_speed_list"] = pd.read_csv(output_folder+"/mf_speed.txt", index_col = 0)["density_speed"].values
    dic["mf_flow_list"] = pd.read_csv(output_folder+"/mf_flow.txt", index_col = 0)["density_flow"].values

    mae_list = Measure.mae(dic)
    mape_list = Measure.mape(dic)
    pearsonr = Measure.pearsonr(dic)
    pear_coe = pearsonr[0]
    pear_p = pearsonr[1]
    
    df = pd.DataFrame({"mae":mae_list,"mape":mape_list, "pear_coe": pear_coe, "pear_p":pear_p},index = ['mf_basic_list','mf_gps_list','mf_speed_list','mf_flow_list'])
    print(df)
    df.to_csv(output_folder + "/measure_delta_30mins.txt")
    
    return 0





if __name__ == '__main__': main()