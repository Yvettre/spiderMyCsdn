# coding=utf-8

import logging
import pymysql
import pandas as pd
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('./config/config.ini')

user = config.get('mysql', 'user')
passwd = config.get('mysql', 'passwd')
database = config.get('mysql', 'database')
logger_name = config.get('logger', 'logger_name')

logger = logging.getLogger(logger_name)

class Mysql(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", user, passwd, database)
        self.cursor = self.db.cursor()
    
    def insert_data(self, table_name, data):
        if isinstance(data, dict):
            tmp_keys = '(' + ','.join(data.keys()) + ')'
            tmp_values = '(' + ','.join(data.values()) + ')'
            sql = 'insert into %s %s values %s' %(table_name, tmp_keys, tmp_values)
        elif isinstance(data, pd.DataFrame):
            pass
        else:
            logger.error('Inserting DATA is not a dictionary or a dataframe.')
            return
        
        try:
            self.cursor.execute(sql)
            self.db.commit()
            logger.info('Sucessfully insert data into table(%s).' %table_name)
        except Exception, e:
            logger.error(e)
            logger.error('Fail to insert data into table(%s).' %table_name)
            self.db.rollback()
            return

    def __del__(self):
        self.db.close()
        logger.debug('Deleted object mysql.')

    # def create_table(self, table_name, keys, data_types):
    #     if len(keys) != len(data_types):
    #         logger.error('length of KEYS is not equal to length of DATA_TYPES.')
    #         return
        
    #     pair = zip(keys, data_types)
    #     tmp = []
    #     for item in pair:
    #         tmp.append('%s %s'%(item[0], item[1]))
    #     tmp = str(tuple(tmp))

    #     sql = 'create table if not exists %s %s'%(table_name, tmp)
    #     try:
    #         self.cursor.execute(sql)
    #         logger.info('Sucessfully create table(%s)!'%table_name)
    #     except Exception,e:
    #         logger.error(e)
    #         logger.error('Fail to create table(%s)'%table_name)
    #         return
    

    # def drop_table(self, table_name):
    #     sql = 'drop table if exists %s'%table_name
    #     try:
    #         self.cursor.execute(sql)
    #         logger.info('Sucessfully drop table(%s).'%table_name)
    #     except Exception,e:
    #         logger.error(e)
    #         logger.error('Fail to drop table(%s).'%table_name)
    #         return