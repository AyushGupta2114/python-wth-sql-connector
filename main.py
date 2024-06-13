import mysql.connector as connector

# con = connector.connect(
#     host='localhost',
#     port='3306',
#     user='root',
#     password='123456',  
#     database='pythontest'
# )

# print(con)

class DBHelper:
    def __init__(self):
        self.con=connector.connect(
                        host='localhost',
                        port='3306',
                        user='root',
                        password='123456',  
                        database='pythontest'
                    )
        query='create table if not exists user(userId int primary key,userName varchar(300),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

#main code
helper=DBHelper()