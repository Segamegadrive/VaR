import csv
import numpy
import random

def parseMicrosoft():
    with open('microsoft-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[7])
        return newArray

def parseMicrosoftAdjClose():
    with open('microsoft-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[5])
        return newArray

def parseAmazon():
    with open('amazon-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[7])
        return newArray

def parseAmazonAdjClose():
    with open('amazon-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[5])
        return newArray


def meanStdAdjFirstValCalculator(funcCompanies, adjClose, datapoints, investment):
    if (funcCompanies == 'microsoft'):
        a = parseMicrosoft()
    if (funcCompanies == 'amazon'):
        a = parseAmazon()

    if (adjClose == 'microsoft'):
        b = parseMicrosoftAdjClose()
    if (adjClose == 'amazon'):
        b = parseAmazonAdjClose()

    unsortedRS = a
    unsortedRS = unsortedRS[0:datapoints]
    for i in range(1, datapoints, datapoints):
        floatURS = [float(i) for i in unsortedRS]
    sortRS = sorted(floatURS)
    totalCount = len(sortRS)
    totalSum = sum(sortRS)
    mean = totalSum / totalCount
    print(mean)
    standardDeviation = numpy.std(sortRS)
    print(standardDeviation)

    adjCloseVal = b
    for i in range(1, datapoints, datapoints):
        adjCloseValFloat = [float(i) for i in adjCloseVal]
        adjCloseFirstVal = adjCloseValFloat[0]
    print(adjCloseFirstVal)



def calcMonte(funcCompanies, datapoints, investment):
    if (funcCompanies == 'microsoft'):
        mean, standardDeviation, adjCloseFirstVal = meanStdAdjFirstValCalculator()
        print(mean, standardDeviation, adjCloseFirstVal)


calcMonte(parseMicrosoft(), 10, 1)
meanStdAdjFirstValCalculator(parseMicrosoft(), parseMicrosoftAdjClose(), 10, 1)





