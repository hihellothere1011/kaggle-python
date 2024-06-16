import time

def pause(t=1):
    time.sleep(t)

def entry():
    pause()

    print("\nThis is the first lesson you\'ll start, it\'s talking about the syntax, the variables, and the operators.")
    pause()

    print("\nLet\'s start with the syntaxes. We\'ll use the example of \"Spam~\"")
    pause()
    spam()

    print("\nWe\'re now talking about the caculations of python.")
    caculate()

    print("\nHere is some basic functions of python")
    #basic()

def spam():
    print("\nAt the time you execute the code, Python will check the syntax before starting any code.")
    pause()
    print("\nCheck this out!")
    pause()

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
    pause()

    print("\nThere is no mistake so this code can run.")
    pause()
    print("\nHere is another easy example:")
    pause()
    print("""
        import winsound
        import time

        def beep(f=1000, d=100):
            for x in range(1,3):
                winsound.Beep(f, d)
                time.sleep(0.1)

        def reminder(t=300):
            while(True):
                beep()
                time.sleep(t)

        reminder()
            """)
    pause()

    print("\nQuite strange, huh?(Why is this thing here???)")
    pause()
    print("\nWe just need to know there is no any mistake so it can work.(Don\'t care about what it is)")
    pause()

def caculate():
    pause()
    print("\nNow, we\'re at the part of understanding the operations.")
    pause()

    print("\nFirst, let\'s explain some operators in Python.")
    pause()
    operators = ["+", "-", "*", "/", "//", "%", "**"]
    operations = ["addtion", "subtraction", "multiplication", "true division", 
                  "floor division(with only full numbers)", "modulus", "exponmentation"]
    for x in range(len(operators)):
        op = ""
        oper = ""
        count1 = x
        op = operators[count1]
        oper = operations[count1]
        print(f"\n\"{op}\" is for \"{oper}\"")
        pause()
    print("\nThese are the basic operations.")
    pause()

    print("\nBy the way, have you heard of PEMDAS?")
    pause()
    print("\nPEMDAS is the order of the mathematic caculations.(Parentheses, Exponments, Mutiplications/Divisions, Additions/Subtractions)")
    pause()
    print("\nPython system follows the rules of PEMDAS automatically.")
    pause()
    print("\nLike \"1 + 3 * 8 - 4\", it gives the result of \"21\" rather than \"28\".")
    

if __name__ == "__main__":
    entry()