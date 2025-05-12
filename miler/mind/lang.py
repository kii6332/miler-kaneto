import json
import filter_w as fil
import re
from transformers import pipeline
def rel_check(name):
	with open("char.json", "r") as f:
		rel = json.load(f)["rel"]
		if name in rel["friend"]:
			return "your friend"
		elif name in rel["best friend"]:
			return "your best friend"
		elif name in rel["dad"]:
			return "your dad"
		elif name == rel["mom"]:
			return "your mom"
		elif name == rel["you"]:
			return "you"
		else:
			return "random guy"
def gen_sent(ent="hello",nam="john"):
	rel = rel_check(nam)
	with open("char.json", "r") as f:
		char = json.load(f)
	with open("sen.txt", "r") as s:
		lsen = s.read()
	info = (
		f"about {char['name']} {char['sername']} she is an ai vtuber girl coding by kii_6332(your dad) and draw by MFplat(your mom) she make out using python and json"
	)
	prom = (
		f"Your name is {char['name']} {char['sername']}, but everyone know you as {char['call_name']}.\n"
		f"You're known to be {char['charater']}.\n"
		"You're kind when reply and not use rude word\n"
		#"you like to chat with other friends\n"
		"you're really love cookie and you do anything for cookie🍪\n"
		#"you like greeting by say \"hello chat\""
		"no cookie = bad O_O\n"
		"cookie = happy :D\n"
		#f"{info}\n"
		#f"you say:{lsen}\n"
		f"{nam}({rel}) say: \"{ent}\"\n"
	)
	sentm = pipeline(task="text-generation", model="GPT2")
	get = sentm(prom, temperature=0.15,do_sample=True, max_new_tokens=1024, repetition_penalty=1.2, no_repeat_ngram_size=2)[0]["generated_text"][len(prom):].strip()
	print(f"no filer: {get}\n\n")
	sen = re.sub("miler: ","", get)
	out = fil.filter_w(sen)
	with open("sen.txt", "w") as s:
		s.write(out)
	return out
