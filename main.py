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
    try:
        if accountList[username]['password'] == password:
            account = username
            print "\nWelcome, " + username
            print "    Your " + accountList[username]['permission'] + '\n'
        else:
            print "Password not match"
    except:
        print "No such account. Fork u :p"
        return 

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
    try:
        if len(questionList) == 0:
            print "There is no question."
        for question in questionList[classs]:
            print i+1, ". title = ", question['title']
            i = i+1
        print ""
    except:
        print "No such class Bro"
        return
    questionNumber = input("Which Question do you want? ")
    if accountList[account]['permission'] == 'admin' and questionNumber == 0:
        deleteNumber = input("Please enter the nubmer you want to delete(0 as cancel) ")
        if deleteNumber == 0:
            return 
        else :
            print "\n", questionList[classs][deleteNumber-1]['title'], "deleted!!", "\n"
            questionList[classs].pop(deleteNumber-1)
            return 
    print ""
    try:
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
    except:
        print "No fucking Question bro"
        return 

def search():
    keyword = raw_input("\nInput your keyword : ")
    for classs in questionList:
        for question in questionList[classs]:
            if keyword in question['title']:
                print question['title']
                try:
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
                except:
                    print "No fucking Question bro"
                    return 
                    

def settings():
    print "\n1.Add class"
    print "2.Del class\n"
    choise = raw_input("Enter your option : ")
    if choise == '1':
        classs = raw_input("Which class do you want to add(0 as cancel) : ")
        if classs == '0':
            return
        else:
             questionList[classs] = {}
    elif choise == '2':
        classs = raw_input("Which class do you want to delete(0 as cancel) : ")
        if classs == '0':
            return
        else:
            print classs, " deleted!!"
            del questionList[classs]
        pass
    print ""

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
            print "\nfork u :p\n"

