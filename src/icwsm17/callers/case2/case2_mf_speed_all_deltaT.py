'''
Created on 31 May 2017

@author: vgong
'''
import sys
import pandas as pd
sys.path.append('/root/case2/socialmedia/')

# import icwsm17.mfs.cell_profile as cp
import icwsm17.mfs.toolbox as tb
import icwsm17.common.extendarea as exarea
# import psycopg2
import scipy.stats
import numpy as np
from icwsm17.mfs.MF_basic import MF_basic
from icwsm17.common.MyDB import MyDB
from icwsm17.entity.DBSource import DBSource as DBS
from icwsm17.entity.ExperimentProfile import ExperimentProfile as EP
from icwsm17.mfs.MF_probability import MF_probability

class case2_mf_probability(object):
    '''
    classdocs
    '''


    def __init__(self, port='9634', dbname='icwsm17', username = 'postgres', host = 'localhost', password = 'postgres', twitter_table='case2smd.v_twitter_geo_is', inst_table='case2smd.v_inst_geo_is', dbs=DBS(), ep=EP()):
        '''
        Constructor
        '''
#         self.dbname = dbname
#         self.port = port
#         self.username = username
#         self.password = password
#         self.host = host
#         self.twitter_table = twitter_table
#         self.inst_table = inst_table
#         self.bin_ts = 60 * 60  # the bin timestamp size, here per hour
#         self.mydb = MyDB(port, dbname, username, host, password)
#         self.ep = ep
#         
#         self.mf_basic = MF_basic(port)
        
        
#     @classmethod
#     def from_dbs_ep(cls, dbs, ep):
#         obj = cls(dbs.port, dbs.dbname, dbs.user, dbs.host, dbs.password, dbs.dbdetail.twitter_table, dbs.dbdetail.inst_table, dbs, ep)
#         return obj
#     
#     #  this one is only used to calculate np_user, and export demographic data
#     def mf_prob_crawl_user(self, platform, area_cell_coord_list, start_ts, end_ts, orderby_c, conn):
#         
#     #     cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise
#     #     area_str = '4.898841 52.380853,4.907432 52.378196,4.906678 52.377343,4.898109 52.380259,4.898841 52.380853'
#         area_str = tb.transfer_coords(area_cell_coord_list)   
#         
# #         sql_fields = 'distinct userid, id, ts, latitude, longitude, gender, age, uclass '
#         sql_fields = 'distinct uid, ts_linux, lat, lon '
# #         sql_table_name = 'public.{}_geo_is_data_user'.format(platform)
#         
#         if platform == 'twitter':
#             sql_table_name = self.twitter_table
#         else:
#             sql_table_name = self.inst_table
#         
#         sql = "SELECT {} FROM {} as t1 where {} <= t1.ts_linux and t1.ts_linux <={} and ST_Within(ST_MakePoint(t1.lon, t1.lat),ST_GeomFromText('POLYGON(({}))')) {};".format(sql_fields, sql_table_name, start_ts, end_ts, area_str, orderby_c)
#         
# #         print(sql)
#         cursor = conn.cursor()
#         cursor.execute(sql)
#         rows = cursor.fetchall()
# #         cursor.close()
#         
#         return rows
#     
#     
#     def mf3v2_mf_np_users_direction(self, platform, timeing, direction, cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, norm_dis_scale, conn):
#         
#         cell = self.ep.cell_points_list[cell_id]
#         
#         if direction == 'left':
#             area = tb.cell_b1_extend_area(cell, max_length)
#         elif direction == 'right':
#             area = tb.cell_b2_extend_area(cell, max_length)
#         elif direction == 'bidirection':
#             area = tb.cell_b1b2_extend(cell, max_length)
#         elif direction == 'radiation':
#             area = tb.cell_extend(cell, max_length)
#         else:
#             area = tb.cell_extend(cell, max_length)    
#        
#         
#         if timeing == 'before':
#             rows = self.mf_prob_crawl_user(platform, area, start_ts - prior_ts, start_ts, 'order by ts_linux desc', conn)
#         else:  # timeing == 'after'
#             rows = self.mf_prob_crawl_user(platform, area, end_ts, end_ts + extra_ts, 'order by ts_linux', conn)
#         
#     #     print('number of posts (rows) got: {}'.format(len(rows)))
#     
#         r = self.ep.cell_half_length[cell_id]
#         norm_p = scipy.stats.norm(r, norm_dis_scale)
#     
#         result = 0
#         for row in rows:
#     #         [(634399970880323584, 914877410, 1440094914, 52.378458, 4.906394),
#     #          (634399970880323584, 914877410, 1440094914, 52.378458, 4.906394)]
#     
#     #         print(row)
#             
#             dist = tb.calculate_distance(row[3], row[2], self.ep.cell_points_list[cell_id])  # par: x, y, cell_id
#             dist = dist - r
# #             if dist < 0: dist = 0  # assume that posts which are in the terrain will be stay there
#             
#     #         print(dist)
#             prob = norm_p.cdf(dist)
#     #         print('prob: {}'.format(prob))
#             result = result + prob
#     #     print(result)
#         return result
#     
    
    
#     def call_membership_fun_probability(self, cell_id, record_start_ts, record_end_ts, bin_ts, delta_t_ts, max_length):
#         print('Start membership function Probability.')
#         
# #         db_conn_str = "dbname='{0}' user='{1}' host='{2}' password='{3}' port='{4}'".format(self.dbname, self.username, self.host, self.password, self.port)
# #         conn = psycopg2.connect(db_conn_str)
#         conn = self.mydb.get_conn()
#         #     cell_id = 0 # 0-3 = cell 1-4
# #     record_start_ts = date2ts('2015-08-19 00:00:01') 
# #     record_end_ts = date2ts('2015-08-22 23:59:59')
#         
#         prior_ts = delta_t_ts
#         extra_ts = delta_t_ts
#         
#         all_sequence_list = []
#         all_before_list = []
#         all_after_list = []
#         all_base_list = []
#         all_total_list = []
#         
#         for i in range(0, round((record_end_ts - record_start_ts) / bin_ts)):
#             start_ts = record_start_ts + i * bin_ts
#             end_ts = record_start_ts + (i + 1) * bin_ts
#             
#             print("----------------------------Time:{}----------------------------".format(i))
#             
#             
#         #       correctly considering timing, and platform -------start------------------------------------
# #         direction: left, right, bidirection, radiation 
#             
#             twitter_before = self.mf3v2_mf_np_users_direction('twitter', 'before', 'radiation', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length / 3, conn)
#             twitter_after = self.mf3v2_mf_np_users_direction('twitter', 'after', 'radiation', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length / 3, conn)       
#             inst_before = self.mf3v2_mf_np_users_direction('inst', 'before', 'radiation', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length / 3, conn)
#             inst_after = self.mf3v2_mf_np_users_direction('inst', 'after', 'radiation', cell_id, start_ts, end_ts, prior_ts, extra_ts, max_length, max_length / 3, conn)
# 
# 
# #         based on MF_gps, which is MF_basic with extend --- start
# #             cell_coord_list = exarea.cell_b1b2_extend(cp.cell_points_list[cell_id], 113)
#             cell_coord_list = exarea.cell_b1b2_extend(self.ep.cell_points_list[cell_id], 113)
#             
#             twitter_before_redundant = self.mf_basic.membership_fun_basic_twitter(cell_coord_list, start_ts, end_ts, conn)
#             twitter_after_redundant = self.mf_basic.membership_fun_basic_twitter(cell_coord_list, end_ts, end_ts + extra_ts, conn)
#             inst_before_redundant = self.mf_basic.membership_fun_basic_inst(cell_coord_list, start_ts - prior_ts, start_ts, conn)
#             inst_after_redundant = self.mf_basic.membership_fun_basic_inst(cell_coord_list, end_ts, end_ts + extra_ts, conn)
#         
#             twitter_mf_base = self.mf_basic.membership_fun_basic_twitter(cell_coord_list, start_ts, end_ts, conn)
#             inst_mf_base = self.mf_basic.membership_fun_basic_inst(cell_coord_list, start_ts, end_ts, conn)
# 
# #         based on MF_gps --- end
# 
# # sum-up result   
#             all_before = twitter_before + inst_before - twitter_before_redundant - inst_before_redundant
#             all_after = twitter_after + inst_after - twitter_after_redundant - inst_after_redundant
#             all_base = twitter_mf_base + inst_mf_base
#             
#             all_total = all_before + all_after + all_base
# #             print(all_total)
#             
#             all_sequence_list.append(i)
#             all_before_list.append(all_before)
#             all_after_list.append(all_after)
#             all_base_list.append(all_base)
#             all_total_list.append(all_total)
#         
# #         sm_cell_flow_list = [np.asarray(all_sequence_list), np.asarray(all_before_list), np.asarray(all_after_list), np.asarray(all_base_list), np.asarray(all_total_list)]
#         sm_cell_flow_list = [np.asarray(all_before_list), np.asarray(all_after_list), np.asarray(all_base_list), np.asarray(all_total_list)]
#         sm_cell_flow_array = np.asarray(sm_cell_flow_list)
#         sm_cell_flow_array = np.transpose(sm_cell_flow_array)
#         return sm_cell_flow_array
# #       correctly considering timming, and platform -------end------------------------------------  
            

