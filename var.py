# Sagar Gurung, MSc Cloud Computing, University of Surrey

import csv

def parseMicrosoft():
    with open('microsoft-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[7])
        return newArray

def calcHistorical(datapoints, investment):

    unsortedRS = parseMicrosoft()
    print "Unsorted Return Series: {}".format(unsortedRS)

    unsortedRS = unsortedRS[0:datapoints]
    print "Unsorted selected RS: {}".format(unsortedRS)

    sortRS = sorted(unsortedRS)
    print "Sorted Return Series: {}".format(sortRS)

    totalCount = len(sortRS)-1 #find out if we need to do -1 here.
    print "The total number of datapoints counts: {}".format(totalCount)

    his95Position = (int(round(0.05 * totalCount)))
    print "The 95th position: {}".format(his95Position)

    his95Value = sortRS[his95Position] * investment
    print "The 95th position value: {}".format(his95Value)


calcHistorical(8045,1)










# dataPoints = input('Please enter last number of days')
# investment = input('Please enter the investment')

#
# newArray = []
# def calHistorical():
#     with open('microsoft-DataAnalysis.csv', 'r') as csvfile:
#         readCSV = csv.reader(csvfile)
#         header = next(readCSV)
#         for row in readCSV:
#             rs = float(row[7])
#             newArray.append(rs)
#             return newArray
#             # print (newArray)
# sort_returnSeries = sorted(newArray)
# print (sort_returnSeries)
#
# calHistorical()



