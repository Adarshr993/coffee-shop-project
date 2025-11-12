import mysql.connector
def insert(bill_master_id,item_id,qty,price):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="insert into bill_details(bill_master_id,item_id,qty,price) values ('{0}','{1}',{2},{3})".format(bill_master_id,item_id,qty,price)
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    print("Item Inserted Succsssfully")
    

def delete(bill_master_id):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query2="delete from bill_details where bill_master_id={0}".format(bill_master_id)
    cursor=con.cursor()
    cursor.execute(query2)
    con.commit()
    cursor.close()


