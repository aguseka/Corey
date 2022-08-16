# context manager works for database connection, opening file that require open and close.


f = open ("test.txt", 'r')
file_contents = f.read()

# This is very easy to forget. With context manager this is not required.
f.close()

words = file_contents.split(' ')
word_counts =  len(words)
print(word_count)


# Now using contxt manager

with open(" test.txt",'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_counts =  len(words)
print(word_count)
