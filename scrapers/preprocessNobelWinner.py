nobelfile = open('nobel.csv').readlines()
outputFile = open('nobel_preprocessed.csv', 'wb')


firstLine = True
validPrizes = ['chemistry', 'medicine', 'physics'] 
validWinners = []
for line in nobelfile:
    data = line.split(',')
    if firstLine:
        firstLine = False
    else:
        prizeType = data[1]
        if prizeType in validPrizes:
            outputFile.write(line)
