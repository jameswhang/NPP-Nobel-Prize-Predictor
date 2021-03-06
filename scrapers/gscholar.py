import hashlib
import random
import time
import requests
from bs4 import BeautifulSoup
from lxml import html
from random import randint

GSCHOLAR_BASE_URL = 'http://scholar.google.com/scholar'
PAGERANK_MAX_DEPTH = 2
USER_AGENT_STRING_LIST = ['Opera/9.80', 'Mozilla/5.0', 'Mozilla/6.0']

def _gen_random_user_agent():
    return USER_AGENT_STRING_LIST[randint(0, 2)]

def _gen_fake_google_id():
    return hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()[:16]

def _wait_random_time():
    time.sleep(random.random(5, 10))

def _do_gscholar_request(gid, query):
    print gid
    _wait_random_time()
    u_agent = _gen_random_user_agent()
    return requests.get(GSCHOLAR_BASE_URL, params=query, headers = {'User-Agent': u_agent, 'Cookie': 'GSP=ID=%s:CF=4' % gid})

def _do_gscholar_request_with_link(gid, link):
    print gid
    _wait_random_time()
    u_agent = _gen_random_user_agent()
    return requests.get(GSCHOLAR_BASE_URL + link, headers = {'User-Agent': u_agent, 'Cookie': 'GSP=ID=%s:CF=4' % gid})

def _get_citation_count(match):
    total_count = 0
    for r in match:
        rtext = str(r.text)
        if 'Cited by' in rtext:
            this_count = rtext.split(' ')[2]
            total_count += int(this_count)
    return total_count

def _get_links_to_citations(match):
    all_links = []
    for r in match:
        if 'Cited by' in str(r.text):
            link = str(r).split('"')[3]
            all_links.append(link)
    return all_links

def _parse_gscholar_html(page):
    soup = BeautifulSoup(page.text)
    res = soup.find_all('div', class_='gs_fl')
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
    q = form_query(name)
    gid = _gen_fake_google_id()
    request_result = _do_gscholar_request(gid, q)
    parse_result = _parse_gscholar_html(request_result)
    return parse_result

def make_query_on_citation(citation_link):
    gid = _gen_fake_google_id()
    request_result = _do_gscholar_request_with_link(gid, citation_link)
    parse_result = _parse_gscholar_html(request_result)
    return parse_result

def get_pagerank_score(target, alpha, depth):
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
