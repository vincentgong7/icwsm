'''
Created on 18 Sep 2017

@author: vgong
'''
from icwsm17.entity.DBDetail import DBDetail as DBD

class DBSource(object):
    '''
    classdocs
    '''

    def __init__(self, dbname='icwsm17', user='postgres', host='localhost', password='postgres', port='9634', dbdetail=DBD()):
        '''
        Constructor
        '''
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.port = port
        self.dbdetail = dbdetail
    
    def set_detail(self, dbdetail):
        self.dbdetail = dbdetail      

    def get_conn_string(self):
        db_conn_str = "dbname='{0}' user='{1}' host='{2}' password='{3}' port='{4}'".format(self.dbname,self.user,self.host,self.password,self.port)
        return db_conn_str
