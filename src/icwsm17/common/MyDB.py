'''
Created on 14 Feb 2017

@author: vgong
'''
import psycopg2
from icwsm17.entity.DBSource import DBSource as DBS


class MyDB(object):
    '''
    classdocs
    '''
    
    def __init__(self, port='5432', dbname='icwsm17', user='postgres', host='localhost', password='postgres'):
        '''
        Constructor
        '''
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.port = port
        
        try:
            self.dbname = dbname
            self.connect_str = "dbname='{0}' user='{1}' host='{2}' password='{3}' port='{4}'".format(dbname, user, host, password, port)
            self.conn = psycopg2.connect(self.connect_str)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)
    
    
    @classmethod
    def from_dbs(cls, dbs):
        obj = cls(dbs.port, dbs.dbname, dbs.user, dbs.host, dbs.password)
        return obj
    
    def get_conn(self):
        return self.conn
    
    def get_cursor(self):
        return self.cursor
    
    def querydb(self, sql):
        try:
            rows = self.cursor.execute(sql)
            print('Affected: {0}. Returned len(rows): {1}'.format(self.cursor.rowcount, len(rows)))
    #         print(len(rows))
            return rows
        except Exception as e:
            print("Uh oh, can't query the db. Maybe invalid SQL.")
            print(e)

    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(e)


def main():
    print ("This only executes when %s is executed rather than imported" % __file__)

    dbs = DBS()
    mydb = MyDB.from_dbs(dbs)
    cursor = mydb.get_cursor()
    
    sql = 'SELECT * FROM case2sensor.v_cam_data_cell limit 5'
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    for i in range(0,len(rows)):
        print(rows[i])



if __name__ == '__main__': main()