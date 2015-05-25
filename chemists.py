#!/usr/bin/python

# James Whang, 5/8/2015
# Scraper for Wikipedia List of Chemists

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

writeFile = open('List_of_chemists.csv', 'wb')
scientists = []

wikipage = urllib2.urlopen('http://en.wikipedia.org/wiki/List_of_chemists').read()

soup = BeautifulSoup(wikipage)

uls = soup.find_all('ul')

writeFile.write('Name, Year, WikiLink\n')

for i in range(1, 25):
    people = uls[i].find_all('li')
    for person in people:
        if 'Solomon' in str(people):
            continue
        elif 'Schultz' in str(people):
            continue
        elif 'Mostafa' in str(people):
            continue

        link = scrapeLib.extractLink(str(person))
        name = scrapeLib.convertLinkToName(link.split('/wiki/')[1])
        year = scrapeLib.extractYear(str(person))
        if year > 0:
            writeFile.write(name.encode('utf-8') + ', ' + year + ', ' + link + '\n')