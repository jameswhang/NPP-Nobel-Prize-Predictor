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