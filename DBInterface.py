import pymysql.cursors

class DBInterface():
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'password'
        self.db_name = 'db_108021063'
        self.table_name = 'table_108021063'
        self.charset = 'utf8mb4'
        self.connect = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            # db = self.db_name,
            charset = self.charset,
            cursorclass = pymysql.cursors.DictCursor
        )
        self.checked = False

    def check_db_and_table(self):
        try:
            with self.connect.cursor() as cursor:
                # 檢查有沒有對應的DataBase 沒有的話就建一個
                cursor.execute('SHOW DATABASES;')
                if len(list(filter(lambda database: database.get('Database') == self.db_name, cursor.fetchall()))) < 1:
                    cursor.execute('CREATE DATABASE {} CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;'.format(self.db_name))
                    print('created database ', self.db_name)

                cursor.execute('SHOW DATABASES;')
                db_list = cursor.fetchall()

                # 使用剛建立的Database
                cursor.execute('USE {};'.format(self.db_name))

                # 檢查有沒有對應的Table 沒有的話建立一個
                cursor.execute('SHOW TABLES;')
                if len(list(filter(lambda table: table.get('Tables_in_{}'.format(self.db_name)) == self.table_name, cursor.fetchall()))) < 1:
                    cursor.execute(
                        'CREATE TABLE {} (ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, Title TEXT NOT NULL, Description TEXT , Date TEXT , ReadTime TEXT);'.format(self.table_name))
                    print('created table ', self.table_name)

                cursor.execute('SHOW TABLES;')
                table_list = cursor.fetchall()
                
                return [db_list, table_list, True]
        except:
            return False

        finally:
            # self.connect.close()
            self.checked = True

    def storeContent(self, Title, Description, Date, ReadTime):
        if self.checked == False:
            self.check_db_and_table()

        try:
            with self.connect.cursor() as cursor:
                cursor.execute('USE {};'.format(self.db_name))
                cursor.execute('INSERT INTO {} (Title, Description, Date, ReadTime) VALUES(%s, %s, %s, %s);'.format(self.table_name), (Title, Description, Date, ReadTime))
                
            return True

        except:
            return False
        finally:
            self.connect.commit()
        
    def getContent(self):
        pass

    def close(self):
        self.connect.commit()
        self.connect.close()