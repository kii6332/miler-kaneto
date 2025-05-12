import json
def sto(data):
	prest = json.dumps(data)
	with open("mem.json", "w") as f:
		f.write(prest)
		f.close()

def lod(data):
	with open("mem.json") as f:
		dal = f.read()
		dl = json.loads(dal)
		return dl[data]
		f.close()

def pull(data):
	with open("base.json") as f:
		dal = f.read()
		dl = json.loads(dal)
		return dl[data]
		f.close()

def keep(data):
	prest = json.dumps(data)
	with open("dat.json", "a") as f:
		f.write(prest)
		f.close()
