'''
Created on 22 Sep 2017

@author: vgong
'''

import icwsm17.entity.DBSource as DBS
import numpy as np
import pandas as pd
import icwsm17.common.MyDB as MyDB
import icwsm17.mfs.toolbox as tb

class Cam(object):
    '''
    classdocs
    '''


    def __init__(self, dic):
        '''
        Constructor
        '''
        self.dic = dic
        self.cam_x = dic['cam.x']
        self.cam_y = dic['cam.y']
        self.cam_x_in = dic['cam.x.in']
        self.cam_x_out = dic['cam.x.out']
        self.cam_y_in = dic['cam.y.in']
        self.cam_y_out = dic['cam.y.out']
        self.cam_table = dic['cam.table']
        self.cam_camera_field_name = dic['cam.camera_field_name']
        self.gap_tt_minutes = dic['cam.gap.tt.minutes']
        self.van_cet_ts = dic['van_cet_ts'] = 'van_cet_ts'
        self.record_start_ts = dic['record_start_ts']
        self.record_end_ts = dic['record_end_ts']
        
        self.mydb = MyDB.MyDB.from_dbs(dic['dbs'])
    
    def process_in(self):
        state_x_in = "sum({})".format(self.cam_x_in)
        result_x = self.process(state_x_in, "{}='{}'".format(self.cam_camera_field_name, self.cam_x))
#         print(result_x)
        
        state_y_in = "sum({})".format(self.cam_y_in)
        result_y = self.process(state_y_in, "{}='{}'".format(self.cam_camera_field_name, self.cam_y))
#         print(result_y)
        
        result_arr = result_x + result_y
        return pd.DataFrame({"cam_in_flow":result_arr})
        
    def process_out(self):
        state_x_out = "sum({})".format(self.cam_x_out)
        result_x = self.process(state_x_out, "{}='{}'".format(self.cam_camera_field_name, self.cam_x))
#         print(result_x)
        
        state_y_out = "sum({})".format(self.cam_y_out)
        result_y = self.process(state_y_out, "{}='{}'".format(self.cam_camera_field_name, self.cam_y))
#         print(result_y)
        
        result_arr = result_x + result_y
        return pd.DataFrame({"cam_out_flow":result_arr})
    
    def process_sum(self):
        '''note: no where-clouse, so only one time of in+out is sufficient'''
        sql_state_sum = "sum({})".format(self.cam_x_in + "+" + self.cam_x_out)
        
        result_arr = self.process(sql_state_sum)
        return pd.DataFrame({"cam_sum_flow":result_arr})
    
    def process_all(self):
        df_in = self.process_in()
        df_out = self.process_out()
        df_sum = self.process_sum()
        
        df_list = [df_in, df_out, df_sum]
        df_all = pd.concat(df_list, axis=1)
        
        return df_all
    
    def process(self, sql_state, where_clause=""):
        
        result = []
        bin_tt_sec = self.gap_tt_minutes * 60
        record_start_ts = self.record_start_ts
        record_end_ts = self.record_end_ts
        for i in range(0, round((record_end_ts - record_start_ts) / bin_tt_sec)):
            start_ts = record_start_ts + i * bin_tt_sec
            end_ts = record_start_ts + (i + 1) * bin_tt_sec
            
            sql = "SELECT {} FROM {} where {}<={} and {} <= {}".format(sql_state, self.cam_table, start_ts, self.van_cet_ts, self.van_cet_ts , end_ts)
            
            if (where_clause != ""):
                sql = "{} and {}".format(sql, where_clause)
            
            conn = self.mydb.get_conn()
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchone()
            val = 0
            if rows:
                val = rows[0]
            if not val:
                val = 0
#             print("{} times,{}".format(i,val))
            result.append(val)
#             cursor.close()
        
        result = np.asarray(result)
        return result
       
        
def main():
    
    dbs = DBS.DBSource()
    
    dic = {"dbs":dbs}
    dic['cam.camera_field_name'] = 'camera'
    dic['cam.table'] = 'case2sensor.cam_data_cell'
    dic['van_cet_ts'] = 'van_cet_ts'
    dic['cam.x'] = 'ZUID-A' 
    dic['cam.y'] = "ZUID-F"
    dic['cam.x.in'] = 'direction2_down'
    dic['cam.x.out'] = 'direction1_up'
    dic['cam.y.in'] = 'direction1_up'
    dic['cam.y.out'] = 'direction2_down'
    dic['cam.gap.tt.minutes'] = 30
    dic['record_start_ts'] = tb.date2ts('2016-04-26 00:00:00') 
    dic['record_end_ts'] = tb.date2ts('2016-04-29 00:00:00')
    dic["outputfolder"] = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1/rate"

    
    cam = Cam(dic)
#     result = cam.process_in()
#     result = cam.process_out()
#     result = cam.process_sum()
    result = cam.process_all()
    
#     gap_tt_minutes
#     record_start_ts
#     record_end_ts
    print(result)
    output_file = '{}/case_2_mf_flow_cam.txt'.format(dic["outputfolder"])
    result.to_csv(output_file)
    return result

    









if __name__ == '__main__': main()
