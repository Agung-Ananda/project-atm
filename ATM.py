user_id = 0
looping = "n"
user = [
    {
        "id"        : "1234",
        "acc_no"    : "112113114",
        "pin"       : "112233",
        "balance"   : 10000000
    },
    {
        "id"        : "1235",
        "acc_no"    : "112113115",
        "pin"       : "111111",
        "balance"   : 20000000
    },
    {
        "id"        : "1236",
        "acc_no"    : "112113116",
        "pin"       : "111222",
        "balance"   : 120000000
    }
]
login_status = False


def pin_checking(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False

def id_checking(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1

def acc_checking(acc_no):
    for i in range(len(user)):
        if str(user[i]['acc_no']) == str(acc_no):
            return int(i)
    return -1

def transfer_money(sum,acc_no):
    index1 = id_checking(user_id)
    index2 = acc_checking(acc_no)
    if index1 >= 0:
        if user[index1]['balance'] >= int(sum):
            user[index1]['balance'] = user[index1]['balance'] - int(sum)
            user[index2]['balance'] = user[index2]['balance'] + int(sum)
            print("You are succesfully transfer Rp. " +str(sum)+ " to " + acc_no)
            print("Your remaining balance are Rp. ", user[index1]['balance'])
        else:
            print("Sorry, Your balance is insufficient")


def withdraw_balance(sum):
    index1 = id_checking(user_id)
    if index1 >= 0:
        if user[index1]['balance'] >= int(sum):
            user[index1]['balance'] = user[index1]['saldo'] - int(sum)
            print("You are succesfully withdraw from your account Rp. " +str(sum))
            print("Your remaining balance are Rp. ", user[index1]['balance'])
        else:
            print("Sorry, Your balance is insufficient")

def save_to_account(sum):
    index1 = id_checking(user_id)
    if index1 >= 0:
        user[index1]['balance'] = user[index1]['balance'] + int(sum)
        print("You are succesfully saving to your account Rp. " +str(sum))
        print("Your remaining balance are Rp. ", user[index1]['balance'])

while login_status == False:
    print("Welcome to ATM Bank ABC")
    print("Please input your PIN")
    p = input("Input your PIN : ")

    pc = pin_checking(p)
    if pc != False:
        print("Welcome")
        user_id = pc['id']
        login_status = True
        looping = 'y'
    else:
        print("Sorry, Your PIN is wrong")

while looping == "y" and login_status == True:
    u = user[id_checking(user_id)]
    print("Welcome to ATM Bank ABC")
    print("1. Balance Check")
    print("2. Transfer")
    print("3. Cash Withdrawal")
    print("4. Save To Account")
    print("5. Exit")
    a = int(input("Please select menu : "))
    if a == 1 :
        print("")
        print("Your remaining balance is : ",u['balance'])
        print("")
        looping = "n"
    elif a == 2:
        print("Please insert beneficiary account number")
        ac_no = input("Beneficiary Account Number : ")
        acchk = acc_checking(ac_no)

        if acchk >= 0:
            print("Account Number found, Please insert amount that will be transferred")
            amount = input("Amount that will be transferred : ")
            transfer_money(amount,ac_no)
            print("")
            looping = "n"
        else:
            print("")
            print("Account number can't be found")
            print("")
    elif a == 3:
        amount = input("Amount that will be withdrawal : ")
        withdraw_balance(amount)
        print("")
        looping = "n"
    elif a == 4:
        amount = input("Amount that will be save to your account : ")
        save_to_account(amount)
        print("")
        looping = "n"
    elif a == 5 :
        login_status = False
        looping = "n"
    else:
        print("option not available")
    if login_status == True:
        input("Back to menu [Enter]")
        print("")
        looping = "y"