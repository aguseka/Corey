# Multiple list with enumerate, the old way doing this.

actors = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = [' Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

print("This one without  zip function")
for urutan, actor in enumerate(actors):
    hero = heroes[urutan]
    print(f'{actor} is actually {hero}')
print("\n")
print("This one with  zip function \n ")

# now this is with the zip function

for actor, hero, universe in zip(actors, heroes, universes):
    print(f'{actor} is actually {hero} in {universe} comics')

for value in zip(actors, heroes, universes):
    print(value)