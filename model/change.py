import os
with open('survey.csv', 'r') as file:
    filedata = file.read()
    filedata = filedata.replace(';', ',')

    with open('survey.csv', 'w') as file:
        file.write(filedata)