#!/usr/bin/python

# nomineeScrape.py ####
# James Whang, 4/9/2015
# Scraper for Nobel Prize Nominees Names

import urllib2
from bs4 import BeautifulSoup

writeFile = open('result.csv', 'w')  # File to write the results to

#        MAIN LOOP          #
for i in range(10000):
    print 'Checking ' + str(i) + '...'
    html = urllib2.urlopen(
        'http://www.nobelprize.org/nomination/archive/show_people.php?id='
        + str(i)).read()

    soup = BeautifulSoup(html)

    entries = soup.find_all('td')
    category = str(soup.find('b'))
    if category == 'None':
        continue

    # filled entries have 6 rows in the table
    if len(entries) == 6 and "Nominee" in category:
        # strip html tags
        firstName = str(entries[1]).replace('<td>', '').replace('</td>', '')
        lastName = str(entries[3]).replace('<td>', '').replace('</td>', '')
        # write to output
        writeFile.write(str(i) + ":" + firstName + ', ' + lastName + '\n')

writeFile.close()
