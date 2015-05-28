import hashlib
import random
import time
import requests
from bs4 import BeautifulSoup
from lxml import html

GSCHOLAR_BASE_URL = 'http://scholar.google.com/scholar'
PAGERANK_MAX_DEPTH = 2

def _gen_fake_google_id():
	return hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()[:16]

def _do_gscholar_request(gid, query):
	time.sleep(random.random() * 5)
	return requests.get(GSCHOLAR_BASE_URL, params=query, headers = {'User-Agent': 'Mozilla/5.0', 'Cookie': 'GSP=ID=%s:CF=4' % gid})

def _do_gscholar_request_with_link(gid, link):
	time.sleep(random.random() * 5)
	return requests.get(GSCHOLAR_BASE_URL + link, headers = {'User-Agent': 'Mozilla/5.0', 'Cookie': 'GSP=ID=%s:CF=4' % gid})

def _get_citation_count(match):
	total_count = 0
	for r in match:
		rtext = str(r.text)
		if 'Cited by' in rtext:
			this_count = rtext.split(' ')[2]
			total_count += int(this_count)
			print this_count
	return total_count

def _get_links_to_citations(match):
	all_links = []
	for r in match:
		if 'Cited by' in str(r.text):
			link = str(r).split('"')[3]
			print link
			all_links.append(link)
	return all_links

def _parse_gscholar_html(page):
	print 'parsing...'
	soup = BeautifulSoup(page.text)
	res = soup.find_all('div', class_='gs_fl')
	print res
	total_citations = _get_citation_count(res)
	cited_by = _get_links_to_citations(res)

	return {
		'citation_count': total_citations, 
		'cited_by_list': cited_by
	}

def form_query(name):
	return {
		'q': name,
		'hl': 'en'
	}

def make_query(name):
	print 'making query on the name ' + name
	q = form_query(name)
	gid = _gen_fake_google_id()
	request_result = _do_gscholar_request(gid, q)
	print request_result.url
	parse_result = _parse_gscholar_html(request_result)
	return parse_result

def make_query_on_citation(citation_link):
	print 'making query on the link ' + citation_link
	gid = _gen_fake_google_id()
	request_result = _do_gscholar_request_with_link(gid, citation_link)
	parse_result = _parse_gscholar_html(request_result)
	return parse_result

def get_pagerank_score(target, alpha, depth):
	print "Ah..?"
	if depth == 0:
		query_result = make_query_on_citation(target)
		total_citations = query_result['citation_count']
		return total_citation

	elif depth == PAGERANK_MAX_DEPTH:
		query_result = make_query(target)
	else:
		query_result = make_query_on_citation(target)

	total_citations = query_result['citation_count']
	cited_by_list = query_result['cited_by_list']

	sum_cindex = 0
	for citation in cited_by_list:
		sum_cindex += get_pagerank_score(citation, alpha, depth-1)
	return (1 - alpha) * total_citations + alpha * sum_cindex

print get_pagerank_score('albert einstein', 0.5, PAGERANK_MAX_DEPTH)