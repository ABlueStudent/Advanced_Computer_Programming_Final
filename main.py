import pandas
import time

from playUSpider import *
from DBInterface import *
from DataAnalysis import *
from datetime import datetime

if __name__ == "__main__":
    playU = playUSpider()
    playU = playU.contentList()
    DBInterface = DBInterface()

    # 補上忘記跑的檢查資料庫的部分
    DBInterface.check_db_and_table()

    DataAnalysis = DataAnalysis()

    # get something on PlayU and put into DataPack. by.可愛的下畫線亞裔黑白相間的熊
    for item in playU:
        DBInterface.storeContent(item.get('title'), item.get('description'), datetime.strptime(item.get('date'), '%B %d, %Y'), item.get('readtime'))

    # 把東西全都Print到Console上

    # print(DBInterface.getContent()) # SELECT * FROM table_

    # print(DataAnalysis.pandaEatData()) # pandas parsed table_

    # print(DataAnalysis.andlyseReadtime())

    # 來正經的做資料輸出

    pandaEatData = DataAnalysis.pandaEatData()
    analyseReadTime = DataAnalysis.andlyseReadtime()

    pandaEatData.to_csv("{}.csv".format(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())))
    print(pandaEatData)

    print("Readtime Data list: ", analyseReadTime)

    