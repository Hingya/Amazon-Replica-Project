import mysql.connector

db=mysql.connector.connect(
   host="127.0.0.1",
   port="3306",
   user="root",
   password="Swapnil99",
   database="Amazon",
   auth_plugin = "mysql_native_password"
)

command_handler = db.cursor(buffered=True)

def cr_member():
    while 1:
        print("Member menu")
        print("1.View Product List")
        print("2.New Order")
        print("3.View Order History")
        print("4.Update Profile")
        print("5.Logout")
        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("View Product List")
            command_handler.execute("SELECT Product_Name FROM product")
            result = command_handler.fetchall()
            for row in result:
                print(row)
                print('\n')
        elif user_option == "2":
            print("")
            print("New Order")
            order_name = input(str("Enter Product_name: "))
            Name = str(input("Enter Name: "))
            Product_id = int(input("Enter Product_id :"))
            query_vals = (order_name,Name,Product_id)
            command_handler.execute("INSERT INTO orders (order_name,Name,Product_id) VALUES (%s,%s,%s)",query_vals)
            db.commit()
            print(order_name +"Your Order is Successfully Placed")
        elif user_option == "3":
            print("")
            print("View Order History")
            command_handler.execute("SELECT orders.order_name,user.Name FROM user INNER JOIN orders ON users.Product_id = orders.Product_id")
            result = command_handler.fetchall()
            for row in result:
                print(row)
                print('\n')
        elif user_option == "4":
            print("")
            print("Update Profile")
            print("1.Change Name")
            print("2.change Email")
            print("3.change username")
            print("4.change password")
            print("5.change Address")
            print("6.Back")
            user_option = input(str("Option : "))
            if user_option == "1":
                print("")
                print("Change Name")
                Name = input(str("Enter New Name : "))
                username = input(str("enter Your username : "))
                command_handler.execute("UPDATE user SET Name = %s WHERE username = %s",(Name,username))
                db.commit()
                print(Name+"Changed Name")
            elif user_option == "2":
                print("")
                print("Change Email")
                Email = input(str("Enter New Email : "))
                username = input(str("enter Your username : "))
                command_handler.execute("UPDATE user SET Email =%s WHERE username =%s",(Email,username))
                db.commit()
                print(Email+"changed Email id")
            elif user_option == "3":
                print("")
                print("change username")
                username = input(str("Enter New username : "))
                Email = input(str("Enter Your Email: "))
                command_handler.execute("UPDATE user SET username =%s WHERE Email =%s",(username,Email))
                db.commit()
                print(username+"changed username")
            elif user_option == "4":
                print("")
                print("change password")
                password = input(str("Enter New password : "))
                username = input(str("Enter Your username : "))
                command_handler.execute("UPDATE users SET password =%s WHERE username =%s",(password,username))
                db.commit()
                print(username+"changed password")
            
            elif user_option == "5":
                print("change Address")
                Address = input(str("Enter New Address : "))
                username = input(str("Enter Your username : "))
                command_handler.execute("UPDATE users SET Address =%s WHERE username =%s",(Address,username))
                db.commit()
                print(username + "changed Address")
            elif user_option == "6":
                print("Back")
                break
            else:
                print("No valid option selected")
        elif user_option == "5":
            print("")
            print("Logout")
            break
        else:
            print("No valid option selected")

