import mysql.connector
def insert(customer_name,address,phone_no):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="insert into customers(customer_name,address,phone_no) values ('{0}','{1}','{2}')".format(customer_name,address,phone_no)
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Data Inserted Successfully.")
    cursor.close()

def delete(customer_id):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query1="select * from customers where customer_id={0}".format(customer_id)
    cursor=con.cursor()
    cursor.execute(query1)
    records=cursor.fetchone();
    if(records!=None):  
        query2="delete from customers where customer_id={0}".format(customer_id)
        cursor=con.cursor()
        cursor.execute(query2)
        con.commit()
        print("Data Deleted!")
        cursor.close()
    else:
        print("Record Not Found")

def update(customer_id,customer_name,address,phone_no):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="update customers set customer_name='{1}',address='{2}',phone_no='{3}' where customer_id='{0}'".format(customer_id,customer_name,address,phone_no)
    cursor=con.cursor()
    cursor.execute(query)
    print(" Record Successfully Updated.")
    con.commit()
    cursor.close()

def get_all():
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="select * from customers "
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    for row in records:
        print("Id:",row[0])
        print("Customer Name:",row[1])
        print("Address:",row[2])
        print("Phone No:",row[3])
        print("------------------------------------")
    con.commit()
    cursor.close()

def search():
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    customer_name=input("Enter Customer Name: ")
    query="select * from customers where customer_name like '%{0}%'".format(customer_name)
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    if  (len(records)==0):
        print("No Record Found. Please Search Again")
        search()
    for row in records:
        print("Id:",row[0])
        print("Customer Name:",row[1])
        print("Address:",row[2])
        print("Phone no:",row[3])
        print("------------------------------------")
    con.commit()
    cursor.close()

    
