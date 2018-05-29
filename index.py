#6397857 Cloud Computing Part b
import os
import webapp2
import jinja2
import csv
import numpy
import httplib
import random
import math

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment( loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

def doRender(handler, tname, values={}):
	temp = os.path.join(os.path.dirname(__file__), 'templates/'+tname)
	if not os.path.isfile(temp):
		doRender(handler, 'index.htm')
		return

	# Make a copy of the dictionary and add the path
	newval = dict(values)
	newval['path'] = handler.request.path

	template = jinja_environment.get_template(tname)
	handler.response.out.write(template.render(newval))
	return True

def parseMicrosoft():
    with open('microsoft-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[7])
        return newArray


def parseAmazon():
    with open('amazon-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[7])
        return newArray

def parseBitcoin():
    with open('bitcoin-DataAnalysis.csv', 'r') as csvfile:
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

def parseAmazonAdjClose():
    with open('amazon-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[5])
            #firstVal = newArray[0:1]
        return newArray

def parseBitcoinAdjClose():
    with open('bitcoin-DataAnalysis.csv', 'r') as csvfile:
        newArray = []
        readCSV = csv.reader(csvfile)
        header = next(readCSV)
        for row in readCSV:
            newArray.append(row[5])
            #firstVal = newArray[0:1]
        return newArray







def calcVar(funcCompanies, datapoints, investment):	
	if (funcCompanies == 'microsoft'):
		a = parseMicrosoft()
	elif (funcCompanies == 'amazon'):
		a = parseAmazon()
	elif (funcCompanies == 'bitcoin'):
		a = parseBitcoin()
	else:
		print("Please select company")	

	unsortedRS = a
	unsortedRS = unsortedRS[0:datapoints]
	for i in range(1, datapoints, datapoints):
		floatURS = [float(i) for i in unsortedRS]
    	sortRS = sorted(floatURS)
    	totalCount = len(sortRS)
    	his95Position = (int(round(0.05 * totalCount)))
    	his95Value = sortRS[his95Position] * investment
    	his99Position = (int(round(0.01 * totalCount)))
    	his99Value = sortRS[his99Position] * investment

    	#Covariance
    	totalSum = sum(sortRS)
    	mean = totalSum/totalCount
    	standardDeviation = numpy.std(sortRS)
    	cov95VaR = -(mean+(1.65*standardDeviation))*investment
    	cov99VaR = -(mean + (2.33 * standardDeviation)) * investment

#     Monte Carlo
	#global firstVal

    	if (funcCompanies == 'microsoft'):
        	firstVal = parseMicrosoftAdjClose()
        	for i in range(1, datapoints):
            		firstVal = [float(i) for i in firstVal]
            		adjCloseFirstVal = firstVal[0]

    	elif (funcCompanies == 'amazon'):
        	firstVal = parseAmazonAdjClose()
        	for i in range(1, datapoints):
            		firstVal = [float(i) for i in firstVal]
            		adjCloseFirstVal = firstVal[0]

	elif (funcCompanies == 'bitcoin'):
        	firstVal = parseBitcoinAdjClose()
        	for i in range(1, datapoints):
            		firstVal = [float(i) for i in firstVal]
            		adjCloseFirstVal = firstVal[0]
	else:
		print("Find a company")
    	randomArray = []
    	for r in range(1, datapoints + 1):
        	randomNum = random.gauss(mean, standardDeviation) * r
        	randomArray.append(randomNum)

    	newAdjCloseValues = []
    	firstVal = (1 + randomArray[0]) * adjCloseFirstVal
    	newAdjCloseValues.append(firstVal)

    	for a in range(1, datapoints):
        	newPrice = (1 + randomArray[a]) * newAdjCloseValues[a - 1]
        	newAdjCloseValues.append(newPrice)

    	newReturnSeries = []
    	for b in range(1, datapoints):
        	newRSeries = (newAdjCloseValues[b] - newAdjCloseValues[b - 1]) / newAdjCloseValues[b]
        	newReturnSeries.append(newRSeries)
	sortNewRS = sorted(newReturnSeries)
	totalCountNewRS = len(sortNewRS)
	monte95Position = (int(round(0.05 * totalCountNewRS)))
	monte99Position = (int(round(0.01 * totalCountNewRS)))
	monte95Value = sortNewRS[monte95Position] * investment
	monte99Value = sortNewRS[monte99Position] * investment
	
	if (funcCompanies == 'microsoft'):
		json='{"key1":"funcCompanies", "key2":'+str(adjCloseFirstVal)+', "key3":'+str(datapoints)+', "key4":'+str(investment)+', "key5":'+str(mean)+', "key6":'+str(standardDeviation)+'}'

	elif (funcCompanies == 'amazon'):
		json='{"key1": "funcCompanies", "key2":'+str(adjCloseFirstVal)+', "key3":'+str(datapoints)+', "key4":'+str(investment)+', "key5":'+str(mean)+', "key6":'+str(standardDeviation)+'}'
	
	elif (funcCompanies == 'bitcoin'):
		json='{"key1": "funcCompanies", "key2":'+str(adjCloseFirstVal)+', "key3":'+str(datapoints)+', "key4":'+str(investment)+', "key5":'+str(mean)+', "key6":'+str(standardDeviation)+'}'
	
	else:
		print("Get company")
	
	c = httplib.HTTPSConnection("cxxdtitwfd.execute-api.eu-west-2.amazonaws.com")
	c.request("POST","/prod",json)
	response = c.getresponse()
	data = response.read()
	#return data
	dataOne = data.replace("[", "")
	dataTwo = data.replace("]", "")
	dataSplitOne = dataOne.split(',')
	dataSplitTwo = dataTwo.split(',')
	monte95Data = dataSplitOne[0]
	monte99Data = dataSplitTwo[1]

	return his95Value, his99Value, cov95VaR, cov99VaR, monte95Value, monte99Value, monte95Data, monte99Data

#def calcMonte(funcCompanies, datapoints, investment):
	#mean, standardDeviation = calVar(funcCompanies, datapoints, investment)
	#if (funcCompanies == 'microsoft'):
		#json='{"key2":'+str(newFirstVal)+', "key3":'+str(datapoints)+', "key4":'+str(investment)+', "key5":'+str(mean)+', "key6":'+str(standardDeviation)+'}'

	#elif (funcCompanies == 'amazon'):
		#json='{"key2":'+str(newFirstVal)+', "key3":'+str(datapoints)+', "key4":'+str(investment)+', "key5":'+str(mean)+', "key6":'+str(standardDeviation)+'}'

		#c = httplib.HTTPSConnection("cxxdtitwfd.execute-api.eu-west-2.amazonaws.com")
		#c.request("POST","/prod",json)
		#response = c.getresponse()
		#data = response.read()
		#return data
	

class CalculateHandler(webapp2.RequestHandler):
	def post(self):
		funcCompanies = self.request.get('company')
		datapoints = int(self.request.get('datapoints'))
		investment = int(self.request.get('investment'))
		# adjCloseFirstVal = self.request.get('adjCloseFirstVal')
		# mean = self.request.get('mean')
		# standardDeviation = self.request.get('standardDeviation')

		if funcCompanies == '' or datapoints == '' or investment == '':
			doRender(
					self,
					'index.htm',
					{'note': 'Please insert all values!'})
		elif funcCompanies == 'microsoft' or funcCompanies == 'amazon' or funcCompanies == "bitcoin":
			his95Value, his99Value, cov95VaR, cov99VaR, monte95Value, monte99Value, monte95Data, monte99Data = calcVar(funcCompanies, datapoints, investment)
			doRender(self, 'chart.htm', {'Company': funcCompanies, 'Datapoints': datapoints,'Investment':investment, 'data': str(his95Value), 'data1': str(his99Value), 'data2': str(cov95VaR), 'data3': str(cov99VaR), 'monte95': str(monte95Value), 'monte99': str(monte99Value), 'monte95Lambda': str(monte95Data), 'monte99Lambda': str(monte99Data)})
		else:
			doRender(self,'index.htm', {'note': 'Please insert all values again'})

class MainPage(webapp2.RequestHandler):
	def get(self):
		path = self.request.path
		doRender(self, path)

app = webapp2.WSGIApplication([('/calculate', CalculateHandler),('/.*', MainPage)],
							  debug=True)
