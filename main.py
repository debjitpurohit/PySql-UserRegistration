import mysql.connector
import random
import string

def adduser(connection , cur):
    uname = input("enter your name :")
    uAge = int(input("enter your Age:"))
    ucon = int(input("enter your Contact Number :"))
    umail = input("enter your Email:")
    upass = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    query= "insert into usertable (Name ,Age,Contact,Email , Password) values(%s,%s,%s,%s,%s)"
    value= (uname, uAge, ucon,umail, upass)
    cur.execute(query, value)
    connection.commit()
    print("User Successfully added")

    print("------------------")
    print("user Details:")
    print("------------------")
    print("User Name :", uname);
    print("User Age :", uAge);
    print("User contact number  :", ucon);
    print("Email :", umail)
    print("password :", upass)

#user deletation
def deleteuser(connection,cur):
    uname = input("Enter Name Details which you delete :")
    query = "Delete from usertable where Name = %s"
    value = (uname,)
    cur.execute(query, value)
    connection.commit()
    print(cur.rowcount, "record Deleted.")

#user updatation
def updateuser(connection , cur):
    uname = input("Enter Name where u want to update")
    print("which value u wanna change")
    print("1. Name ")
    print("2 . Contact Number")
    print("3. Age")
    print("4. Email")
    chng=int(input("Which value u want to update "))
    if(chng==2):
        chngcnct= int(input("enter your new Contact Number :"))
        query = "update usertable set Contact= %s where Name= %s ; "
        value = (chngcnct,uname)
        cur.execute(query, value)
        connection.commit()
        print(cur.rowcount, "contact number updated.")
    elif(chng==1):
        chngcnct= input("enter your new Name :")
        query = "update usertable set Name= %s where Name= %s ; "
        value = (chngcnct,uname)
        cur.execute(query, value)
        connection.commit()
        print(cur.rowcount, "name updated.")
    elif(chng==3):
        chngcnct= int(input("enter your new Age :"))
        query = "update usertable set Age= %s where Name= %s ; "
        value = (chngcnct,uname)
        cur.execute(query, value)
        connection.commit()
        print(cur.rowcount, "Age updated.")
    elif(chng==4):
        chngcnct= input("enter your new Email :")
        query = "update usertable set Email= %s where Name= %s ; "
        value = (chngcnct,uname)
        cur.execute(query, value)
        connection.commit()
        print(cur.rowcount, "Mail updated.")
    else:
        print("U entered wrong details")
#python to mysql connection
def main():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user"
    )
    cur=connection.cursor()
    if(cur):
        print("database connection established successfully")
        choice = 0
        while choice <= 3:
            print("1.User Registration")
            print("2.Delete User")
            print("3. Update user")
            print("4.Exit application")
            print("\n-----------------")
            choice = int(input("choose your Demand :"))
            if (choice == 1):
                print("Enter Your Details")
                adduser(connection, cur)
            elif(choice==2):
                deleteuser(connection,cur)

            elif(choice==3):
                updateuser(connection,cur)
            else:
                print("Thanks for visiting us")
                exit()

    else:
        print("Databse connection not establissed")
main()
