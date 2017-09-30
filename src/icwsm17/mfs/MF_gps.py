'''
Created on 30 May 2017

@author: vgong
'''
import sys
sys.path.append('/root/case2/socialmedia/')

import icwsm17.mfs.cell_profile as cp
import icwsm17.mfs.toolbox as tb
import icwsm17.common.extendarea as exarea
import psycopg2
import numpy as np
import pandas as pd

class MF_gps(object):
        
    def __init__(self, port='9634', dbname='icwsm17', twitter_table = 'case2smd.v_twitter_geo_is', inst_table = 'case2smd.v_inst_geo_is'):
        self.dbname = dbname
        self.port = port
        self.username = 'postgres'
        self.password = 'postgres'
        self.host = 'localhost'
        self.twitter_table = twitter_table
        self.inst_table = inst_table
        self.bin_ts = 60 * 60 #the bin timestamp size, here per hour
    
    def call_membership_fun_gps(self, cell_id, record_start_ts, record_end_ts):
    #     cell_id = 3 # 0-3 = cell 1-4
    #     record_start_ts = date2ts('2015-08-19 00:00:01') 
    #     record_end_ts = date2ts('2015-08-20 23:59:59')
        
#         db_conn_str = "dbname='{0}' user='{1}' host='{2}' password='{3}' port='{4}'".format('icwsm17','postgres','localhost','postgres','5432')
        db_conn_str = "dbname='{0}' user='{1}' host='{2}' password='{3}' port='{4}'".format(self.dbname,self.username,self.host,self.password,self.port)

        conn = psycopg2.connect(db_conn_str)
    
        result_list = [['hour', 'start_ts','end_ts','twitter_density','inst_density', 'total']]
        result_total_value_list = []
        for i in range(0, round((record_end_ts - record_start_ts) / self.bin_ts)):
            start_ts = record_start_ts + i * self.bin_ts
            end_ts = record_start_ts + (i+1) * self.bin_ts
            
            # decide the none or expanding the area
            cell_coord_list = exarea.cell_b1b2_extend(cp.cell_points_list[cell_id], 113)
            
            twitter = self.membership_fun_basic_twitter(cell_coord_list,start_ts,end_ts, conn)
            inst = self.membership_fun_basic_inst(cell_coord_list,start_ts,end_ts, conn)
            total = twitter + inst
            
            # np_users / cell_area = density
            twitter = twitter/cp.cell_area[cell_id]
            inst = inst/cp.cell_area[cell_id]
            total = total/cp.cell_area[cell_id]
            
            result_list.append([i, start_ts,end_ts, twitter, inst, total])
            result_total_value_list.append(total)
            print('{} times, {} users'.format(i, total))
        
#         result_total_value_list = np.asarray(result_total_value_list)
        result = [result_list, result_total_value_list]
        return result_total_value_list
    
    def membership_fun_basic_twitter(self, cell_coord_list, start_ts, end_ts, conn):
        
        #cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
        #area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
        cursor = conn.cursor()
        area_str = tb.transfer_coords(cell_coord_list)
        sql_fields = 'count(distinct uid) as num'
#         sql_table_name = 'public.twitter_geo_is_data_user'
        sql_table_name = self.twitter_table
        sql = "SELECT {} FROM {} as t1 where {} <= t1.ts_linux and t1.ts_linux <={} and ST_Within(ST_MakePoint(t1.lon, t1.lat),ST_GeomFromText('POLYGON(({}))'));".format(sql_fields,sql_table_name,start_ts,end_ts,area_str)
#         print(sql)
        cursor.execute(sql)
        rows = cursor.fetchone();
        cursor.close()
        return rows[0]
    
    def membership_fun_basic_inst(self, cell_coord_list, start_ts, end_ts, conn):
        
        #cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
        #area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
        cursor = conn.cursor()
        area_str = tb.transfer_coords(cell_coord_list)
        sql_fields = 'count(distinct uid) as num'
#         sql_table_name = 'public.inst_geo_is_data_user'
        sql_table_name = self.inst_table
        sql = "SELECT {} FROM {} as t1 where {} <= t1.ts_linux and t1.ts_linux <={} and ST_Within(ST_MakePoint(t1.lon, t1.lat),ST_GeomFromText('POLYGON(({}))'));".format(sql_fields,sql_table_name,start_ts,end_ts,area_str)
        cursor.execute(sql)
        rows = cursor.fetchone();
        cursor.close()
        return rows[0]

    
def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    strategy_suffix = 'gps'
    port = 9634
    outputfolder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1/case2/mf_gps'

#    configured for runing on the server
#     port = 5432
#     outputfolder = '/root/case2/socialmedia/result/0531-v1'

    
    mf_strategy = MF_gps(port)
    for cell_id in range(0,1):
    # cell_id = 1 # 0-3 = cell 1-4
        record_start_ts = tb.date2ts('2016-04-26 00:00:00') 
        record_end_ts = tb.date2ts('2016-04-29 00:00:00')
        output_file = '{}/mf_{}_cell_{}.txt'.format(outputfolder, strategy_suffix, cell_id)

        # cell_id, record_start_ts, record_end_ts
        
        result = mf_strategy.call_membership_fun_gps(cell_id, record_start_ts, record_end_ts)
#         result_list = result[0]
#         result_total_value_list = result[1]
        
        print('\n\n\n !DONE! \n\n\n')
        
        result_total_value_df = pd.DataFrame({"density_gps":result})
        print(result_total_value_df)
        result_total_value_df.to_csv(output_file)
        
# #         save as a numpy table
#         tb.printlist(result_total_value_list)
#         np.save(output_file, result_total_value_list)
#         
# #         save to file
#         tb.printlist(result_list)
#         tb.mywritelines2file(tb.mf_result_list_transfer(result_list), output_file)








if __name__ == '__main__': main()

