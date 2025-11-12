import users;
import bill_master
import bill_details;
import customers;
import items;
def MainMenu(choice):
    if(choice=="MainMenu"):
        
        print("------------------MAIN MENU------------------")
        print("1---------------------------Manage Users")
        print("2---------------------------Manage Customers")
        print("3---------------------------Manage Items")
        print("4---------------------------Manage Billing")
        print("5---------------------------Reports")
        ch=input("Enter Your Choice: ")
        if(ch=="1"):
            MainMenu("Users")
        elif(ch=="2"):
            MainMenu("Customers")
        elif(ch=="3"):
            MainMenu("Items")
        elif(ch=="4"):
            MainMenu("Billing")
        elif(ch=="5"):
            MainMenu("Reports")
           
    elif(choice=="Users"):
            print("------------------USERS------------------")
            print("1---------------------------Add Users")
            print("2---------------------------Delete User")
            print("3---------------------------Update User")
            print("4---------------------------Get All Users")
            print("5---------------------------Search")
            print("9---------------------------Main Menu")
            ch=input("Enter Your Choice: ")
            if(ch=="1"):
                user_name=input("Enter User Name:")
                password=input("Enter User's Password:");
                users.insert(user_name,password)
                MainMenu("Users")
            elif(ch=="2"):
                users.search()
                user_id=input("Enter User Id to delete : ")
                users.delete(user_id)
                MainMenu("Users")              
            elif(ch=="3"):
                users.search()
                user_id=input(" Enter User Id: ")
                user_name=input(" Enter  New User Name: ")
                password=input(" Enter New Password: ")
                users.update(user_id,user_name,password)
                MainMenu("Users")
            elif(ch=="4"):
                users.get_all()
                MainMenu("Users")
            elif(ch=="5"):
                users.search()
                MainMenu("Users")
            elif(ch=="9"):
                MainMenu("MainMenu")
    
    elif(choice=="Customers"):
        print("------------------CUSTOMERS------------------")
        print("1---------------------------Add Customer")
        print("2---------------------------Delete Customer")
        print("3---------------------------Update Customer")
        print("4---------------------------Get All Customerers")
        print("5---------------------------Search")
        print("9---------------------------Main Menu")
        ch=input("Enter Your Choice: ")
        if(ch=="1"):
            customer_name=input("Enter Customer Name:")
            address=input("Enter  Address:")
            phone_no=input("Enter  Phone No:")
            customers.insert(customer_name,address,phone_no)
            MainMenu("Customers")
        elif(ch=="2"):
            customers.search()
            customer_id=input("Enter Customer's Id To Delete : ")
            customers.delete(customer_id)
            MainMenu("Customers")
        elif(ch=="3"):
                    customers.search()
                    customer_id=input(" Enter Customer's Id: ")
                    customer_name=input("Enter Customer's New Name: ")
                    address=input(" Enter   Customer's  New Address: ")
                    phone_no=input(" Enter Customer's New Phone No. : ")
                    customers.update(customer_id,customer_name,address,phone_no)
                    MainMenu("Customers")
        elif(ch=="4"):
             customers.get_all()
             MainMenu("Customers")
        elif(ch=="5"):
            customers.search()
            MainMenu("Customers")
        elif(ch=="9"):
            MainMenu("MainMenu")            
    elif(choice=="Items"):
            print("------------------ITEMS------------------")
            print("1---------------------------Add Item")
            print("2---------------------------Delete Item")
            print("3---------------------------Update Item")
            print("4---------------------------Get All Items")
            print("5---------------------------Search")
            print("9---------------------------Main Menu")
            ch=input("Enter Your Choice: ")
            if(ch=="1"):    
                item_name=input("Enter Item Name:")
                mrp=float(input("Enter mrp: "))
                items.insert(item_name,mrp)
                MainMenu("Items")
            elif(ch=="2"):
                items.search()
                item_id=input("Enter Item Id to delete : ")
                items.delete(item_id)
                MainMenu("Items")
            elif(ch=="3"):
                items.search()
                item_id=input(" Enter Item Id: ")
                item_name=input("Enter  Item's New Name: ")
                mrp=float(input(" Enter Item's New Mrp: "))
                items.update(item_id,item_name,mrp)
                MainMenu("Items")
            elif(ch=="4"):
                 items.get_all()
                 MainMenu("Items")
            elif(ch=="5"):
                items.search()
                MainMenu("Items")
            elif(ch=="9"):
                MainMenu("MainMenu")     
    elif(choice=="Billing"):
        print("------------------BILLING------------------")
        print("1---------------------------Generate Bill")
        print("2---------------------------Delete Bill")
        print("9---------------------------Main Menu")
        ch=input("Enter Your Choice: ")
        if(ch=="1"):
                customers.search()
                customer_id=int(input("Enter Customer Id: "))
                billing_dt=input("Enter Billing Date(yyyy/mm/dd): ")
                bill_master_id=bill_master.insert(customer_id,billing_dt)
                print("Bill Created Successfully with ID", bill_master_id)
                print("-----------------------------------------------------------------------")
                print("Please enter Items in the Bill")
                while True:
                    items.search()
                    item_id=int(input("Enter Item Id: "))
                    qty=float(input("Enter  Quantity: "))
                    price=float(input("Enter Price: "))
                    bill_details.insert(bill_master_id,item_id,qty)
                    print("----------------------------------------------------------------------")
                    ch=input("Do you  want to add more Items? Enter 'N' to Exit: ")
                    if(ch.lower()=="n"):
                        print("Bill Generated Successfully. Thanks for your order")
                        bill_master.bill_details_by_bill_id(bill_master_id)
                        break
                MainMenu("Billing")
            
        elif (ch=="2"):
            
            bill_master_id=input("Enter Bill Master Id: ")
            bill_details.delete(bill_master_id)
            bill_master.delete(bill_master_id)
            MainMenu("Billing")
        elif(ch=="9"):
            MainMenu("MainMenu")
    elif(choice=="Reports"):
        print("------------------REPORTS------------------")
        print("1---------------------------Get Records")
        print("9---------------------------Main Menu")
        ch=input("Enter Your Choice: ")
        if(ch=="1"):
            startdt=input("Enter starting date [YYYY,MM,DD]: ")
            enddt=input("Enter ending date [YYYY,MM,DD]: ")
            bill_master.reports(startdt,enddt)
            MainMenu("Reports")
        elif(ch=="9"):
            MainMenu("MainMenu")
        
 

                
    
