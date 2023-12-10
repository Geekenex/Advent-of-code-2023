inputFile = open('2/input.txt', 'r')
lines = inputFile.readlines()

powerSum = 0
for line in lines:
    blueNeeded = 0
    redNeeded = 0
    greenNeeded = 0
    lineInfo = line.split(':')
    gameNumber = int(lineInfo[0].replace('Game ', ''))
    cubeInfo = lineInfo[1].split(';')
    for cubeEntry in cubeInfo:
        cubeCounts = cubeEntry.split(',')
        for cubeCount in cubeCounts:
            cubeColor = cubeCount.strip().split(' ')[1]
            cubeAmount = int(cubeCount.strip().split(' ')[0])
            if(cubeColor == 'blue'):
                if(cubeAmount > blueNeeded):
                    blueNeeded = cubeAmount
            elif(cubeColor == 'red'):
                if(cubeAmount > redNeeded):
                    redNeeded = cubeAmount
            elif(cubeColor == 'green'):
                if(cubeAmount > greenNeeded):
                    greenNeeded = cubeAmount
    powerSum += greenNeeded * redNeeded * blueNeeded
    print(powerSum)

        
