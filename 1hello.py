def spam(spam_amounts:int)->str:
    """This is a the first example in the python course, you give the amount of spam and print that much of \"Spam\" """
    print(spam_amounts)

    spam_amounts = spam_amounts + 4
    if spam_amounts > 0:
        print("But I don't want ANY spam!")

    viking_songs = "Spam "*spam_amounts
    return viking_songs

def basic_math(a:int,b:int)->int:
    """This fuction explains how the basic math works in python"""
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)
    print(a%b)
    print(a**b)
    print(-a)
def height(hat:int,mine:int)->float:
    """"This function will caculate the total height of you and your hat, then it will return it in meters"""
    total_height_meter = (hat + mine)/100
    return("Height in meters =",total_height_meter, "?")

def minmax(a:int,b:int,c:int)->int:
    """This function will show you what the min() and max() do"""
    print(min(a, b, c))
    print(max(a, b, c))

def abs(num:int)->int:
    """This function shows us what the abs() do (It returns the absolute value of the number)"""
    return abs(num)

def area(pi:float, diameter:int):
    """This function caculates the area of a circle by giving it radius"""
    radlus = diameter/2
    area = radlus**2*pi
    return area

def changing():
    a = [1,2,3]
    b = [3,2,1]
    a1 = a
    a = b
    b = a1
    print(a)
    print(b)

ac = 121
bc = 77
cc = 109
to_smash = (ac+bc+cc) - (3*((ac + bc + cc)//3))
print(to_smash)