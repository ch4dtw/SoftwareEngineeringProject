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

def lists():
    print ""
    for classs in questionList:
        print classs
    print ""
    classs = raw_input("Which class do you want to see? : ")
    i = 0
    print ""
    for question in questionList[classs]:
        print i+1, ". title = ", question['title']
        i = i+1
    print ""
    questionNumber = input("Which Question do you want? ")
    print ""
    question = questionList[classs][questionNumber-1]
    print "class = ", classs
    print "title = ", question['title']
    print "name = " , question['questioner']
    for answer in question['answer']:
        print "#############################"
        if answer['isBestAnswer'] == True:
            print "This is Best Answer!!"
        print "name = ", answer['name'], ", integral = ", accountList[answer['name']]['integral']
        print "Answer = ", answer['data']
    print ""

def search():
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
        elif choise == '2':
             submit()
        else:
            print "fork u :p"
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
        else:
            print "fork u :p"
                
             


