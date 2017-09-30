'''
Created on 15 Sep 2017

@author: vgong
'''
import numpy as np
import icwsm17.mfs.toolbox as tb
from icwsm17.common.MyDB import MyDB
import pandas as pd
from icwsm17.entity.DBSource import DBSource as DBS
from icwsm17.entity.DBDetail import DBDetail as DBD

if __name__ == '__main__':
    print("test")
#     test_array = np.load("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0911-v1/mf_probability_cell_0.txt.npy")
#     print(len(test_array))
#     print(len(test_array[1]))
#     print(test_array.shape)
#     
#     print(test_array[4][71])
    
#     output_file = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0911-v1/test.txt"
#     
#     print_list = []
#     a_test_array = np.transpose(test_array)
#     for item in a_test_array:
#         line = '{},{},{},{},{}'.format(item[0],item[1],item[2],item[3],item[4])
#         print_list.append(line)
#     
#     tb.mywritelines2file(print_list, output_file)
     
#     test_array_tmp = np.transpose(test_array[0:2],0)
#     print(test_array_tmp)
#     print(len(test_array_tmp))
    
#     print(np.transpose(test_array_tmp))
#     
#     test2 = np.transpose(test_array_tmp)
#     print(len(test2))
#     print(len(test2[0]))
#     
#     print(test2)
    
    
    
#     arr = np.arange(12).reshape((4,3))
#     print (arr)
#     print(len(arr))
#     print(len(arr[0]))
#     print (arr[:,1])
#     print (np.transpose(arr))
    
    
#     dbs = DBS()
#     mydb = MyDB.from_dbs(dbs)
#     conn = mydb.get_conn()
#     cursor = mydb.get_cursor()
#     sql = 'SELECT * FROM case2sensor.v_cam_data_cell limit 20'
#     cursor.execute(sql)
#     rows = cursor.fetchone()
#     cursor.close()
#     print(rows)
#      
#     dbs = DBS()
#     dbdetail = DBD()
#     dbs.set_detail(dbdetail)
#     print(dbs.dbdetail.cam_table)
#     
#     
#     print(tb.date2ts('2016-04-26 00:30:00')-tb.date2ts('2016-04-26 00:00:00'))
#     print(30*60)
     
#     output_file = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0916-v1/flow_rate_per30min.txt" 
#     df1 = pd.read_csv(output_file, index_col=0)
#     df2 = pd.read_csv(output_file, index_col=0)
#     
#     df = pd.concat([df1,df2], index = [df1, df2], axis = 1)
#     
#     print(df)

# before = np.load('/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0918-v1/mf_probability_cell_0_after.txt.npy')
# print(before)
#     
#     df1 = pd.read_csv("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0919-v2/mf_flow_mf_flow_tmp_mf_prob_cell_0.txt")
#     df2 = pd.read_csv("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0919-v2/mf_flow_mf_flow_tmp_mf_prob_cell_1.txt")
#     
#     test_list = [df1, df2]
#     
# #     print(df1)
#     print("----------------")
# #     print(df2)
#     result = pd.concat(test_list, axis=1)
#     print("----------------")
#     print(result)


#     df1 = pd.read_csv("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0919-v2/flow_rate_30min.txt", index_col=0)
#     print(df1)
#      
#     print("-----------------")
#     print(df1.flow_rate_before[list(range(0,144,2))])
#     
    
#     t = list(range(0,144,2))
#     print(t)
#     
#     for i in range(5):
#         print(i)



# d1 = '2.269e-1' 
# d2 = '2.108e-1'
# 
# density = float(d1) + float(d2)
# print(density)


#     df1 = pd.read_csv("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0920-v1/result/mf_prob/mf_probability_cell_0.txt", index_col=0)
# #     print(df1)
#     
#     df1["MF_speed_density"] = df1["total"] / (0.640*10000)
#     df1["MF_basis_density"] = df1["basis"] / (0.640*10000)
# #     print(df1["MF_speed_density"])
#     df_result = pd.DataFrame(df1["MF_speed_density"], df1.MF_basis_density)
#     df_result.to_csv("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0920-v1/result/mf_prob/mf_probability_cell_0_density.txt")


#     df = pd.read_csv("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1/case2/mf_speed/mf_probability_cell_0_deltaT_30.txt", index_col = 0)
#     df2 = pd.DataFrame()
#     df2["density_speed"] = df["total_density"]
#     df2.to_csv("/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0928-v1/case2_deliverables/mf_speed.txt")
    
    
    
    