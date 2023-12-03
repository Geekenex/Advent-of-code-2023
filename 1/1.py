import re

inputFile = open('1/input.txt', 'r')
lines = inputFile.readlines()
 
calibrationValuesSum = 0
# Strips the newline character
for line in lines:
    calibrationValuesLine = re.sub("[^0-9]", "", line)
    if(len(calibrationValuesLine) == 1):
        calibrationValuesSum += int(str(calibrationValuesLine) + str(calibrationValuesLine))
    else:
        calibrationValuesSum += int(str(calibrationValuesLine[0]) + str(calibrationValuesLine[len(calibrationValuesLine)-1]))
print(calibrationValuesSum)