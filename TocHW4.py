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

def main():

	#check the command line input 
	if len(sys.argv) != 2:
		print 'Error !!  Do --> TOC_HW4.py <url> '
		sys.exit(0)
	else:
		url= sys.argv[1]

	page = urllib.urlopen(url) #load json from the web
  	data = json.load(page)  #json to python list(dictionary)


if __name__ == '__main__':
	main()