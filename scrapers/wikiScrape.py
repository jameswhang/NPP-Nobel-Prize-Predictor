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

info_to_scrape = ['Institutions', 'Alma mater', 'Notable awards', 'Fields', ]

for line in physicists_file:
    data = line.split(',')
    name = scrapeLib.wiki_extract_name(data)
    link = scrapeLib.wiki_extract_link(data)
    people[name] = link

for line in chemists_file:
    data = line.split(',')
    name = scrapeLib.wiki_extract_name(data)
    link = scrapeLib.wiki_extract_link(data)
    people[name] = link

for line in biologists_file:
    data = line.split(',')
    name = scrapeLib.wiki_extract_name(data)
    link = scrapeLib.wiki_extract_link(data)
    people[name] = link

for person, link in people.iteritems():
    wikiPage = urllib2.urlopen('http://en.wikipedia.org' + link).read()
    soup = BeautifulSoup(wikiPage)

    infoBox = soup.find('table', class_='infobox')

    if infoBox is None:
        print ':(((('
        continue

    attr_list = infoBox.find_all('th')
    attr_vals = infoBox.find_all('td')
    print len(attr_list)
    print len(attr_vals)

    attr_file = open('../attr_test.csv', 'wb')
    val_file = open('../val_test.csv', 'wb')
    for attr in attr_list:
        attr_file.write(str(attr))
    for val in attr_vals:
        val_file.write(str(val))

    time.sleep(random.random() * 5)

'''
winnerNames = []
categories = ['Born', 'Nationality', 'Institutions', 'Alma mater', 'Known for', 'Notable awards']
scrapedInfo = []

for line in nobelFile:
    data = line.split(',')
    winnerNames.append(data[2])

#winnerNames = ['Marie Curie']
for winner in winnerNames:
    print winner
    newDict = {}
    winner = winner.replace(' ', '_')
    winner = winner.replace('\'', '%27')
    winner = winner.replace('\n', '')
    winner = winner.replace('"', '')
    newDict['name'] = winner

    if winner == 'Lord_Rayleigh_(John_William_Strutt)':
        winner = 'John_William_Strutt,_3rd_Baron_Rayleigh'
    
    wikipage = urllib2.urlopen(
            'http://en.wikipedia.org/wiki/' + str(winner)).read()

    soup = BeautifulSoup(wikipage)
    infoBox = soup.find('table', class_='infobox')

    #print infoBox
    if infoBox is None:
        continue
    attr_list = infoBox.find_all('th')
    attr_val_list = infoBox.find_all('td')

    index = 0

    for attr_tag in attr_list:
        attr_tag_str = str(attr_tag)
        attr = attr_tag_str.split('>')[1]
        attr = attr.split('<')[0]

        if attr in categories:
            attr_val = attr_val_list[index].get_text()
            print attr
            print attr_val
            newDict[attr] = attr_val

        index += 1
        
    time.sleep(random.random() * 5)
    scrapedInfo.append(newDict)

for item in scrapedInfo:
    for attr in item:
        writeFile.write(val.replace('\n', '').encode('utf8'))
        writeFile.write(' ') 

'''