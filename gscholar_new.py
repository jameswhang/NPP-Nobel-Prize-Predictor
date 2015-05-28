import hashlib
import random
import requests

GSCHOLAR_BASE_URL = 'http://scholar.google.com/scholar'

def _gen_fake_google_id():
    return hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()[:16]

def _do_gscholar_request(path, gid):
    return requests.get(GSCHOLAR_BASE_URL + path, 
