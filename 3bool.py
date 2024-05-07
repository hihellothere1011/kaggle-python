print(""" 
 a == b	a equal to b		
 a != b	a not equal to b
 a < b	a less than b		
 a > b	a greater than b
 a <= b	a less than or equal to b		
 a >= b	a greater than or equal to b""")

def president(age:int)->bool:
    """Can someone of the given age run for president in the US?"""
    return age >= 35
print("Can a 19-year-old run a president?",president(19))
print("Can a 45-year-old run a president?",president(45))

def president2(age,citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    return citizen and age >= 35
print(president2(19,True))
print(president2(39,False))
print(president2(64,True))

def odd(num:int)->bool:
    """this function returns true or false if the number you return is an odd number"""
    return num % 2 == 0
print("Is 100 an odd?",odd(100))
print("Is 131 an odd?",odd(131))

def orand(n=None)->bool:
    """this function returns the result of "True or True and False" """    
    return True or True and False
orand()

def whatsx(x:int)->str:
    """this function returns the relationship of x and 0"""
    if x == 0:
        print(x,"is 0")
    elif x > 0:
        print(x,"is positve")
    elif x < 0:
        print(x, "is negative")
    else:
        print("It's nothing")
whatsx(0)
whatsx(153)
whatsx(-25)

print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))

if 0:
    print(0)
elif "spam":
    print("spam")

print(int(True))

def sign1(n):
    if n<0:
        return -1
    elif n>0:
        return 1
    else:
        return 0 
print(sign1(2345678))
print(sign1(-1234))
print(sign1(0))
