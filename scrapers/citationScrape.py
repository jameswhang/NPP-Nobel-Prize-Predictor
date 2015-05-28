#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import random
import time
import scrapeLib

physicistsFile = open('../csv/List_of_physicists.csv').readlines()
chemistsFile = open('../csv/List_of_chemists.csv').readlines()
biologistsFile = open('../csv/List_of_biologists.csv').readlines()

names = []

for line in physicistsFile:
	data = line.split(',')
	names.append(data[0].replace(' ', ''))

for line in chemistsFile:
	data = line.split(',')
	names.append(data[0].replace(' ', ''))

for line in biologistsFile:
	data = line.split(',')
	names.append(data[0].replace(' ', ''))

for name in names:
	query_key = scrapeLib.scholar_form_query(name)
	query = 'https://scholar.google.com/scholar?q=' + query_key + '&btnG=&hl=en&as_sdt=0%2C14'

	scholarPage = urllib2.urlopen(query).read()
	soup = BeautifulSoup(scholarPage)
	print soup
