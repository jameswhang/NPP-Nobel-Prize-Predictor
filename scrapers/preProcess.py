wiki_data = open('../csv/Wikipedia_scraped.csv').readlines()
new_wiki_data = open('../csv/Wikipedia_scraped_new.csv', 'wb')

info_scraped = ['Nationality', 'Institutions', 'Alma mater', 'Notable awards', 'Fields', 'Known for']

first = True
for line in wiki_data:
	data = line.split('|')
	awards = data[4]
	new_wiki_data.write(line.replace('\n', ''))

	if first:
		new_wiki_data.write(' | Nobel Laureate\n')
		first = False
		continue
	if 'Nobel' in awards:
		new_wiki_data.write(' | Yes \n')
	else:
		new_wiki_data.write(' | No \n')