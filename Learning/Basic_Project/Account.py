import json
from datetime import date
class account:
    
    users_data_file = "Learning/Basic_Project/Account.json"
    _pass = ""
    def __init__(self , user_name , password,balance:int):
        self.user_name = user_name
        self.password = password
        self.balance = balance
        self.i_d = 0
        self.is_loan_taken = False
        self.total_loan = 0 
        self.repayment_left = 0
        self.date_for_loan = []
        self.months_for_which_loan_taken = 0
        self.last_payment_ = 0

    def AddMoney(self , amount_to_add:int):
        self.balance += amount_to_add
        print(f"{amount_to_add} Deposited")
        self.UpdateInfo()

    def WithdrawMoney(self , amount_to_withdraw:int):

        if self.balance - amount_to_withdraw >= 0:
            self.balance -= amount_to_withdraw
            print(f"{amount_to_withdraw} Withdrew")

            self.UpdateInfo()
        else:
            print(f"Not Enough Money {self.balance}")
            return False

    def UpdatePassword(self,_pass):
        self.password = _pass
        self.UpdateInfo()

    def LoadData(self):
        try :
            with open(self.users_data_file , 'r')as file:
                return json.load(file)
        except:
            return []
                     
    def UpdateInfo(self):
        data = self.LoadData()

        if data:
            for d in data:
                if self.i_d == d["ID"]:
                    d["Balance"] = self.balance
                    d["Password"] = self.password
                    break
            
            with open(self.users_data_file,'w') as file:
                json.dump(data,file,indent=4)

    def UpdateLoanInfo(self):
        data = self.LoadData()

        if data:
            for d in data:
                if self.i_d == d["ID"]:
                    d["Balance"] = self.balance
                    d["LoanTaken"] = self.is_loan_taken
                    d["TotalLoan"] = self.total_loan
                    d["Repayment"] = self.repayment_left
                    d["Timeline"] = self.months_for_which_loan_taken
                    d["LastPayment"] = [date.today().year , date.today().month , date.today().day,0]
                    d["DateTaken"] = [date.today().year , date.today().month , date.today().day]
                    break
            
            with open(self.users_data_file,'w') as file:
                json.dump(data,file,indent=4)

    def ClearLoan(self):
        self.is_loan_taken = False
        self.total_loan = 0 
        self.repayment_left = 0
        self.date_for_loan = []
        self.months_for_which_loan_taken = 0
        self.last_payment_ = 0
        self.UpdateLoanInfo()


    def Take_Money(self , more:bool):
        total = self.total_loan + (self.total_loan * 0.015 * self.months_for_which_loan_taken)
        emi = total / self.months_for_which_loan_taken + 1000 if more else 0

        if not self.WithdrawMoney(emi):
            self.repayment_left += emi
            return
        
        self.WithdrawMoney(emi)
        self.date_for_loan = [date.today().year , date.today().month , date.today().day,emi]
        self.repayment_left -= emi

        if self.repayment_left <= 0 :
            self.ClearLoan()
        self.UpdateLoanInfo()
    
    def PayLoan(self,amount):
        if not self.WithdrawMoney(amount):
            print("You dont Have money")
            return
        
        self.repayment_left -= amount
        if self.repayment_left <= 0:
            self.ClearLoan()

        self.UpdateLoanInfo()

    def AddInterset(self):
        if self.is_loan_taken:
            last_payment_date = date(self.last_payment_[0],self.last_payment_[1],self.last_payment_[2])
            loan_taken = date(self.date_for_loan[0],self.date_for_loan[1],self.date_for_loan[2])
            diff = (date.today() - last_payment_date).days
            months =(date.today() - loan_taken).days // 30 
            if diff >= 30:
                self.Take_Money(True if months > self.months_for_which_loan_taken else False)


    def TakeLoan(self,amount_of_loan:int,months_for_loan_taken:int):
        self.AddMoney(amount_of_loan)
        self.is_loan_taken = True
        self.total_loan = amount_of_loan
        self.repayment_left = amount_of_loan + 1000
        self.months_for_which_loan_taken = months_for_loan_taken
        self.last_payment_ = [date.today().year , date.today().month , date.today().day,0]
        self.UpdateLoanInfo()

    def SaveAccountInfo(self):
        data = self.LoadData()

        user_data = {"User_Name":self.user_name,
                     "Password":self.password,
                     "Balance":self.balance,
                     "ID":len(data)
                    }
        self._pass = self.password
        self.i_d = len(data)

        data.append(user_data)

        with open(self.users_data_file,'w') as file:
            json.dump(data,file,indent=4)