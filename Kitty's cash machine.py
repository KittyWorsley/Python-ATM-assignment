print("Welcome to Kitty's ATM please enter your card") 
transaction_list=[]
trials = 3
user_pin = "5678"
user_pin_successful = False

while trials > 0 and user_pin_successful == False:
    pin = input("Please put your 4 number pin in")
    if user_pin == pin:
        user_pin_successful = True
    else:
        trials-=1
        print("incorrect pin number", trials,"Trials left")
if not user_pin_successful:
    print("too many incorrect attempts, please insert your card again")

user_choice = -1
balance = 0 
menu = """
1. Withdraw. 
2. Deposit. 
3. Check Balance. 
4. Transaction history.
5. Quit.
"""
user_choice = input(" 1 : Withdraw money: 2 : deposit money 3: check balance 4: transaction history 5: quit ")  

if user_choice == "1":
            user_withdraw = float(input("How much do you want to withdraw? £:"))                                                
            if user_withdraw <balance:
                                  balance-= user_withdraw
                                  transaction_list.append(f"withdrawn:£{user_withdraw}")
            print(f"£{user_withdraw} has been withdrawn out of your bank") 
          

            

user_choice = input(" 1 : Withdraw money: 2 : deposit money 3: check balance 4: transaction history 5: quit ")
if user_choice == "2":
    user_deposit = float(input("How much do you want to deposit:") )    
         
transaction_list.append(f"Deposited: £{user_deposit}")
print(f"£{user_deposit} has been deposited into your account.")

User_Choice = input(" 1 : Withdraw money: 2 : deposit money 3: check balance 4: transaction history 5: quit ")
if user_choice=="3":
    print(f"your balance is: £{balance}")

User_Choice = input(" 1 : Withdraw money: 2 : deposit money 3: check balance 4: transaction history 5: quit ")
if user_choice =="4":
   
    if transaction_list:
        print("transaction list:")
    for transaction in transaction_list:
          print(transaction)   

if user_choice=="5":
            user_exit=input("would you like to continue? yes/no")
if"no":
            print("thank you for using kittys ATM") 
        













  
