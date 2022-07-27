import os
with open('test.csv', 'r') as file:
    filedata = file.read()
    filedata = filedata.replace(';', ',')

    with open('test.csv', 'w') as file:
        file.write(filedata)