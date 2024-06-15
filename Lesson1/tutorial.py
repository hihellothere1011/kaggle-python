def entry():
    
    print("This is the first lesson you\'ll start, it\'s talking about the syntax, the variables, and the operators.")

    print("Let\'s start with the syntaxes. We\'ll use the example of \"Spam~\"")
    spam()

    print("We\'re now talking about the caculations of python.")
    caculate()

    print("Here is some basic functions of python")
    #basic()

def spam():
    print("At the time you execute the code, Python will check the syntax before starting any code.")
    print("Check this out!")

    print("""
        spam = 0
        print(spam)
          
        spam = spam + 4
        print(spam) 
        
        if spam > 0:
            print("But I don't want ANY spam!")
        
        viking = "spam" * spam
        print(viking)
            """)

def caculate():
    print("For this, let\'s explain some operators in Python.")

    operators = ["+", "-", "*", "/", "//", "%", "**"]
    operations = ["addtion", "subtraction", "multiplication", "true division", 
                  "floor division(with only full numbers)", "modulus", "exponmentation"]
    for x in range(len(operators)):
        op = ""
        oper = ""
        count1 = -1
        op = operators[count1]
        oper = operations[count1]
        print(f"\"{op}\" is for \"{oper}\"")
        count1 += 1
        
entry()