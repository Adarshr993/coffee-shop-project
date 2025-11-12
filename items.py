import mysql.connector
def insert(item_name,mrp):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="insert into items(item_name,mrp) values ('{0}','{1}')".format(item_name,mrp)
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Data Inserted Successfully.")
    cursor.close()

def delete(item_id):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query1="select * from items where item_id={0}".format(item_id)
    cursor=con.cursor()
    cursor.execute(query1)
    records=cursor.fetchone();
    if(records!=None):  
        query2="delete from items where item_id={0}".format(item_id)
        cursor=con.cursor()
        cursor.execute(query2)
        con.commit()
        print("Data Deleted!")
        cursor.close()
    else:
        print("Record Not Found")

def update(item_id,item_name,mrp):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="update items set item_name='{1}',mrp='{2}' where item_id='{0}'".format(item_id,item_name,mrp)
    cursor=con.cursor()
    cursor.execute(query)
    print(" Record Successfully Updated.")
    con.commit()
    cursor.close()
 
def get_all():
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="select * from items "
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    for row in records:
        print("Item Id:",row[0])
        print("Item Name:",row[1])
        print("Mrp:",row[2])
        print("------------------------------------")
    con.commit()
    cursor.close()

def search():
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    item_name=input("Enter item name: ")
    query="select * from items where item_name like '%{0}%'".format(item_name)
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    for row in records:
        print("Id:",row[0]),
        print("Item Name:",row[1]),
        print("Mrp:",row[2])
        print("------------------------------------")
    con.commit()
    cursor.close()

