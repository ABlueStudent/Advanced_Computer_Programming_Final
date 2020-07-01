import matplotlib.pyplot as plt
import pandas
import pymysql

from DBInterface import *

class DataAnalysis(DBInterface):
    def __init__(self):
        super(DataAnalysis, self).__init__() # call father init
        
        self.connect = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.db_name,
            charset = self.charset,
            cursorclass = pymysql.cursors.DictCursor
        )