def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    case = "case2"
    strategy_suffix = 'probability'
    port = 9634
    outputfolder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1'
    outputfolder = "{}/{}/mf_speed_all_deltaT".format(outputfolder,case)
#     port = 5432
#     outputfolder = '/root/case2/socialmedia/result/0531-v1'

    
    mf_strategy = MF_probability(port)
    
    delta_tm = 30
    
    
    '''When only run for delta_t = 30'''
#     for delta_tm in range(30,31):
    '''When run for delta_t = 5,10,15,20,25,30,35,40,45,50,55,60'''
    speed_density_all_df = pd.DataFrame()
    
    for delta_tm in range(5,65,5):
    
        for cell_id in range(0, 1):
        # cell_id = 1 # 0-3 = cell 1-4
        
            '''for Mf_prob'''
            extra_out_put_flag = '' 
            bin_ts = 60*60  # the bin timestamp size, here per hour, in seconds
            
            delta_ts = delta_tm*60  # in seconds
            record_start_ts = tb.date2ts('2016-04-26 00:00:00') 
            record_end_ts = tb.date2ts('2016-04-29 00:00:00')
    
            '''for "before"'''
    #         extra_out_put_flag = '_before' 
    #         bin_ts = 60*60  # the bin timestamp size, here per hour, in seconds
    #         delta_ts = 60*60  # in seconds
    #         record_start_ts = tb.date2ts('2016-04-26 01:00:00') 
    #         record_end_ts = tb.date2ts('2016-04-29 01:00:00')
            
            '''for "after"'''
    #         extra_out_put_flag = '_after' 
    #         bin_ts = 60*60  # the bin timestamp size, here per hour, in seconds
    #         delta_ts = 60*60  # in seconds
    #         record_start_ts = tb.date2ts('2016-04-25 23:00:00') 
    #         record_end_ts = tb.date2ts('2016-04-28 23:00:00')
    
    
            # cell_id, record_start_ts, record_end_ts
            
            output_file = '{}/mf_{}_cell_{}{}_deltaT_{}.txt'.format(outputfolder, strategy_suffix, cell_id, extra_out_put_flag, delta_tm)
            pedestrian_speed = 1.40 # the pedestrian speed is normally below 7.
            max_length = pedestrian_speed * delta_ts  # e.g. 7 * (30*60), delta_t_ts is in seconds
            result_list = mf_strategy.call_membership_fun_probability(cell_id, record_start_ts, record_end_ts, bin_ts, delta_ts, max_length)
            print('\n\n\n !DONE! \n\n\n')
            
            
            '''save as a pandas DataFrame'''
            result_df = pd.DataFrame(result_list,columns=['before', 'after', 'basis', 'total', 'total_density'])
            result_df.to_csv(output_file)
            
            col_name = "mf_speed_{}".format(delta_tm)
            total_density_values = result_df["total_density"].values
            
            speed_density_all_df[col_name] = total_density_values
            
    #         save as a numpy table
    #         tb.printlist(result_list[2])
    #         result_array = np.asarray(result_list)
    #         
    #         result_list = [sequence, before, after, basis, total]
            '''modify based on function'''
    #         np.save(output_file, result_array)
    #         result_array = np.transpose(result_array)
            
    #         save to file
    #         tb.printlist(result_list[0])
    #         tb.mywritelines2file(tb.mf_prob_result_list_transfer(result_array), output_file)
    
    speed_density_all_df.to_csv(outputfolder + "/mf_speed_all.txt")
    
        

if __name__ == '__main__': main()
