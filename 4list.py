planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def indexing():
    print(planets[0])
    print(planets[1])
    print(planets[-1])
    print(planets[-2])
    print(planets[0:3])
    print(planets[:3])
    print(planets[3:])
    print(planets[1:-1])
indexing()
def changing_lists():
    print(planets)
    planets[3] = 'Malacandra'
    print(planets)
    planets[:3] = ['Mur', 'Vee', 'Ur']
    print(planets)
    planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
changing_lists()
def list_functions():
    print(len(planets))
    print(sorted(planets))
    primes = [2,3,5,7]
    print(sum(primes))
    print(max(primes))
list_functions()
def objects():
    x = 12
    print(x.imag)
    c = 12+3j
    print(c.imag)
    print(x.bit_length())
objects()
def list_methods():
    planets.append("Pluto")
    print(planets)
    print(planets.pop())
    print(planets)
    print(planets.index("Earth"))
    print("Earth" in planets)
    print("asdfghjkloiuytrewq" in planets)
list_methods()
def tuples():
    t = (1,2,3)
    print(t)
    t = 1,2,3
    print(t)
    x = 0.125
    print(x.as_integer_ratio())
tuples()