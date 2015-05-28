import gscholar

PAGERANK_MAX_DEPTH = 2
ALPHA = 0.5

chemists_data = open('../csv/List_of_chemists.csv').readlines()
chemists_with_citation = open('../csv/chemists_citations.csv', 'wb')
chemists = []

first = True
for line in chemists_data:
	if first:
		first = False
		continue
	data = line.split(',')
	name = data[0]
	if name == ' ':
		continue
	chemists.append(name)

for chemist in chemists:
	name = chemist.replace('\n', '')
	print 'scraping: ' + name
	citation_score = gscholar.get_pagerank_score(name, ALPHA, PAGERANK_MAX_DEPTH)
	print 'score: ' + str(citation_score)
	chemists_with_citation.write(name)
	chemists_with_citation.write(',')
	chemists_with_citation.write(str(citation_score) + '\n')