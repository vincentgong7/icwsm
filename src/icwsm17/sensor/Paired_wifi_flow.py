'''
Created on 13 Sep 2017

@author: vgong
'''
import icwsm17.mfs.toolbox as tb
import numpy as np
import psycopg2
import pandas as pd

class Paired_wifi_flow(object):
    '''
    classdocs
    '''


    def __init__(self, port='9634', dbname='icwsm17', paired_wifi_table = 'case2sensor.v_cam_data_cell'):
        '''
        Constructor
        '''
        self.dbname = dbname
        self.port = port
        self.username = 'postgres'
        self.password = 'postgres'
        self.host = 'localhost'
        self.paired_wifi_table = paired_wifi_table
        db_conn_str = "dbname='{0}' user='{1}' host='{2}' password='{3}' port='{4}'".format(self.dbname,self.username,self.host,self.password,self.port)
        self.conn = psycopg2.connect(db_conn_str)
        self.where_clause = ''
     
    def process(self, record_start_ts, record_end_ts, gap_tt_minutes):
        
        result = []
        bin_tt_sec = gap_tt_minutes * 60
        for i in range(0, round((record_end_ts - record_start_ts) / bin_tt_sec)):
            start_ts = record_start_ts + i* bin_tt_sec
            end_ts = record_start_ts + (i + 1) * bin_tt_sec
            
            sql = "SELECT count(id) FROM {} where {}<=firstseen_a_ts and firstseen_a_ts <= {}".format(self.paired_wifi_table, start_ts, end_ts)
            if (self.where_clause):
                sql = "{} and {}".format(sql, self.where_clause)
            
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchone()
            print("{} times,{}".format(i,rows[0]))
            result.append(rows[0])
            df_result = pd.DataFrame({"paired_wifi_flow": result})
            
        return df_result
     
    def set_where(self, where_clause):
        self.where_clause = where_clause
        
def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    function_flag = "paired_wifi_count"
    
    port = 9634
    dbname='icwsm17'
    paired_wifi_table = 'case2sensor.v_paired_wifi'
    outputfolder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0920-v1'
    gap_tt_minutes = 60 # minutes
    start_ts = tb.date2ts('2016-04-26 00:00:00') 
    end_ts = tb.date2ts('2016-04-29 00:00:00')
    output_file = '{}/{}_gap_{}mins.txt'.format(outputfolder, function_flag, gap_tt_minutes)
    
    paired_wifi_flow = Paired_wifi_flow(port,dbname,paired_wifi_table)
    paired_wifi_flow.set_where("(hostname_a = 'rb-0035' or hostname_a = 'rb-0018')") # add where-clouse if needed
    result = paired_wifi_flow.process(start_ts, end_ts, gap_tt_minutes) # result is a list
    
    print('\n\n\n !DONE! \n\n\n')
    
    print(result)
    result.to_csv(output_file)
# #   save as a numpy table
#     tb.printlist(result)
#     np.save(output_file, result)
#         
# #       save to file
#     tb.printlist(result)
#     tb.mywritelines2file(tb.result_list_transfer(result), output_file)
    
    

if __name__ == '__main__': main()