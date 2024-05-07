spam_amounts = 0
print(spam_amounts)

spam_amounts = spam_amounts + 4
if spam_amounts > 0:
    print("But I don't want ANY spam!")

viking_songs = "Spam "*spam_amounts
print(viking_songs)

print(type(spam_amounts))
print(type(19.95))

a = 100
b = 50
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(-a)

hat_height_cm = 25
my_height_cm = 190
total_height_meter = (hat_height_cm + my_height_cm)/100
print("Height in meters =",total_height_meter, "?")

print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(19.9))
print(int("807")+1)

pi = 3.14159
diameter = 3
radlus = diameter/2
area = radlus**2*pi
print(area)

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