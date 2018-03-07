'''
Created on 6 Oct 2017

@author: vgong
'''
from decimal import Decimal
import numpy as np
import icwsm17.mfs.toolbox as tb
from icwsm17.common.MyDB import MyDB
import pandas as pd
from icwsm17.entity.DBSource import DBSource as DBS
from icwsm17.entity.DBDetail import DBDetail as DBD
import icwsm17.mfs.cell_profile as cp
import icwsm17.common.extendarea as exarea
from pandas.io.tests.parser import index_col
import icwsm17.common.myio as myio
# from matplotlib.pyplot import table

# print(np.array([1.123456789]))

def format_density(df_density):
    density = []
    for i in range(len(df_density.index)):
        if df_density.iloc[i,0]>=0:
            density.append(df_density.iloc[i,0])
    
#     print(len(density))
#     print(",,,,,,,,,,")
#     print(density)
    
    density = np.asarray(density)
    mean = np.mean(density)
    std = np.std(density)
    # print(df_den.describe())
    mean_str = "{:.3e}".format(Decimal(mean))
    std_str = "{:.3e}".format(Decimal(std))
    result = "{}$\pm${}".format(mean_str,std_str)
    return result


'''
# calculate the mean and std and format it with scientific anotation

folder = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0928-v1/case2_deliverables"

df_den_sensor = pd.read_csv(folder + "/sensor_density_per_hour.txt", index_col=0)
df_den_basic = pd.read_csv(folder + "/mf_basic.txt", index_col=0)
df_den_gps = pd.read_csv(folder + "/mf_gps.txt", index_col=0)
df_den_speed = pd.read_csv(folder + "/mf_speed.txt", index_col=0)
df_den_flow = pd.read_csv(folder + "/mf_flow.txt", index_col=0)

print(format_density(df_den_sensor))
print(format_density(df_den_basic))
print(format_density(df_den_gps))
print(format_density(df_den_speed))
print(format_density(df_den_flow))
'''



# read measurements for delta = 30 for filling the table
# folder = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0928-v1/case2_deliverables"
# df_measure = pd.read_csv(folder + "/measure_delta_30mins.txt", index_col = 0)
# print(df_measure)

folder = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1/case2"

df_speed_mae = pd.read_csv(folder + "/mf_speed_all_deltaT/speed_mae_full_df.txt", index_col = 0)
df_speed_correlation = pd.read_csv(folder + "/mf_speed_all_deltaT/speed_spearman_full_df.txt", index_col = 0)

df_flow_mae = pd.read_csv(folder + "/mf_flow_all_deltaT/flow_mae_full_df.txt", index_col = 0)
df_flow_correlation = pd.read_csv(folder + "/mf_flow_all_deltaT/flow_spearman_full_df.txt", index_col = 0)

# print(df_speed_mae)
# 
# print(df_speed_mae.loc[["d_mean"]])

# speed_mae_mean_arr = df_speed_mae.loc[["d_mean"]].values.tolist()[0]
# myio.mywritelines2file(speed_mae_mean_arr, folder + "/mf_speed_all_deltaT/speed_mae_mean_df.txt" )


# speed_corr_mean_arr = df_speed_correlation.loc[["correlation"]].values.tolist()[0]
# myio.mywritelines2file(speed_corr_mean_arr, folder + "/mf_speed_all_deltaT/speed_corr_df.txt" )


flow_mae_mean_arr = df_flow_mae.loc[["d_mean"]].values.tolist()[0]
myio.mywritelines2file(flow_mae_mean_arr, folder + "/mf_flow_all_deltaT/flow_mae_mean_df.txt" )

flow_corr_mean_arr = df_flow_correlation.loc[["correlation"]].values.tolist()[0]
myio.mywritelines2file(flow_corr_mean_arr, folder + "/mf_flow_all_deltaT/flow_corr_df.txt" )







