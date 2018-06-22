
#--------------------------------------opens the file----------

accounts_file = open('accounts.txt')
text = accounts_file.read().strip().split() 
#------------------------------------Declares variables---------
mainmenu=0
balance = ["£600,000"]
transactions = ["Maccies: 13/06/18 £20, Argos: 12/06/2018, £800"]

#-----------------------------Functions--------------------------
def Options():
    mainmenu = int(input("To view your balance press 1, To view your recent transactions press 2, To transfer money press 3, To logout press 4"))
    if mainmenu == 1:
        OptionOne(mainmenu)
    elif mainmenu == 2:
        OptionTwo(mainmenu)
    elif mainmenu == 3:
        OptionThree(mainmenu)
    else:
        OptionFour(mainmenu)


def OptionOne(mainmenu):
        print(balance)
        lol = input("Are you finished?")
        if lol == "Yes":
            print("Logged Out")
            exit()
        else:
            mainmenu = int(input("To view your balance press 1, To view your recent transactions press 2, To transfer money press 3, To logout press 4"))
def OptionTwo(mainmenu):
    print(transactions)
    lol2 = input("Are you finished?")
    if lol2 == "Yes":
        print("Logged Out")
        exit()
    else:
        mainmenu = int(input("To view your balance press 1, To view your recent transactions press 2, To transfer money press 3, To logout press 4"))

def OptionThree(mainmenu):
    where = input("Please enter the account number you want to transfer money to")
    amount = input("Please enter the amount you would like to transfer to: "+where+"")
    print("Successfully sent "+amount+" to "+where+"")
    lol3 = input("Are you finished?")
    if lol3 == "Yes":
        print("Logged Out")
        exit()
    else:
        mainmenu =int(input("To view your balance press 1, To view your recent transactions press 2, To transfer money press 3, To logout press 4"))

def OptionFour(mainmenu):
    print("Logged out")
    exit()

#-------------------------------Opening part of program--------------

print("Welcome to the Cashew Bank")


initallogin = input("Please enter your PIN Code")
while mainmenu != 4:
    if initallogin == '':
        continue
    if initallogin in text:
        print("Logged in")
        Options()#calls the main menu of options
    else:
        end()
            
        
