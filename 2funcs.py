def least_difference(a:int,b:int,c:int)->int:
    """this function returns the least difference of the three arguments"""
    diff1 = a - b
    diff2 = b - c
    diff3 = a - c
    return min(diff1,diff2,diff3)
print(least_difference(10,50,250))

print(1,2,3,sep="<")

def greet(who = "Austin")->str:
    """this function returns 'hello who' and returns 'hello Austin' if the argument is empty """
    print("Hello",who)
print(greet("Sam"))

def mod(x:int)->int:
    """Return the remainder of x after dividing by 5"""
    return x % 5
print(mod(12345678987654321))

def round_to_two(num:float)->float:
    """this function returns the argument into floats with two decimal places"""
    return round(num,2)
print(round_to_two(0.363735272))

def nn(num:float)->float:
    """this function returns the argument become floats that back up with two decimal places """
    return round(num,-2)
print(nn(123.456))

def smash(candies,friends=3):
    """this function returns the candies that need to be smash"""
    return candies%friends
print(smash(1234567,12))
x = True
print(x)
type(x)