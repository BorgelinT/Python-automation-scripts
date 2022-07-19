trimFile = open('trimtext.txt', 'r')
Lines = trimFile.readlines()
resultFile = open('result.txt', 'w+')


count = 0
for line in Lines:

    # get the first string inside quotations and ignore odd quotes
    Lines[count] = Lines[count].split('"')[1::2][0]

    # angular formbuilder
    #resultFile.write(Lines[count] + ': [\'\'],\n') 

    # just the strings, separeted by linebreaks
    resultFile.write(Lines[count] + '\n') 
    count += 1

resultFile.close()

input('Press Enter to exit')