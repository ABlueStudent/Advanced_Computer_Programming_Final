import matplotlib.pyplot as plt
import pandas
import pymysql
import time

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

    def pandaEatData(self):
        dataFromSQL = pandas.read_sql('SELECT * FROM {}'.format(self.table_name), self.connect)
        sortedData = dataFromSQL.sort_values(by = ['Date'], ascending = False)
        return sortedData

    def andlyseReadtime(self):
        with self.connect.cursor() as cursor:
            cursor.execute('SELECT ReadTime FROM {}'.format(self.table_name))
            rawData = cursor.fetchall()
            Data = map(lambda item: item.get('ReadTime').split(' ')[0], rawData)
            Data = map(lambda item: int(item), Data)
            Data = list(Data)

            x = list()
            y = list()

            for Int in range(0, max(Data)+2):
                x.append(Int)
                y.append(Data.count(Int))

            plt.bar(x, y)
            plt.xlabel('Read Time')
            plt.ylabel('Count')
            plt.yticks([ytick for ytick in range(0, max(y)+2)])
            plt.savefig("{}.png".format(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())))

            return Data