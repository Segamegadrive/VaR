# Sagar Gurung, MSc Cloud Computing, University of Surrey

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

# def drawTimeReturnSeries():
#     with open('microsoft-DataAnalysis.csv', 'r') as csvfile:
#         newArray = []
#         readCSV = csv.reader(csvfile)
#         header = next(readCSV)
#         for row in readCSV:
#             newArray.append(row[5])
#             floatSeries = [float(row) for row in newArray ]
#         return floatSeries

def calcVar(funcCompanies, datapoints, investment):

    unsortedRS = funcCompanies
    print "Unsorted Return Series: {}".format(unsortedRS)

    unsortedRS = unsortedRS[0:datapoints]
    print "Unsorted selected RS: {}".format(unsortedRS)

    # Loops through num 1 to given datapoints value. It matches the CSV file given number range from 1 to 8044.
    # Therefore, the datapoints value shouldn't exceed more than 8044
    for i in range(1, datapoints, datapoints):
        floatURS = [float(i) for i in unsortedRS]
        print "Converted to float: {}" .format(floatURS)

    # Sorting the selected datapoints values
    sortRS = sorted(floatURS)
    print "Sorted Return Series: {}".format(sortRS)

    totalCount = len(sortRS)   #find out if we need to do -1 here.
    print "The total number of datapoints counts: {}".format(totalCount)

    his95Position = (int(round(0.05 * totalCount)))
    print "The 95th position: {}".format(his95Position)

    his95Value = sortRS[his95Position] * investment
    print "Historical VaR at 95%: {}".format(his95Value)

    his99Position = (int(round(0.01 * totalCount)))
    print "The 99th position: {}".format(his99Position)

    his99Value = sortRS[his99Position] * investment
    print "Historical VaR at 99%: {}".format(his99Value)


    #Covariance
    totalSum = sum(sortRS)
    print "Total sum of given data points: {}".format(totalSum)
    mean = totalSum/totalCount
    print "Mean: {}".format(mean)

    standardDeviation = numpy.std(sortRS)
    print "Standard Deviation: {}".format(standardDeviation)

    cov95VaR = -(mean+(1.65*standardDeviation))*investment
    print "Covariance VaR at 95%: {}".format(cov95VaR)

    cov99VaR = -(mean + (2.33 * standardDeviation)) * investment
    print "Covariance VaR at 99%: {}".format(cov99VaR)


def calcMonte(funcCompanies, adjClose, datapoints, investment):
    unsortedRS = funcCompanies
    unsortedRS = unsortedRS[0:datapoints]
    for i in range(1, datapoints, datapoints):
        floatURS = [float(i) for i in unsortedRS]
        sortRS = sorted(floatURS)
        totalCount = len(sortRS)
        totalSum = sum(sortRS)

        mean = totalSum / totalCount
        print "new mean: {}".format(mean)
        standardDeviation = numpy.std(sortRS)
        print "new standard deviation: {}".format(standardDeviation)

    adjCloseVal = adjClose
    for i in range(1, datapoints, datapoints):
        adjCloseValFloat = [float(i) for i in adjCloseVal]
        adjCloseFirstVal = adjCloseValFloat[0]
        print "First old value in Adj Close Column: {} ".format(adjCloseFirstVal)


    numOfDataPoints = datapoints
    for r in range(1, numOfDataPoints+1):
        randomArray = []
        randomNum = random.gauss(mean, standardDeviation) * r
        randomArray.append(randomNum)
        print(randomArray)

    newAdjCloseValues = []
    firstNewAdjClosePrice = (1 + randomArray[0])*adjCloseFirstVal
    newAdjCloseValues.append(firstNewAdjClosePrice)
    print(newAdjCloseValues)

    for i in range(1, numOfDataPoints):
        newAdjCloseValuesList = (1 + randomArray[i])*newAdjCloseValues[i+1]
        print(newAdjCloseValuesList)





        # print "List of random numbers: {}".format(randomArray)
        # for row in randomArray:
        #     newAdjClosePriceList = []
        #     newAdjClosePrice = ((1 + row) * adjCloseFirstVal)
        #     newAdjClosePriceList.append(newAdjClosePrice)
            # print (newAdjClosePriceList)

            # newAdjClosePriceArray = numpy.asarray(newAdjClosePriceList)
            # print (newAdjClosePriceArray)

            # print "New Adj Close Price: {}".format(newAdjClosePriceArray)

            # newReturnSeries = (newAdjClosePriceArray[0] - newAdjClosePriceArray[1])/newAdjClosePriceArray[1]
            # print(newReturnSeries)






# calcVar(parseMicrosoft(),8044,1)

calcMonte(parseMicrosoft(), parseMicrosoftAdjClose(), 20, 1)