def admin_session():
    while 1:
        print("Addmin Menu \n 1.Create Product \n 2.View Product List \n 3.View Order Details \n 4.Update Product \n 5.Delete Product \n 6.Logout")
        print("")
        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Create Product")
            Product_id = int(input("Product id : "))
            Product_name = str(input("Product Name : "))
            Manufacturer_Name = str(input("Manufacturer_Name : "))
            Price = int(input("Price : "))
            Discount = int(input("Discount : "))
            Total_stock_available = int(input("Total_stock_available : "))
            query_vals = (Product_id,Product_name,Manufacturer_Name,Price,Discount,Total_stock_available)
            command_handler.execute("INSERT INTO product (Product_id,Product_name,Manufacturer_Name,Price,Discount,Total_stock_available) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(Product_name + " These Product is Created")
        elif user_option == "2":
            print("")
            print("View Product List")
            command_handler.execute("SELECT Product_Name FROM product")
            result = command_handler.fetchall()
            for row in result:
                print(row)
                print('\n')
        elif user_option == "3":
            print("")
            print(" View Order Details")
            print("Product_id,","Product_Name,","Manufacturer_Name,","Price,","Discount,","Total_stock_available,")
            command_handler.execute("SELECT * FROM product")
            result = command_handler.fetchall()
            for row in result:
                print(row)
                print('\n')
        elif user_option == "4":
            print("")
            print("Update Product")
            print("Change Details")
            print("1. Change Product_id")
            print("2. Change Product_name")
            print("3. Change Manufacturer_Name")
            print("4. Change Price")
            print("5. Change  Discount")
            print("6. Change Total_stock_available")
            user_option = input(str("Option : "))
            if user_option == "1":
                print("")
                print("Change Product_id")
                Product_id = int(input("Change  Product_id: "))
                Product_name = str(input("Enter Product_name: "))
                command_handler.execute("UPDATE product SET Product_id = %s WHERE Product_name = %s",(Product_id,Product_name))
                db.commit()
                print("Changed Product_id")
            elif user_option == "2":
                print("")
                print("Change Product_name")
                Product_name = str(input("Change Product_name: "))
                Product_id = int(input("Enter Product_id: "))
                command_handler.execute("UPDATE product SET Product_name = %s WHERE Product_id = %s",(Product_name,Product_id))
                db.commit()
                print("Changed Product_name")
            elif user_option == "3":
                print("")
                print("Change Manufacturer_Name")
                Manufacturer_Name = str(input("Change Manufacturer_Name: "))
                Product_name = str(input("Enter Product_name: "))
                command_handler.execute("UPDATE product SET Manufacturer_Name = %s WHERE Product_name = %s",(Manufacturer_Name,Product_name))
                db.commit()
                print("Changed Manufacturer_Name")
            elif user_option == "4":
                print("")
                print("Change Price")
                Price = int(input("Change Price: "))
                Product_name = str(input("Enter Product_name: "))
                command_handler.execute("UPDATE product SET Price = %s WHERE Product_name = %s",(Price,Product_name))
                db.commit()
                print("Changed Price")
            elif user_option == "5":
                print("")
                print("Change  Discount")
                Discount = int(input("Change  Discount: "))
                Product_name = str(input("Enter Product_name: "))
                command_handler.execute("UPDATE product SET Discount = %s WHERE Product_name = %s",(Discount,Product_name))
                db.commit()
                print("Changed Discount")
            elif user_option == "6":
                print("")
                print("Change Total_stock_available")
                Total_stock_available = int(input("Change Total_stock_available: "))
                Product_name = str(input("Enter Product_name: "))
                command_handler.execute("UPDATE product SET Total_stock_available = %s WHERE Product_name = %s",(Total_stock_available,Product_name))
                db.commit()
                print("Changed Total_stock_available")
            elif user_option == "7":
                print("")
                print("Back")
                break
            else:
                print("No valid option selected")

        elif user_option == "5":
            print("")
            print("Delete Product")
            Product_name = str(input("Enter Product_name: "))
            command_handler.execute("DELETE FROM product WHERE Product_name = '%s'",(Product_name))
            db.commit()
            print("Product is Deleted")
        elif user_option == "6":
            print("")
            print("Logout")
            break
        else:
            print("No valid option selected")

def a_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "admin":
                admin_session()
            
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")

def member():
    print("")
    print("member Login")
    print("")
    username = input(str("Username : "))
    us = command_handler.execute("SELECT * FROM user WHERE username = '{}'".format(username))
    password = input(str("Password : "))
    pa = command_handler.execute("SELECT * FROM user WHERE password = '{}'".format(password))
    try:
        cr_member()
        if username == db.commit(us):
            if password ==db.commit(pa):
                print("")
            else:
                print("Incorrect password !")
        else:
            print("Login details not recognised")
    except:
        cr_member()
        if username == "swapnil99":
            if password == "swapnil99":
                cr_member()
            else:
                print("Incorrect password !")
        else:
            print("Login details not recognised")

def member_ab():
    while 1:
        print("Register Member Menu")
        print("1. Register new Member")
        print("2. Delete Existing Member")
        print("3. Back")
        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Register new Member")
            Name = input(str("Enter Your Name : "))
            Email = input(str("Enter Your Email : "))
            username = input(str("Enter Your username : "))
            password = input(str("Enter Your password : "))
            Address = input(str("Enter Your Address : "))
            query_vals = (Name,Email,username,password,Address)
            command_handler.execute("INSERT INTO user (Name,Email,username,password,Address) VALUES (%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(username + " has been registered as a Member")
        elif user_option == "2":
            print("")
            print("Delete Existing Member Account")
            username = input(str("Member username : "))
            Email = input(str("Member password : "))
            query_vals = (username,password)
            command_handler.execute("DELETE FROM user WHERE username = %s AND password = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")
        elif user_option == "3":
            break
        else:
            print("No valid option selected")

def main():
    print("Welcome to Amazon Replica \n")
    while 1:
        print("1. Login Addmin")
        print("2. Login Member")
        print("3. Register Member")
        print("4. End ")
        user_option = input(str("Option : "))
        if user_option =="1":
            print("Addmin Login")
            a_admin()
        elif user_option == "2":
            print("Member Login")
            member()
        elif user_option == "3":
            print("Register Member")
            member_ab()
        elif user_option == "4":
            print("End")
            print("❤ Thank You For Visiting Amazon Replica World ❤")
            break
        else:
            print("Not Valid")
main()