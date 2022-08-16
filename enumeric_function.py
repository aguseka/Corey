# old way doing this

names = ['Eka','Desak', 'Satria', 'Ayu', 'Andra']

# index = 0
'''
for name in names:
    print(index, name,)
    index += 1
print("\n")
'''


# names = ['Eka','Desak', 'Satria', 'Ayu', 'Andra']
for urutan, name_1 in enumerate(names, start=1):
    print(urutan, name_1)

print("\n")

