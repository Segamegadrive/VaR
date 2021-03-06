# Sagar Gurung, MSc Cloud Computing, University of Surrey

import csv
import numpy


def parseMicrosoft():
    with open('microsoft-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[7])
        return newArray


def calcVar(datapoints, investment):
    unsortedRS = parseMicrosoft()
    print "Unsorted Return Series: {}".format(unsortedRS)

    unsortedRS = unsortedRS[0:datapoints]
    print "Unsorted selected RS: {}".format(unsortedRS)

    # Loops through num 1 to given datapoints value. It matches the CSV file given number range from 1 to 8044.
    # Therefore, the datapoints value shouldn't exceed more than 8044
    for i in range(1, datapoints, datapoints):
        floatURS = [float(i) for i in unsortedRS]
        print "Converted to float: {}".format(floatURS)

    # Sorting the selected datapoints values
    sortRS = sorted(floatURS)
    print "Sorted Return Series: {}".format(sortRS)

    totalCount = len(sortRS)  # find out if we need to do -1 here.
    print "The total number of datapoints counts: {}".format(totalCount)

    his95Position = (int(round(0.05 * totalCount)))
    print "The 95th position: {}".format(his95Position)

    his95Value = sortRS[his95Position] * investment
    print "Historical VaR at 95%: {}".format(his95Value)

    his99Position = (int(round(0.01 * totalCount)))
    print "The 99th position: {}".format(his99Position)

    his99Value = sortRS[his99Position] * investment
    print "Historical VaR at 99%: {}".format(his99Value)

    # Covariance
    totalSum = sum(sortRS)
    print "Total sum of given data points: {}".format(totalSum)
    mean = totalSum / totalCount
    print "Mean: {}".format(mean)

    standardDeviation = numpy.std(sortRS)
    print "Standard Deviation: {}".format(standardDeviation)

    cov95VaR = -(mean + (1.65 * standardDeviation)) * investment
    print "Covariance VaR at 95%: {}".format(cov95VaR)

    cov99VaR = -(mean + (2.33 * standardDeviation)) * investment
    print "Covariance VaR at 99%: {}".format(cov99VaR)


calcVar(8044, 1)




