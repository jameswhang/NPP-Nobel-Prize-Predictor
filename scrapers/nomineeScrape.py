#### nomineeScrape.py ####
#### James Whang, 4/9/2015
#### Scraper for Nobel Prize Nominees Names

import urllib2
import io
from bs4 import BeautifulSoup

writeFile = open('result.csv', 'w') # File to write the results to

################## MAIN LOOP #######################
for i in range(10000):
	print 'Checking ' + str(i) + '...'
	html = urllib2.urlopen('http://www.nobelprize.org/nomination/archive/show_people.php?id=' + str(i)).read()

	soup = BeautifulSoup(html)

	entries = soup.find_all('td')

	# filled entries have 6 rows in the table 
	if len(entries) == 6:
		firstName = str(entries[1]).replace('<td>', '').replace('</td>', '') # strip the html tags
		lastName = str(entries[3]).replace('<td>', '').replace('</td>', '')
		writeFile.write(str(i) + ":" + firstName + ', ' + lastName + '\n')

writeFile.close()