planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

s = '''steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe,
message, image, Or video.'''
for char in s:
    if s.isupper():
        print(char, end=' ')

for i in range(5):
    print("doing important works. i =",i)

x = 0
while x < 10:
    print(x)
    x += 1

squares = [x**2 for x in range(10)]
print(squares)
short_planets = [p for p in planets if len(p)<6]
print(short_planets)
lsp = [p.upper()+"!" for p in planets if len(p)<6]
print(lsp)

def negatives(num):
    count = 0
    for x in num:
        if x < 0:
            count += 1
    return count
print(negatives([-2342,5678,-0,373.9,-9876]))

def easy_negative(num):
    return len([n for n in num if n < 0])
print(easy_negative([-2342,5678,-0,373.9,-9876]))

def easy(num):
    return sum([n < 0 for n in num])
print(easy([-2342,5678,-0,373.9,-9876]))

