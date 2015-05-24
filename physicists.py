#!/usr/bin/python

# James Whang, 5/8/2015
# Scraper for Wikipedia

import urllib2
from bs4 import BeautifulSoup
import random
import time

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

writeFile.write('Name WikiLink')

for i in range(1, 25):
    people = uls[i].find_all('li')
    for person in people:
        if '(' in str(person):
            if 'born' in str(person):
                year = str(person).split('>')[3].split('(')[1].split(')')[0].split('born')
                if len(year) is 2:
                    print person.get_text()
                    year = year[1].replace(' ', '')
                    link = str(person).split('"')[1]
                    if int(year) > 1850:
                        print person.get_text()
                        print link
                        print year
            elif '-' in str(person):
                print person.get_text()
                splittags = str(person).split('>')
                year = splittags[len(splittags)-2].split('(')[1]
                print year
                if '-' in year:
                    year = year.split('-')[0]
                else:
                    year = year.split('\xe2')[0]
                print year
                if int(year) > 1850:
                    print person.get_text()
                    print link
                    print year
