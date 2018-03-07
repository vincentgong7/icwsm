'''
Created on 1 Nov 2017

@author: vgong
'''
from icwsm17.entity.DBSource import DBSource as DBS
from icwsm17.common.MyDB import MyDB
import pandas as pd


class query_wifi(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        dbs = DBS()
        self.mydb = MyDB.from_dbs(dbs)
        
    def ask(self, sql):
        cursor = self.mydb.get_cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        return rows

def main():
    print ("This only executes when %s is executed rather than imported" % __file__)

    query = query_wifi()
    

    folder = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/1101-v1/case1-algorithm/tem_data/wifi"
    
    for cell_id in range(1, 5):
        
        print("Woring on cell_{}......".format(cell_id))
        
        sql = "SELECT a_ts_hour, count(id) as total FROM case1sensor.v_wifi_data_ready where cell_id = {} and flow_direction = '->' group by a_ts_hour".format(cell_id) 
        
#         first section:
#         ----------------------------------
        direction = '->'
    
        ts_hour = 'a_ts_hour'
        sql = "SELECT {}, count(id) as total FROM case1sensor.v_wifi_data_ready where cell_id = {} and flow_direction = '{}' group by {}".format(ts_hour, cell_id, direction, ts_hour)
        rows = query.ask(sql)
        
        labels = ['ts_hour', 'total']
        df = pd.DataFrame.from_records(rows, columns=labels)
        
        filename = "cell_{}_left_in".format(cell_id)
        df.to_csv("{}/{}".format(folder, filename))
        

        ts_hour = 'b_ts_hour'
        sql = "SELECT {}, count(id) as total FROM case1sensor.v_wifi_data_ready where cell_id = {} and flow_direction = '{}' group by {}".format(ts_hour, cell_id, direction, ts_hour)
        rows = query.ask(sql)
        
        labels = ['ts_hour', 'total']
        df = pd.DataFrame.from_records(rows, columns=labels)
        
        filename = "cell_{}_right_out".format(cell_id)
        df.to_csv("{}/{}".format(folder, filename))

#         ----------------------------

#         second section:
#         ----------------------------------
        direction = '<-'
    
        ts_hour = 'a_ts_hour'
        sql = "SELECT {}, count(id) as total FROM case1sensor.v_wifi_data_ready where cell_id = {} and flow_direction = '{}' group by {}".format(ts_hour, cell_id, direction, ts_hour)
        rows = query.ask(sql)
        
        labels = ['ts_hour', 'total']
        df = pd.DataFrame.from_records(rows, columns=labels)
        
        filename = "cell_{}_right_in".format(cell_id)
        df.to_csv("{}/{}".format(folder, filename))
        

        ts_hour = 'b_ts_hour'
        sql = "SELECT {}, count(id) as total FROM case1sensor.v_wifi_data_ready where cell_id = {} and flow_direction = '{}' group by {}".format(ts_hour, cell_id, direction, ts_hour)
        rows = query.ask(sql)
        
        labels = ['ts_hour', 'total']
        df = pd.DataFrame.from_records(rows, columns=labels)
        
        filename = "cell_{}_left_out".format(cell_id)
        df.to_csv("{}/{}".format(folder, filename))

#         ----------------------------

    print("Done!")

if __name__ == '__main__': main()