import json
def txtfor(txt=""):
	text = txt.lower()
	sen = tuple(text.split())
	sens = len(sen)
	for a in range(len(sen)):
		sen += (list(sen[a]),)
	nsen = ("_",)
	for n in range(sens):
		n = n+sens
		nsen += (list(sen[n]),)
	numsen = ("_",)
	nm = []
	for k in range(len(nsen)):
		if type(nsen[k]) == list:
			with open("data-table.json","r") as g:
				p = json.loads(g.read())
				for t in range(len(nsen[k])):
					m = nsen[k][t]
					l = p[m]
					nm.append(l)
				numsen += (nm),
				nm = []
	num = list(numsen)
	numsn = num.pop(0)
	return numsn
def txtdefor(num=[]):
	for i in range(len(num)):
		for t in range(len(num[i])):
			with open("data-table.json","r") as g:
				if num[i][t] in range(10):
					
