import mysql.connector
def insert(user_name,password):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="insert into users(user_name,password) values ('{0}','{1}')".format(user_name,password)
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Data Inserted Successfully.")
    cursor.close()

def delete(user_id):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query1="select * from users where user_id={0}".format(user_id)
    cursor=con.cursor()
    cursor.execute(query1)
    records=cursor.fetchone();
    if(records!=None):  
        query2="delete from users where user_id={0}".format(user_id)
        cursor=con.cursor()
        cursor.execute(query2)
        con.commit()
        print("Data Deleted!")
        cursor.close()
    else:
        print("Record Not Found")

def update(user_id,user_name,password):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="update users set user_name='{1}',password='{2}' where user_id='{0}'".format(user_id,user_name,password)
    cursor=con.cursor()
    cursor.execute(query)
    print(" Record Updated Successfully.")
    con.commit()
    cursor.close()

def get_all():
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="select * from users "
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    print("There are ",cursor.rowcount,"records in the table.")
    for row in records:
        print("Id:",row[0]),
        print("User Name:",row[1])
        print("Password:",row[2])
        print("--------------------------------")
    con.commit()
    cursor.close()

def search():
    user_name=input("Enter User Name: ")
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="select * from users where user_name like '%{0}%'".format(user_name)
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    if(cursor.rowcount==0):
        return -1;
    print("---------------------------------------------------------------------")
    for row in records:
        print("User Id:", row[0])
        print("User Name:", row[1])
        print("Password:", row[2])
        print("----------------------------------")
       
    con.commit()
    cursor.close()


def login():
    print("--------------LOGIN --------------")
    user_name=input("Enter User Name: ")
    password=input("Enter Password: ")
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="select * from users where user_name = '{0}' and password='{1}'".format(user_name,password)
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    if len(records)==0:
        return -1;
    else:
        return 1;
    cursor.close()
     
 
    
 
