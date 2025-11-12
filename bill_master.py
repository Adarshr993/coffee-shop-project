import mysql.connector
import datetime
def insert(customer_id,billing_dt):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query="insert into bill_master(customer_id,billing_dt) values ('{0}','{1}')".format(customer_id,billing_dt)
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    bill_master_id=cursor.lastrowid
    cursor.close()
    return bill_master_id;  

def delete(bill_master_id):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query2="delete from bill_master where bill_master_id={0}".format(bill_master_id)
    cursor=con.cursor()
    cursor.execute(query2)
    con.commit()
    print("Data Deleted!")
    cursor.close()



def bill_details_by_bill_id(bill_master_id):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query1="select b.item_name,a.price,a.qty from bill_details as a  inner join items as b on a.item_id=b.item_id where bill_master_id={0} ". format(bill_master_id)
    cursor=con.cursor()
    cursor.execute(query1)
    records=cursor.fetchall()
    final_total=0
    for row in records:
        print("Item Name: ",row[0])
        print("Price: ",row[1])
        print("Qty: ",row[2])
        item_total=float(row[1])*float(row[2])
        final_total=final_total+item_total;
        print("Total:",item_total)
        print("-----------------------------------------")
    print("Total Bill Amount: ",final_total)

    con.commit()
    cursor.close()

def reports(startdt,enddt):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query1="select a.bill_master_id,a.customer_id,a.billing_dt,b.customer_name from bill_master as a inner join customers as b on a.customer_id=b.customer_id  where billing_dt between {0} and {1} ". format(startdt,enddt)
    cursor=con.cursor()
    cursor.execute(query1)
    records=cursor.fetchall()
    for row in records:
        print("Bill Master Id: ",row[0])
        print("Customer Id: ",row[1])
        print("Customer Name: ",row[3])
        print("Billing Date: ",row[2])
        print("--------BILL DETAILS-------------------")
        bill_details_by_bill_id(row[0])
        print("--------------------------------------------")
    con.commit()
    cursor.close()

def report_by_customer(customer_id):
    con=mysql.connector.connect(host="localhost",user="root",password="student",database="dbcoffeeshop")
    query1="select * from bill_master  where customer_id={0} ". format(customer_id)
    cursor=con.cursor()
    cursor.execute(query1)
    records=cursor.fetchall()
    for row in records:
        print("Bill Master Id: ",row[0])
        print("Billing Date: ",row[2])
        print("--------BILL DETAILS-------------------")
        bill_details_by_bill_id(row[0])
        print("--------------------------------------------")
    con.commit()
    cursor.close()
 
report_by_customer(1)
