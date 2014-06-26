# coding=utf-8
################################################
# Program : TocHW3.py
# Coder :  陳彥清 ( yChing )
# Student ID :  F74002086
# Description : parsing housing data from the website using json 
# How to use : python TocHW3.py <url> <dist> <road> <year>
# Example use : python main.py http://www.datagarage.io/api/5365dee31bc6e9d9463a0057 楊梅市 金山街 101
# Reference : http://www.crifan.com/summary_what_is_json_and_how_to_process_json_string/
# Reference : http://andylin02.iteye.com/blog/845355
################################################
import urllib # get data from the website | another choose is urllib2
import sys # command line input | python main.py arg1 arg2 arg3
import json
import re  #parsing json


def parsing(data, iDists, iRoad, iYear):
	
	#chinese needs to be converted to unicode
	getDists = unicode("鄉鎮市區", "utf-8")
	getRoad = unicode("土地區段位置或建物區門牌", "utf-8")
	getYear = unicode("交易年月", "utf-8")
	getPrice = unicode("總價元", "utf-8")

	
	# inputed chinese should be  converted utf-8 to unicode
	iDists = unicode(iDists, "utf-8")
	iRoad = unicode(iRoad, "utf-8")
	iYear = int(iYear)

	# regular expression 
	pattern1 = re.compile(iDists)
	pattern2 = re.compile(iRoad)

	
	count = 0 #muched result
	TotalMoney = 0 # total money of  the fined data

	# find which data is matched
	for i in range(len(data)):
		# match is a bool type. (return by search in re)
		matchDists = pattern1.search(data[i][getDists])
		matchRoad = pattern2.search(data[i][getRoad])

		tYear = str(data[i][getYear])
		if iYear <= int(tYear[:-2]):
			matchYear = True
		else:
			matchYear = False


		if matchDists and matchRoad and matchYear:
			count += 1
			FinalDists = json.dumps(data[i][getDists], ensure_ascii=False).encode('utf-8')
			FinalRoad = json.dumps(data[i][getRoad], ensure_ascii=False).encode('utf-8')
			FinalYear = json.dumps(data[i][getYear], ensure_ascii=False).encode('utf-8')
			FinalPrice = json.dumps(data[i][getPrice], ensure_ascii=False).encode('utf-8')
			FinalDists = re.sub('"(.*?)"', r'\1', FinalDists)  # delete " " ("Dists" --> Dists)
			FinalRoad = re.sub('"(.*?)"', r'\1', FinalRoad)  # delete " " ("Road" --> Road)
			TotalMoney += data[i][getPrice]
			print FinalDists + '    ' + FinalRoad + '    ' + FinalYear + '    ' + FinalPrice

	try:
		AvgMoney = TotalMoney / count
	except ZeroDivisionError:
		print 0
		return

	print AvgMoney

def main():

	#check the command line input 
	if len(sys.argv) != 5:
		print 'Error !!  Do --> TOC_HW3.py <url> <dist> <road> <year>'
		sys.exit(0)
	else:
		url, dists, road, year = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

	page = urllib.urlopen(url) #load json from the web
  	data = json.load(page)  #json to python list(dictionary)

	parsing(data, dists, road, year)

if __name__ == '__main__':
	main()