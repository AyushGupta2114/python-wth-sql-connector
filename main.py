
from dbhelper import DBHelper

def main():
    db=DBHelper()   
    while True:
        print("*********WELCOME*********")
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter user id "))
                username=input("Enter username")
                userphone=input("Enter userphone")
                db.insert_user(uid,username,userphone)
            elif choice==2:
                #display user
                db.fetch_all()
                pass
            elif choice==3:
                userid=int(input("Enter userid to which you want to delete"))
                db.delete_user(userid)
                #delete user
            elif choice==4:
                uid=int(input("Enter user id of user to change "))
                username=input("new username")
                userphone=input("new userphone")
                db.update_user(uid,username,userphone)
                #update user
            elif choice==5:
                break
            else:
                print("Input invalid try again")
        except Exception as e:
            print(e)
            print("Invalid input USER try again ")


if __name__=='__main__':
    main()














# #main code
# helper=DBHelper()
# # helper.insert_user(1325,"Pooja","2225")
# # helper.insert_user(323,"Mohit","2125")
# # helper.insert_user(334,"Aman","2545")
# # helper.insert_user(534,"Piyush","2735")
# # helper.fetch_all()
# helper.update_user(1425,'Ankit','9506')
# helper.fetch_all()