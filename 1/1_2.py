import regex as re

inputFile = open('1/input.txt', 'r')
lines = inputFile.readlines()
letterValues = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

def rreplace(s, old, new):
    return (s[::-1].replace(old[::-1],new[::-1], 1))[::-1]

calibrationValuesSum = 0

for line in lines:
    numberLine = line
    #word into number
    foundWords = re.findall('|'.join(letterValues), numberLine, overlapped=True)
    if len(foundWords) > 0:
        lowWord = foundWords[0]
    if len(foundWords) > 1:
        highWord = foundWords[len(foundWords)-1]
    
    numberLine = line.replace(lowWord, str(letterValues.get(lowWord)), 1)
    numberLine = rreplace(numberLine, highWord, str(letterValues.get(highWord)))
    #keep only digits
    numberLine = re.sub("[^0-9]", "", numberLine)
    if(len(numberLine) == 1):
        calibrationValuesSum += int(str(numberLine) + str(numberLine))
    elif(len(numberLine) > 1):
        calibrationValuesSum += int(str(numberLine[0]) + str(numberLine[len(numberLine)-1]))
print(calibrationValuesSum)