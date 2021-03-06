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
            # firstVal = newArray[0:1]
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

def parseBitcoin():
    with open('bitcoin-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[7])
        return newArray

def parseBitcoinAdjClose():
    with open('bitcoin-DataAnalysis.csv', 'r') as csvfile:
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

#     Monte Carlo

    if (funcCompanies == parseMicrosoft()):
        firstVal = parseMicrosoftAdjClose()
        for i in range(1, datapoints):
            firstVal = [float(i) for i in firstVal]
            adjCloseFirstVal = firstVal[0]
        print "First old value in Adj Close Column: {} ".format(adjCloseFirstVal)

    elif (funcCompanies == parseAmazon()):
        firstVal = parseAmazonAdjClose()
        for i in range(1, datapoints):
            firstVal = [float(i) for i in firstVal]
            adjCloseFirstVal = firstVal[0]
        print "First old value in Adj Close Column: {} ".format(adjCloseFirstVal)

    elif (funcCompanies == parseBitcoin()):
        firstVal = parseBitcoinAdjClose()
        for i in range(1, datapoints):
            firstVal = [float(i) for i in firstVal]
            adjCloseFirstVal = firstVal[0]
        print "First old value in Adj Close Column: {} ".format(adjCloseFirstVal)
    else:
        print("Please find companies")

    randomArray = []
    for r in range(1, datapoints + 1):
        randomNum = random.gauss(mean, standardDeviation) * r
        randomArray.append(randomNum)
    # print(randomArray)

    newAdjCloseValues = []
    firstVal = (1 + randomArray[0]) * adjCloseFirstVal
    newAdjCloseValues.append(firstVal)

    for a in range(1, datapoints):
        newPrice = (1 + randomArray[a]) * newAdjCloseValues[a - 1]
        newAdjCloseValues.append(newPrice)
    print "New adj close value: {}".format(newAdjCloseValues)

    newReturnSeries = []
    for b in range(1, datapoints):
        newRSeries = (newAdjCloseValues[b] - newAdjCloseValues[b - 1]) / newAdjCloseValues[b]
        newReturnSeries.append(newRSeries)
    print "New return series: {}".format(newReturnSeries)

    sortNewRS = sorted(newReturnSeries)
    print"sorted rs {}".format(sortNewRS)
    totalCountNewRS = len(sortNewRS)

    monte95Position = (int(round(0.05 * totalCountNewRS)))
    print(monte95Position)

    monte99Position = (int(round(0.01 * totalCountNewRS)))
    print(monte99Position)

    monte95Value = sortNewRS[monte95Position] * investment
    monte99Value = sortNewRS[monte99Position] * investment
    print(monte95Value)
    print(monte99Value)
















# def calcMonte(funcCompanies, adjClose, datapoints, investment):
#     unsortedRS = funcCompanies
#     unsortedRS = unsortedRS[0:datapoints]
#     for i in range(1, datapoints, datapoints):
#         floatURS = [float(i) for i in unsortedRS]
#         sortRS = sorted(floatURS)
#         totalCount = len(sortRS)
#         totalSum = sum(sortRS)
#
#         mean = totalSum / totalCount
#         print "new mean: {}".format(mean)
#         standardDeviation = numpy.std(sortRS)
#         print "new standard deviation: {}".format(standardDeviation)
#
#
#     adjCloseVal = adjClose
#     for i in range(1, datapoints, datapoints):
#         adjCloseValFloat = [float(i) for i in adjCloseVal]
#         adjCloseFirstVal = adjCloseValFloat[0]
#         print "First old value in Adj Close Column: {} ".format(adjCloseFirstVal)


    # numOfDataPoints = datapoints

    # randomArray = []
    # for r in range(1, datapoints+1):
    #     randomNum = random.gauss(mean, standardDeviation) * r
    #     randomArray.append(randomNum)
    # print(randomArray)


    # newAdjCloseValues = []
    # firstVal = (1+randomArray[0])*adjCloseFirstVal
    # newAdjCloseValues.append(firstVal)
    #
    # for a in range(1, datapoints):
    #     newPrice = (1 + randomArray[a])*newAdjCloseValues[a-1]
    #     newAdjCloseValues.append(newPrice)
    # print(newAdjCloseValues)


    # newReturnSeries = []
    # for b in range(0, datapoints):
    #     newRSeries = (newAdjCloseValues[b] - newAdjCloseValues[b-1])/newAdjCloseValues[b]
    #     newReturnSeries.append(newRSeries)
    # print(newReturnSeries)
    #
    #
    # sortNewRS = sorted(newReturnSeries)
    # print(sortNewRS)
    #
    # totalCountNewRS = len(sortNewRS)
    # print(totalCountNewRS)
    #
    # monte95Position = (int(round(0.05 * totalCountNewRS)))
    # print(monte95Position)
    #
    # monte99Position = (int(round(0.01 * totalCountNewRS)))
    # print(monte99Position)
    #
    # monte95Value = sortRS[monte95Position] * investment
    # monte99Value = sortRS[monte99Position] * investment
    # print(monte95Value)
    # print(monte99Value)




calcVar(parseMicrosoft(),20,1)

# calcMonte(parseMicrosoft(), parseMicrosoftAdjClose(), 10, 1)
# parseAmazonAdjClose()




