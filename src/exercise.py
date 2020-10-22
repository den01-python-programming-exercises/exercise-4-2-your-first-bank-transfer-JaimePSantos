
def main():
    #write your code below this line
    acc1 = Account("Matthew's account",1000)
    acc2 = Account("My account",0)
    acc1.withdraw(100)
    acc2.deposit(100)
    print(acc1)
    print(acc2)
    

if __name__ == '__main__':
    from account import Account
    main()
else:
    from src.account import Account