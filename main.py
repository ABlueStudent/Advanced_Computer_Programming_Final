from playUSpider import *
from DBInterface import *
from DataAnalysis import *
from datetime import datetime

if __name__ == "__main__":
    playU = playUSpider()
    playU = playU.contentList()
    DBInterface = DBInterface()
    DataAnalysis = DataAnalysis()

    # get something on PlayU and put into DataPack. by.可愛的下畫線亞裔黑白相間的熊
    for item in playU:
        DBInterface.storeContent(item.get('title'), item.get('description'), datetime.strptime(item.get('date'), '%B %d, %Y'), item.get('readtime'))

    print(DBInterface.getContent())