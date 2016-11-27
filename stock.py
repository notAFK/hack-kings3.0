''' This allows you to access the stock price of a company at any given
date and time up to the last 15 days
'''

import csv
import urllib2
import utils
import datetime
import calendar
import time

# INPUTS: Company name AND Date and Time (up to the second)
# OUTPUT: Stock price of company at that date and time

# Example link: # http://chartapi.finance.yahoo.com/instrument/1.0/AAPL/chartdata;type=quote;range=1d/csv


def epochToTimeStamp(epoch):
	epoch = float(epoch) # Makes sure its a float
	timestamp = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S') # Converts to specified format
	return timestamp # Returns seconds since 1/1/1970 (epoch)

def timeStampToEpoch(day, month, year, hour, minute, second):
	# Makes sure less than 10 values are double digits (e.g. 07)
	if (day < 10):
		day = '0' + str(day)
	if (month < 10):
		month = '0' + str(month)
	if (hour < 10):
		hour = '0' + str(hour)
	if (minute < 10):
		minute = '0' + str(minute)
	if (second < 10):
		second = '0' + str(second)


	date_time = str(day) + '.' + str(month) + '.' + str(year) + ' ' + str(hour) + ':' + str(minute) + ':' + str(second)
	pattern = '%d.%m.%Y %H:%M:%S' # Pattern to plug in supplied values
	epoch = int(time.mktime(time.strptime(date_time, pattern)))
	return epoch

def getDaysHistory(timestamp):
	current_timestamp = int(time.time())
	seconds_in_one_day = 60 * 60 * 24 # 86400
	days = int((current_timestamp - timestamp) / seconds_in_one_day)
	
	if (days == 0):
		days = 1 # Makes sure minimum day scrape is 1

	return str(days)


# Assumes timestamp is in epoch
def getStockPrices(company, start_time, end_time):
	ticker = utils.get_ticker(company) # Converts name to stock-friendly name

	daysHistory = getDaysHistory(start_time)
	# {TIME_STAMP, CLOSE, HIGH, LOW, OPEN, VOLUME}
	url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + ticker + '/chartdata;type=quote;range=' + daysHistory +'d/csv'
	response = urllib2.urlopen(url) # Stores url response (csv file)

	stock_data = [] # Stores read data

	spamreader = csv.reader(response, delimiter=' ', quotechar='|')
	stock_data = list(spamreader) # Makes csv into a list/array

	if (daysHistory == 1):
		stock_data = stock_data[17:]
	elif (daysHistory <= 15):
		stock_data = stock_data[18 + daysHistory:] # Store from the starting to the ending stock
	else:
		stock_data = stock_data[33:]

	stock_data = stock_data[17:]

	time_and_prices = []

	for item in stock_data:
		dataStamp = item[0].split(',') # Splits single array to multiple elements
		# dateStamp[0] == Epoch time stamp
		# if (timestamp <= int(dataStamp[0])):
		# 	return dataStamp[1] # Returns CLOSE price of stick

		if (int(dataStamp[0]) <= end_time):
			if (int(dataStamp[0]) >= start_time):
				time_and_prices += [[dataStamp[0], dataStamp[1]]]
		else:
			return time_and_prices


name = "Microsoft" # INPUT company name
start_time = timeStampToEpoch(25, 11, 2016, 14, 30, 14) # INPUT start date and time
end_time = timeStampToEpoch(25, 11, 2016, 17, 24, 56) # INPUT end date and time
# print start_time
stock_prices = getStockPrices(name, start_time, end_time)
for item in stock_prices:
	print name + " Price: " + item[1] + " at " + epochToTimeStamp(item[0])



