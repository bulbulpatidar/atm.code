print("insert the card")
language=input("enter your language :")
if language=="english":
    print("next")
    pin=int(input("enter your pin: "))
    if pin>=1000 and pin<=9999:
        print("next")
        accounttype=input("enter your account type :")
        if accounttype=="saving" or accounttype=="current":
            print("next")
            transtion=input("enter your transtion :")
            balance=10000
            if transtion=="withdrawl":
                withdrawl=int(input("enter your withdrawl :"))
                remain=balance-withdrawl
                print("bank balane=",remain)
            else:
                if transtion=="deposite":
                     deposite=int(input("enter your deposite: "))
                     remain=balance+deposite
                     print("bank balance=",remain)     
            reciept=input("do you want reciept: ")
            if reciept=="yes":
                print("collect your reciept")
                print("thanks for visiting") 
            else:
                print("collect your reciept")
                print("thanks for visiting")    
        else:
            print("plz choose your account : ")
    else:
       print("plz enter valid pin :")
else:
    print("plz enter language : ")