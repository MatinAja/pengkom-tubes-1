import random as r
import pickle as p
import os.path as o

Accounts = {}

while True:
    print("-"*80)
    print("Banking System".center(80))
    print("-"*80)
    print("1.Admin Login\n2.Customer Login")
    choice = int(input("Select:"))
    
    if choice == 1:
        admin_id = input("Enter Admin Id:")
        password = input("Enter Admin Password:")
        if admin_id == "Ishim" and password == "1234":
            while True:
                print("-"*80)
                print("Admin Panel".center(80))
                print("-"*80)
                print("1.Add New Account")
                print("2.Remove Account")
                print("3.Edit Account")
                print("4.Display All Accounts")
                print("5.Search Account")
                print("0.Exit")
                admin_choice = int(input("Select:"))
                
                if admin_choice == 1:
                    ac_no = input("Enter Account Number:")
                    if ac_no in Accounts.keys():
                        print("This Account Number already exists")
                    else:
                        name = input("Enter Account Holder Name:")
                        phone = input("Enter Phone Number:")
                        address = input("Enter Address:")
                        gender = input("Enter gender:")
                        password = r.randint(100000, 1000000)
                        balance = 0
                        Accounts[ac_no] = [name, phone, address, gender, password, balance]
                        print("Account Has Been Created")
                
                elif admin_choice == 2:
                    ac_no = input("Enter Account Number:")
                    if ac_no in Accounts.keys():
                        del Accounts[ac_no]
                        print("Account Has Been Deleted")
                    else:
                        print("Account Doesn't Exists")
                
                elif admin_choice == 3:
                    ac_no = input("Enter Account Number:")
                    if ac_no in Accounts.keys():
                        print("-"*80)
                        print("Holder Name:", Accounts[ac_no][0])
                        print("Phone:", Accounts[ac_no][1])
                        print("Address:", Accounts[ac_no][2])
                        print("Gender:", Accounts[ac_no][3])
                        print("Password:", Accounts[ac_no][4])
                        print("Balance:", Accounts[ac_no][5])
                        print("-"*80)
                        print("What do you want to change:")
                        print("0.Holder Name")
                        print("1.Phone")
                        print("2.Address")
                        print("3.Gender")
                        admin_edit_choice = int(input())
                        if admin_edit_choice >= 0 and admin_edit_choice < 4:
                            v = input("Enter New Value:")
                            if v != "":
                                Accounts[ac_no][admin_edit_choice] = v
                                print("Account Has Been Updated")
                            else:
                                print("Try Again..")
                        else:
                            print("Wrong Choice")
                    else:
                        print("Account Doesn't Exists")
                
                elif admin_choice == 4:
                    print("-"*80)
                    print("Account Table".center(80))
                    print("-"*80)
                    for account in Accounts:
                        print(account, Accounts[account])
                
                elif admin_choice == 5:
                    ac_no = input("Enter Account Number:")
                    if ac_no in Accounts.keys():
                        print("-"*80)
                        print("Holder Name:", Accounts[ac_no][0])
                        print("Phone:", Accounts[ac_no][1])
                        print("Address:", Accounts[ac_no][2])
                        print("Gender:", Accounts[ac_no][3])
                        print("Password:", Accounts[ac_no][4])
                        print("Balance:", Accounts[ac_no][5])
                        print("-"*80)
                    else:
                        print("Account Doesn't Exists")
                
                elif admin_choice == 0:
                    exit()
                
                input("Continue...")
        
        else:
            print("Id/Password not mateched")
    
    elif choice == 2:
        act_no = input("Enter Account Number:")
        if act_no in Accounts.keys():
            password = int(input("Enter Account Password:"))
            if Accounts[act_no][4] == password:
                while True:
                    print("-"*80)
                    print("Customer Panel".center(80))
                    print("-"*80)
                    print("1.Deposit Cash")
                    print("2.Withdraw Cash")
                    print("3.Check Balance")
                    print("0.Exit")
                    customer_choice = int(input("Select:"))
                    
                    if customer_choice == 1:
                        amount = int(input("Enter Amount For Deposit:"))
                        Accounts[act_no][5] += amount
                        print("Amount Deposited")
                    
                    elif customer_choice == 2:
                        amount = int(input("Enter Amount For Withdraw:"))
                        if Accounts[act_no][5] > amount:
                            Accounts[act_no][5] -= amount
                            print("Amount Withdraw.")
                        else:
                            print("Can not Withdraw.")
                    
                    elif customer_choice == 3:
                        print("Balance: Rs.", Accounts[act_no][5])
                    
                    elif customer_choice == 0:
                        exit()
                    
                    input("Continue...")
            
            else:
                print("Password does not matched")
        
        else:
            print("Account not available")
