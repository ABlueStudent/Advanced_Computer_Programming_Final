from playUSpider import *
from DBInterface import *

if __name__ == "__main__":
    # playU = playUSpider()
    # print(playU.contentList())
    
    # DBInterface = DBInterface()
    # print(DBInterface.storeContent('Good Morning!', 'Just OwO 而已', '2020/06/29', '0 min'))
    # DBInterface.close()

    playU = playUSpider()
    playU = playU.contentList()
    DBInterface = DBInterface()

    for item in playU:
        DBInterface.storeContent(item.get('title'), item.get('description'), item.get('date'), item.get('readtime'))

    