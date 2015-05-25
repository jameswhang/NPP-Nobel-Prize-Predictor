#!/usr/bin/python

# James Whang, 5/8/2015
# Scraper for Wikipedia

import urllib2
from bs4 import BeautifulSoup
import random
import time
import scrapeLib

def get_year(people_str):
    people = people_str.split('(')[1]
    people = people.split(')')[0]
    print people
    return people

writeFile = open('list_of_scientists.csv', 'wb')
scientists = []

wikipage = urllib2.urlopen('http://en.wikipedia.org/wiki/List_of_physicists').read()

soup = BeautifulSoup(wikipage)

uls = soup.find_all('ul')

writeFile.write('Name, Year, WikiLink\n')

for i in range(1, 25):
    people = uls[i].find_all('li')
    for person in people:
        if '(' in str(person):
            if 'born' in str(person):
                year = str(person).split('>')[3].split('(')[1].split(')')[0].split('born')
                if len(year) is 2:
                    year = year[1].replace(' ', '')
                    splitonquote = str(person).split('"')
                    for split in splitonquote:
                        if '/wiki/' in split:
                            link = split
                            break
                    name = scrapeLib.convertLinkToName(link.split('/')[2])
                    if int(year) > 1850:
                        writeFile.write(name + ', ' + year + ', ' + link + '\n')
            elif '-' in str(person):
                if 'Snellius' in str(person): # this guy has a weird issue
                    continue
                splittags = str(person).split('>')
                year = splittags[len(splittags)-2].split('(')[1]
                links = str(person).split('"')
                for elem in links:
                    if '/wiki/' in elem:
                        link = elem
                        break
                name = scrapeLib.convertLinkToName(link.split('/')[2])
                
                if '-' in year:
                    year = year.split('-')[0]
                else:
                    year = year.split('\xe2')[0]
                
                if int(year) > 1850:
                    writeFile.write(name + ', ' + year + ', ' + link + '\n')