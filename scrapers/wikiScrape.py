#!/usr/bin/python
#-*- coding: utf-8 -*-

# wikiScrape.py
# James Whang, 5/8/2015
# Scraper for Wikipedia

import urllib2
from bs4 import BeautifulSoup
import random
import time
import codecs
import scrapeLib
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

people = {}
physicists_file = open('../csv/List_of_physicists.csv').readlines()
chemists_file = open('../csv/List_of_chemists.csv').readlines()
biologists_file = open('../csv/List_of_biologists.csv').readlines()

output_file = open('../csv/Wikipedia_Scraped.csv', 'wb')

attr_file = open('../attr_test.csv', 'wb')
val_file = open('../val_test.csv', 'wb')

info_to_scrape = ['Nationality', 'Institutions', 'Alma mater', 'Notable awards', 'Fields', 'Known for']

first = True
'''
for line in physicists_file:
    if first:
        first = False
        continue
    data = line.split(',')
    name = scrapeLib.wiki_extract_name(data)
    link = scrapeLib.wiki_extract_link(data)
    people[name] = link
'''

for line in chemists_file:
    if first:
        first = False
        continue
    data = line.split(',')
    name = scrapeLib.wiki_extract_name(data)
    link = scrapeLib.wiki_extract_link(data)
    people[name] = link

'''
for line in biologists_file:
    data = line.split(',')
    name = scrapeLib.wiki_extract_name(data)
    link = scrapeLib.wiki_extract_link(data)
    people[name] = link

'''
output_file.write('Name , Nationality , Institutions , Alma mater , Notable awards , Fields , Known for\n')

for person, link in people.iteritems():
    if 'Raymond_Davis_Jr' in person:
        continue
    print '****' + person + '****'
    print '****' + link + '****'
    if 'William_Henry_Perkin' in person:
        continue
    wikiPage = urllib2.urlopen('http://en.wikipedia.org' + link).read()
    soup = BeautifulSoup(wikiPage)

    infoBox = soup.find('table', class_='infobox')

    if infoBox is None:
        print ':(((('
        continue

    attr_list = infoBox.find_all('th')
    attr_vals = infoBox.find_all('td')

    if len(attr_list) != len(attr_vals):
        print ':((((('
        continue 

    attrDict = {
        'Nationality': -1,
        'Institutions': -1,
        'Alma mater': -1,
        'Notable awards': -1,
        'Fields': -1,
        'Known for': -1,
    }
    index = 0

    for attr in attr_list:
        if attr.text in info_to_scrape:
            attrDict[attr.text] = index
        index += 1

    output_file.write(person + ' , ')
    for info in info_to_scrape:
        print info
        i = attrDict[info]
        if i != -1:
            val = attr_vals[i].text.decode('utf-8').replace(u'\u000a', u'\u0026').encode('utf-8')
        else:
            val = ''
        output_file.write(repr(val))
        output_file.write(' , ')

    output_file.write('\n')
    time.sleep(3)
