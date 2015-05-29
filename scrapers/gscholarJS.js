var papers = $('#gs_ccl').children,
	counts = []
for (var i = 0; i < papers.length; i++) {
	var paper = papers[i],
		html = paper.innerHTML;

	if (paper.className != 'gs_r') {
		continue;
	}
	else {
		if (html.indexOf('Cited by ') < 0) {
			continue;
		} else {
			var count = html.split('Cited by ')[1].split('</a>')[0];
			counts.push(count)
		}
	}
}
totalCount = 0;
for (var j = 0; j < counts.length; j++) {
	totalCount += parseInt(counts[j]);
}
console.log(totalCount);