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

    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('User saved to db')

#main code
helper=DBHelper()
helper.insert_user(1325,"Pooja","2225")
helper.insert_user(323,"Mohit","2125")
helper.insert_user(334,"Aman","2545")
helper.insert_user(534,"Piyush","2735")