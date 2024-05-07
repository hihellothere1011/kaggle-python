def xandy():
    x = "pluto is a planet"
    y = "pluto is a planet"
    print((x == y))
def specials():
    #print('Pluto's a planet!')#WRONG!!!
    print('Pluto\'s a planet!')
    print('What\'s up!')
    print("""Look, a mountain:
          /\\""")

def diffs():
    hello = "hello\nworld"
    print(hello)
    triplehello = """hello
    world"""
    print(triplehello)
    print(triplehello == hello)
planet = "Pluto"
def changes():
    print("hello")
    print("Pluto")
    print("hello",end='')
    print("Pluto",end='') 
    planet = "Pluto"
    print(planet[0])
    print(planet[-3:])
    print(len(planet))
    print([char +"!" for char in planet])
claim = "Pluto is a planet"
def methods():
    claim = "Pluto is a planet"
    print(claim.upper())
    print(claim.lower())
    print(claim.index("planet"))
    print(claim.startswith("planet"))
    print(claim.endswith("planet"))
    print(claim.split())


datestr = "1956-01-31"
year,month,day = datestr.split("-")
print("/".join([month,day,year]))
print(' 👏 '.join([w.upper() for w in claim]))
print(planet+", we miss you.")
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")
print("{}, you'll always be the {}th planet to me.".format(planet,position))

plutomass = 1.303 * 10**22
earthmass = 5.9722 * 10**24
population = 52910390
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, plutomass, plutomass/earthmass, population
))
print("@"*100)
num = {"one":1,"two":2}
print(num)
print(num["one"])
num["eleven"] = 11
print(num)
num["one"] = "Pluto"
print(num)
print("@"*100)
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet123 = {pl: pl[0] for pl in planets}
print(planet123)
print("@"*100)
for x in num:
    print(f"{x}={num[x]}")
print("@"*100)
print(" ".join(sorted(planet123.values())))
print("@"*100)
for planet,ott in planet123.items():
    print(f"{planet.rjust(10)} begins with \"{ott}\"")

z = "1234x"
for x in z:
    try:
        int(x)
    except :
        print(False)
    print(True)

import string
def findsindex():
    dl = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    for punc in string.punctuation:
        dl = [x.replace(punc,' ') for x in dl]
    kw = "casino"
    dl = [x.lower().split() for x in dl]
    kw = kw.lower()
    for index, x in enumerate(dl):
        for i in x:
            if i == kw: print(index)
findsindex()