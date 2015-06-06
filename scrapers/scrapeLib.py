def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
def convertLinkToName(someLink):
	return someLink.replace('_', ' ')


def extractLink(li_str):
	elems = li_str.split('"')
	for elem in elems:
		if '/wiki/' in elem:
			return elem

def extractYear(li_str):
	if '(born' in li_str:
		return li_str.split('(born')[1].split(')')[0].replace(' ', '')
	else:
		year = li_str.split('</a>')[1].replace(' ', '')[1:5]
		if isInt(year):
			if int(year) > 1850:
				return year
			else:
				return -1
		else:
			return -1


def scholar_form_query(names):
	names = names.split(' ')
	q = ''
	for name in names:
		q += name
		if name is names[len(names)-1]:
			return q
		else: 
			q += '+'


def wiki_extract_name(data):
	return data[0].replace(' ', '_')


def wiki_extract_link(data):
	return data[2].replace(' ', '').replace('\n', '')

'''
def wiki_extract_info(th_str):
	for char in th_str:
		if 
		'''