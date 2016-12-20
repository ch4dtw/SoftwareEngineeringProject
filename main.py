import json

content = open("account.json").read()
accountList = json.loads(content)
content = open("question.json").read()
questionList = json.loads(content)
account = ""

def login():
    global accountList,account
    username = raw_input("please enter the account : ")
    password = raw_input("please enter the password : ")
    if accountList[username]['password'] == password:
        account = username
        print "\nWelcome, " + username
        print "    Your " + accountList[username]['permission'] + '\n'
    else:
        print "Password not match"

def submit():
    print "no such features yet"
    pass
def search():
    pass
def lists():
    pass
def settings():
    pass

while(1):
    if account == "":
        print "1.login"
        print "2.submit"
        choise = raw_input("Enter your option : ")
        if choise == '1':
            login()
        else:
             submit()
    else:
        print "1.Class List"
        print "2.Search"
        if accountList[account]['permission'] == 'admin':
            print "3.Settings"
        choise = raw_input("Enter your option : ")
        if choise == '1':
            lists()
        elif choise == '2':
            search()
        elif choise == '3' and accountList[account]['permission'] == 'admin':
            settings()
                
             


