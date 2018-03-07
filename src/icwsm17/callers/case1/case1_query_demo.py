'''
Created on 6 Nov 2017

@author: vgong
'''

import icwsm17.callers.case1.case1_ep
from icwsm17.callers.case1.case1_ep import case1_ep
import icwsm17.mfs.toolbox as tb
from icwsm17.common.MyDB import MyDB
from icwsm17.entity.DBSource import DBSource as DBS
from icwsm17.entity.ExperimentProfile import ExperimentProfile as case2_ep

class demo_query(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def generate_sql(self):
        
        
    
        delta_ts = 30 * 60  # in seconds
        pedestrian_speed = 1.4  # the pedestrian speed is normally below 7.
        dist = pedestrian_speed * delta_ts
        
#  ---------- customize ---------       
        sql_fields = 'distinct userid, gender, age_level, age, uclass, venue_root_cat, post_content, ts, latitude, longitude '
        orderby_c= 'order by ts'
        
        case = 2
        cell_id = 1
        start_ts = 1461826800
        end_ts = 1461844800
    
#  ---------- customize ---------        
    
        if case == 1:
            cell_points_list = case1_ep.get_case1_ep().cell_points_list
        elif case == 2:
            cell_points_list = case2_ep().cell_points_list
            
        cell_id = cell_id - 1
        for sql_table_name in ['vincent.vg_twitter_geo_is_data_user_poi', 'vincent.vg_twitter_geo_is_data_user_poi']:
            print("The cell_id:{}".format(cell_id))
            print(cell_points_list[cell_id])
            
            '''extend the location of each cell'''
            extended_cell = tb.cell_extend(cell_points_list[cell_id], dist)
            print(extended_cell)
    
            '''generate sql'''
            
            area_str = tb.transfer_coords(extended_cell)
            sql = "SELECT {} FROM {} as t1 where {} <= t1.ts and t1.ts <={} and ST_Within(ST_MakePoint(t1.longitude, t1.latitude),ST_GeomFromText('POLYGON(({}))')) {};".format(sql_fields, sql_table_name, start_ts, end_ts, area_str, orderby_c)
            print("sql")
            print(sql)
    
    
    def query_age_level(self):
        
#         dbs = DBS(dbname='sail_db', user='postgres', host='localhost', password='postgres', port='9636')
        dbs = DBS(dbname='kings2016_db', user='postgres', host='localhost', password='postgres', port='9636')
        
        mydb = MyDB.from_dbs(dbs)
        cursor = mydb.get_cursor()
        
        
#         for v_id in [1,2,3,4,5,9,10,11,12,13,14,6,7,8,15]:
        for v_id in [16,17,18,19]:
            
            re_dic = {}
            
            for platform in ['twitter', 'inst']: 
                
                sql = 'SELECT  age_level, count(distinct userid) FROM vincent.v_{}_{} group by age_level'.format(v_id, platform)
                cursor.execute(sql)
                rows = cursor.fetchall()
                
                for i in range(0,len(rows)):
#                     print("{}:{}".format(rows[i][0],rows[i][1]))
                    if rows[i][0] in re_dic:
                        re_dic[rows[i][0]] = rows[i][1] + re_dic[rows[i][0]]
                    else:
                        re_dic[rows[i][0]] = rows[i][1]
                
            print()
            print()
            print("------View_id: {}".format(v_id))    
            
            if 'young' in re_dic: 
                print("young: {}".format(re_dic['young']))
            else: print("young: 0")
                
            if 'young-adult' in re_dic: 
                print("young-adult: {}".format(re_dic['young-adult']))
            else: print("young-adult: 0")
                
            if 'adult' in re_dic: 
                print("adult: {}".format(re_dic['adult']))
            else: print("adult: 0")
                
            if 'old' in re_dic: 
                print("old: {}".format(re_dic['old']))
            else: print("old: 0")
                    
        cursor.close()


    def query_gender(self):
        
#         dbs = DBS(dbname='sail_db', user='postgres', host='localhost', password='postgres', port='9636')
        dbs = DBS(dbname='kings2016_db', user='postgres', host='localhost', password='postgres', port='9636')

        mydb = MyDB.from_dbs(dbs)
        cursor = mydb.get_cursor()
        
#         for v_id in [1,2,3,4,5,9,10,11,12,13,14,6,7,8,15]:
        for v_id in [16,17,18,19]:
            re_dic = {}
            
            for platform in ['twitter', 'inst']: 
                
                sql = 'SELECT  gender, count(distinct userid) FROM vincent.v_{}_{} group by gender'.format(v_id, platform)
                cursor.execute(sql)
                rows = cursor.fetchall()
                
                for i in range(0,len(rows)):
#                     print("{}:{}".format(rows[i][0],rows[i][1]))
                    if rows[i][0] in re_dic:
                        re_dic[rows[i][0]] = rows[i][1] + re_dic[rows[i][0]]
                    else:
                        re_dic[rows[i][0]] = rows[i][1]
                
            print()
            print()
            print("------View_id: {}".format(v_id))    
            
            if 'Male' in re_dic:
                print("Male: {}".format(re_dic['Male']))
            else: print("Male: 0")
                
            if 'Female' in re_dic: 
                print("Female: {}".format(re_dic['Female']))
            else: print("Female: 0")
                    
        cursor.close()
        

    def query_role(self):
        
#         dbs = DBS(dbname='sail_db', user='postgres', host='localhost', password='postgres', port='9636')
        dbs = DBS(dbname='kings2016_db', user='postgres', host='localhost', password='postgres', port='9636')
        
        mydb = MyDB.from_dbs(dbs)
        cursor = mydb.get_cursor()
        
        
#         for v_id in [1,2,3,4,5,9,10,11,12,13,14,6,7,8,15]:
        for v_id in [16,17,18,19]:
            
            re_dic = {}
            
            for platform in ['twitter', 'inst']: 
                
                sql = 'SELECT uclass, count(distinct userid) FROM vincent.v_{}_{} group by uclass'.format(v_id, platform)
#                 print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                
                for i in range(0,len(rows)):
#                     print("{}:{}".format(rows[i][0],rows[i][1]))
                    if rows[i][0] in re_dic:
                        re_dic[rows[i][0]] = rows[i][1] + re_dic[rows[i][0]]
                    else:
                        re_dic[rows[i][0]] = rows[i][1]
                
            print()
            print()
            print("------View_id: {}".format(v_id))    
            
            if 'RESIDENT' in re_dic: 
                print("RESIDENT: {}".format(re_dic['RESIDENT']))
            else: print("RESIDENT: 0")
                
            if 'LOCAL_TOURIST' in re_dic: 
                print("LOCAL_TOURIST: {}".format(re_dic['LOCAL_TOURIST']))
            else: print("LOCAL_TOURIST: 0")
                
            if 'FOREIGN_TOURIST' in re_dic: 
                print("FOREIGN_TOURIST: {}".format(re_dic['FOREIGN_TOURIST']))
            else: print("FOREIGN_TOURIST: 0")
                
        cursor.close()


    def query_poi(self):
        
#         dbs = DBS(dbname='sail_db', user='postgres', host='localhost', password='postgres', port='9636')
        dbs = DBS(dbname='kings2016_db', user='postgres', host='localhost', password='postgres', port='9636')
        
        mydb = MyDB.from_dbs(dbs)
        cursor = mydb.get_cursor()
        
        
#         for v_id in [1,2,3,4,5,9,10,11,12,13,14,6,7,8,15]:
        for v_id in [16,17,18,19]:
            
            re_dic = {}
            
            print()
            print()
            print("------View_id: {}".format(v_id))
            for platform in ['twitter', 'inst']: 
                
                sql = 'SELECT venue_root_cat, count(distinct userid) sum FROM vincent.v_{}_{} group by venue_root_cat order by sum desc'.format(v_id, platform)
#                 print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                
                for i in range(0,len(rows)):
#                     print("{}:{}".format(rows[i][0],rows[i][1]))
                    if rows[i][0] in re_dic:
                        re_dic[rows[i][0]] = rows[i][1] + re_dic[rows[i][0]]
                    else:
                        re_dic[rows[i][0]] = rows[i][1]
                
                print()
                
                for i in range(0,4):
                    print("{}:{}".format(rows[i][0],rows[i][1]))

        cursor.close()


        
def main():
    
    dq = demo_query()
    
#     dq.generate_sql()
#     dq.query_gender()
#     dq.query_age_level()
#     dq.query_role()
    dq.query_poi()



    
    
    



if __name__ == '__main__': main()    
