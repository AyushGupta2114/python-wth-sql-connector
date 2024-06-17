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

    #Fetch all data
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User id :", row[0])
            print("User Name :", row[1])
            print("User Phone :", row[2])
            print("\n")
    def fetch_by_id(self,user_id):
        query="select userid,username,phone from user where userid={}".format(user_id)
        cur=self.con.cursor()
        cur.execute(query)
        row=cur.fetchone()
        print(row)
        if(row):
            print("User id :", row[0])
            print("User Name :", row[1])
            print("User Phone :", row[2])
            print("\n")
        else:
            print("NO road available")

    #delete useid
    def delete_user(self,userid):
        query="delete from user where userid={}".format(userid)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        print('deleted')
        self.con.commit()

    #update
    def update_user(self,userid,newName,newphone):
        query="update user set username='{}',phone='{}' where userid={}".format(newName,newphone,userid)
        print(query)
        s=self.con.cursor()
        s.execute(query)
        self.con.commit()
        print("updated")