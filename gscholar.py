import hashlib
import random
import requests
from bs4 import BeautifulSoup
from lxml import html

GSCHOLAR_BASE_URL = 'http://scholar.google.com/scholar'

def _gen_fake_google_id():
    return hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()[:16]

def _do_gscholar_request(gid, query):
    return requests.get(GSCHOLAR_BASE_URL, params=query, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': 'GSP=ID=%s:CF=4' % gid})

def _get_citation_count(match):
	total_count = 0
	for r in match:
		rtext = str(r.text)
		if 'Cited by' in rtext:
			this_count = rtext.split(' ')[2]
			total_count += int(this_count)
	return total_count

def _parse_gscholar_html(page):
	soup = BeautifulSoup(page.text)
	res = soup.find_all('div', class_='gs_fl')

	citation_count(res)

	

q = {
	'hl': 'en',
	'q': 'albert einstein'
}

gid = _gen_fake_google_id()
result = _do_gscholar_request(gid, q)

_parse_gscholar_html(result)