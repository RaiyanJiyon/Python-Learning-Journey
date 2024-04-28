# Open a file using a context manager
with open('text1.txt', 'w') as file:
    file.write('Raiyan Jiyon\n')
    file.write('Sabbir Ahamed')

with open('text1.txt', 'r') as readfile:
    data = readfile.read()
    print(data)
# File is automatically closed outside the context manager