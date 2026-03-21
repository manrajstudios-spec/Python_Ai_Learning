from Learning.Basic_Project.PasswordManager.Encryption_Decryption_Caesar_Ciphe import Encrypt
from Learning.Basic_Project.BankManager.Account import account
import time
import json

users_data_file = "Learning/Basic_Project/BankManager/Account.json"

def MakeNewAccount():
    while True:
        print("Enter The Details Asked To Make New Account Or Press (n) to abort action")
        user_input_name = input("Enter Your Name --> ")

        if user_input_name == "n":
            break
        
        time.sleep(0.5)
        if user_input_name:
            user_input_password = input("Create A Password ForYour Account Make Sure Password Is Strong --> ")

            time.sleep(0.5)
            if user_input_password :
                time.sleep(0.5)

                password = Encrypt(user_input_password)

                user_input_amount = input("Enter amount to deposit in account --> ")
                time.sleep(0.5)
                if user_input_amount and user_input_amount.isdigit():
                    amount = int(user_input_amount)
                    new_account = account(user_input_name , password)
                    new_account.AddMoney(amount_to_add=amount)
                    new_account.SaveAccountInfo()
                    i_d = new_account.i_d
                    time.sleep(1)

                    print("Account Made")
                    print(f"Your User ID is {i_d} dont forget it ,you would need it to access your account")
                    break

def LoadData():
    try :
        with open(users_data_file , 'r')as file:
            return json.load(file)
    except:
        return []
    
def TakeLoan(a:account):
    if a.is_loan_taken:
        print("Loan Cannot be Taken")
        return
    
    while True:
        user_input_amount = input("Enter Amount Which You Want To Take Loan For must be Graeater than 10000--> ")

        if user_input_amount and user_input_amount.isdigit() and int(user_input_amount) > 10000:
            user_input_timeline = input("Enter The Number of Months You want loan for --> ")

            if user_input_timeline and user_input_timeline.isdigit() and int(user_input_timeline) > 0:
                a.TakeLoan(int(user_input_amount),int(user_input_timeline))
                break
        if user_input_amount == "n":
            break
            

def Options(a:account):
    while True:
        user_input = input("Enter 1 To Deposit Money \nType 2 To Withdraw Money \nEnter 3 To Change Password \nPress 4 To Take Loan \nPress 5 to Pay Loan \n")

        if user_input and user_input.isdigit():
            u_input = int(user_input)
            match u_input:
                case 1: a.AddMoney(user_input)
                case 2: a.WithdrawMoney(user_input)
                case 3:
                    while True:
                        user_pass = input("Enter New Password")
                        if user_pass:
                            a.UpdatePassword(Encrypt(user_pass))      
                case 4: TakeLoan(a) 
                case 5:
                    while True:
                        if a.is_loan_taken :
                            print(f'Repayment left is {a.repayment_left}')
                            u_I = input("Enter Amount To Pay --> ")

                            if u_I and u_I.isdigit():
                                a.PayLoan(int(u_I))
                                break
                        else:
                            print("No Loan Taken")
                            break
                case _:
                    print("Invalid")
        elif user_input == "n":
            break    
        break

def AccessAccount():
    while True:
        user_input = input("Enter Your User ID provided when creating account: ")

        if user_input == "n":break
        if user_input  and user_input.isdigit():
            data = LoadData()
            if data:
                for d in data:
                    if d["ID"] == int(user_input):
                        while True:
                            user_pass = input("Enter Password To your Account --> ")
                            _pass = Encrypt(user_pass)
                            if user_pass and _pass == d["Password"]:
                                print(f'Account Holder Name is {d["User_Name"]} \nBank Balance is --> {d["Balance"]}')
                                _a = account(d["User_Name"] , d["Password"])
                                _a.i_d = d["ID"]
                                _a.balance = d["Balance"]
                                _a.is_loan_taken = d["LoanTaken"]
                                _a.total_loan = d["TotalLoan"]
                                _a.date_for_loan = d["DateTaken"]
                                _a.months_for_which_loan_taken = d["Timeline"]
                                _a.repayment_left = d["Repayment"]
                                _a.last_payment_ = d["LastPayment"]
                                _a.AddInterset()
                                Options(_a)
                                break
                            else:
                                print("Password Was Wrong")
                                time.sleep(1)
while True:
    user_input = input("Press 1 To Make New Account \nPress 2 To Access old account \n:  ")

    if user_input == "1":
        MakeNewAccount()
        break
    elif user_input == "2":
        AccessAccount()
        break