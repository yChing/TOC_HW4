# coding=utf-8
################################################
# Program : TocHW4.py
# Coder :  陳彥清 ( yChing )
# Student ID :  F74002086
# Description : parsing housing data from the website using json 
# How to use : python TocHW4.py <url> 
# Example use : python TocHW4.py http://www.datagarage.io/api/5385b69de7259bb37d925971
#Output: "臺中市南區忠明南路, 最高成交價:9500000, 最低成交價:3960000
#                 臺中市后里區墩北里大興路, 最高成交價:10000000, 最低成交價:9380000"
# Reference : http://www.crifan.com/summary_what_is_json_and_how_to_process_json_string/
# Reference : http://andylin02.iteye.com/blog/845355
################################################
import urllib # get data from the website | another choose is urllib2
import sys # command line input | python main.py arg1 arg2 arg3
import json
import re  #parsing json

def main():
	#variable allocated
	Dataaroad= {} 
	Databroad = {} 
	MAXnum = 0 
	MAXid = [] 
	year = [] 
	num = {}   
	numofID = 0   

	#check the command line input 
	if len(sys.argv) != 2:
		print 'Error !!  Do --> TOC_HW4.py <url> '
		sys.exit(0)
	else:
		url= sys.argv[1]

	page = urllib.urlopen(url) #load json from the web
  	data = json.load(page)  #json to python list(dictionary)

	for i_value in data:
		
		name = u""
		itr = 0 
		#null路街巷
		while (itr < len(i_value[u"土地區段位置或建物區門牌"])-1 and i_value[u"土地區段位置或建物區門牌"][itr]!=u"路" and i_value[u"土地區段位置或建物區門牌"][itr]!=u"街" and i_value[u"土地區段位置或建物區門牌"][itr]!=u"巷"):
			name = name + i_value[u"土地區段位置或建物區門牌"][itr]
			itr = itr+1
		if itr != len(i_value[u"土地區段位置或建物區門牌"])-1:
			name = name + i_value[u"土地區段位置或建物區門牌"][itr]
		# others continue
		else :  
			continue

		if Dataaroad.has_key(name): 
			id = Dataaroad[name]
			if int(i_value[u"交易年月"]) not in year[id]:
				year[id].append(int(i_value[u"交易年月"]))
				num[id] = num[id] + 1
				if num[id] == MAXnum:
					MAXid.append(id)
				if num[id] > MAXnum:
					MAXnum = num[id]
					MAXid = [] 
					MAXid.append(id)
		else : 
			Dataaroad[name] = numofID
			Databroad[numofID] = name
			year.append([]) 
			year[numofID].append(int(i_value[u"交易年月"])) 
			num[numofID] = 1
			numofID = numofID + 1
	MAXid.sort() 
	itr = 0 
	for mid in MAXid:
		Hmoney = 0 
		Lmoney = 999999999 
		name = Databroad[mid]
		for i_value in data:
			if name in i_value[u"土地區段位置或建物區門牌"]:
				if i_value[u"總價元"] > Hmoney:
					Hmoney = int(i_value[u"總價元"])
				if i_value[u"總價元"] < Lmoney:
					Lmoney = int(i_value[u"總價元"])

		name += ","
		if itr == 0:
			sys.stdout.write("\"")	
		if itr == len(MAXid)-1:
			print name, "最高成交價:%d, 最低成交價:%d\"" % (Hmoney,Lmoney)
		else:
			print name, "最高成交價:%d, 最低成交價:%d" % (Hmoney,Lmoney)
		itr = itr+1

if __name__ == '__main__':
	main()