'''
4
Write a Python program that computes the net amount of a bank account
 based a transaction log from console input. The transaction log format
  is shown as following: D 100 W 200 (Withdrawal is not allowed if balance
   is going negative. Write functions for withdraw and deposit)
    D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300, D 300 , W 200, D 100 Then, the output should be: 500'''


from colorama import Fore

Amount=0
while True:
    choice = input("W to Withdraw D to Deposit").split()
    if int(choice[1]) > 0 :
        if 'D' in choice:
            Amount=Amount+int(choice[1])
        if Amount > 0:
            if 'W' in choice:
                Amount = Amount-int(choice[1])
        else:
            print(Fore.RED+"Your Account Balance is Insufficient")
        print(Fore.GREEN+"Now Your Account Balance is ",Amount)
    else:
        print(Fore.RED+"NEGATIVE AMOUNT NOT ALLOWED FOR WITHDRAW AND DEPOSIT")
