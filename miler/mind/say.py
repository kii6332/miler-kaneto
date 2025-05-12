import edge_tts
import asyncio
import os
import filter_w as fil
def say(word = "hello"):
	word = fil.filter_w(word)
	async def tts():
		say = edge_tts.Communicate(word,voice="en-US-AnaNeural")
		await say.save("say.mp3")
	asyncio.run(tts())
	os.system("play say.mp3")
	with open("sub.txt", "w") as m:
		m.write(word)
