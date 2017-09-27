'''
Created on 13 Sep 2017

@author: vgong
'''
import icwsm17.mfs.toolbox as tb
import numpy as np
import psycopg2
import pandas as pd

class Cam_flow(object):
    '''
    classdocs
    '''


    def __init__(self, port='9634', dbname='icwsm17', data_table = 'case2sensor.paired_wifi'):
        '''
        Constructor
        '''
        self.dbname = dbname
        self.port = port
        self.username = 'postgres'
        self.password = 'postgres'
        self.host = 'localhost'
        self.data_table = data_table
        db_conn_str = "dbname='{0}' user='{1}' host='{2}' password='{3}' port='{4}'".format(self.dbname,self.username,self.host,self.password,self.port)
        self.conn = psycopg2.connect(db_conn_str)
        self.where_clause = ''
     
    def process(self, record_start_ts, record_end_ts, gap_tt_minutes, mode):
        
        result = []
        bin_tt_sec = gap_tt_minutes * 60
        for i in range(0, round((record_end_ts - record_start_ts) / bin_tt_sec)):
            start_ts = record_start_ts + i* bin_tt_sec
            end_ts = record_start_ts + (i + 1) * bin_tt_sec
            
            state = mode
            
            sql = "SELECT {} FROM {} where {}<=van_cet_ts and van_cet_ts <= {}".format(state, self.data_table, start_ts, end_ts)
            if (self.where_clause):
                sql = "{} and {}".format(sql, self.where_clause)
            
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchone()
            val = rows[0]
            if not val:
                val = 0
            print("{} times,{}".format(i,val))
            result.append(val)
        
#         result_df = pd.DataFrame({"cam_all_flow":result})
        return result
     
    def set_where(self, where_clause):
        self.where_clause = where_clause
        
def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    function_flag = "cam_count"
    
    port = 9634
    dbname='icwsm17'
    cam_table = 'case2sensor.v_cam_data_cell'
    outputfolder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0919-v2'
    gap_tt_minutes = 30 # minutes
    start_ts = tb.date2ts('2016-04-26 00:00:00') 
    end_ts = tb.date2ts('2016-04-29 00:00:00')
    
    '''--------Camera F-------------'''
    extra_out_put_flag = 'F'
    output_file = '{}/{}_{}.txt'.format(outputfolder, function_flag,extra_out_put_flag)
    cam_flow = Cam_flow(port,dbname,cam_table)
    # add where-clouse if needed, camera = 'ZUID-A', 'ZUID-F1', 'ZUID-F2'
    cam_flow.set_where("(camera = 'ZUID-F1' or camera = 'ZUID-F2')") 
    
    # mode = "direction1_up" or "direction2_down" or "direction1_up + direction2_down" or "direction1_up - direction2_down".
    # mode default = "direction1_up + direction2_down"
    # SQL: select #mode# from ...
    result_f = cam_flow.process(start_ts, end_ts, gap_tt_minutes, "sum(direction1_up + direction2_down)/2") # result is a list
    result_f_df = pd.DataFrame({extra_out_put_flag:result_f})
    print(result_f_df)
    result_f_df.to_csv(output_file, index=0)
    
    '''--------Camera A-------------'''
    extra_out_put_flag = 'A'
    output_file = '{}/{}_{}.txt'.format(outputfolder, function_flag,extra_out_put_flag)
    cam_flow = Cam_flow(port,dbname,cam_table)
    # add where-clouse if needed, camera = 'ZUID-A', 'ZUID-F1', 'ZUID-F2'
    cam_flow.set_where("(camera = 'ZUID-A')") 
    
    # mode = "direction1_up" or "direction2_down" or "direction1_up + direction2_down" or "direction1_up - direction2_down".
    # mode default = "direction1_up + direction2_down"
    # SQL: select #mode# from ...
    result_a = cam_flow.process(start_ts, end_ts, gap_tt_minutes, "sum(direction1_up + direction2_down)") # result is a list
    result_a_df = pd.DataFrame({extra_out_put_flag:result_a})
    print(result_a_df)
    result_a_df.to_csv(output_file, index=0)   
#
#     
# #   save as a numpy table
#     tb.printlist(result)
#     np.save(output_file, result)
#         
# #       save to file
#     tb.printlist(result)
#     tb.mywritelines2file(tb.result_list_transfer(result), output_file)
    

if __name__ == '__main__': main()