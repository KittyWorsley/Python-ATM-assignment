print("Welcome to Kitty's ATM please enter your card")
Trials = 3
Userpin = 5678
while Trials !=0:
    Pin = int(input("Please put your 4 number pin in"))
    if Pin != Userpin:
        Trials -= 1
        print("incorrect pin number", Trials,"Trials left")
    else:
        UserChoice = input("D: Deposit money or W: Withdraw money: ")
        if UserChoice == "D":
            UserDeposit = input("How much do you want to deposit:")
            print("UserDeposit,£ has been deposited into your bank")
            UserChoice = input("D: Deposit money or W: Withdraw money: ")
        if UserChoice == "W":
            UserWithdraw = input("How much do you want to withdraw:")
            print("UserWithdraw,£ has been withdrawn into your bank")
    UserExit = input("Would you like to continue? Yes/No")
    if UserExit == "No":
     print("Thank you for using Kitty's ATM")
     break
    else:
        continue
    
