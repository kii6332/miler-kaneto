import discord
import random
import re
import os
import asyncio
import lang as lng
import time
print("start")
def igm_rp(txt,state,on_check = True,igm=""):
		if on_check:
			isig = (txt != igm)
			return isig
		else:
			if state:
				igm = txt
				return igm
rep = [True,False]
sm =[True,False]
repm = random.choices(rep, weights = [2,3])[0]
def replace_mentions(guild, text):
	pattern = r"<@!?(\d+)>"

	def replace(match):
		user_id = int(match.group(1))
		member = guild.get_member(user_id)
		return member.display_name if member else match.group(0)

	return re.sub(pattern, replace, text)
class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)
		channel = self.get_channel(1362928965769232425)
		if channel:
			async with channel.typing():
				greet = lng.gen_sent("*back online in discord*","miler")
				await channel.send(greet)
	async def on_message(self, message):
		if message.author == self.user:
			return
		nam = message.author.display_name
		text = replace_mentions(message.guild, message.content)
		igms = igm_rp(text,repm,False)
		print(f"{nam}:{text}")
		repl = igm_rp(text,False,True,igms) or self.user in message.mentions
		if nam == "kii" and text == "<CMD>ter<- re_py":
			await message.channel.send("command:restart")
			await self.restart_bot()
		elif nam == "kii" and text == "<CMD>ter<- close_py":
			await message.channel.send("command:close")
			await self.close()
		else:
			if igm_rp(text,False,True,igms) or self.user in message.mentions:
				async with message.channel.typing():
					reply_by = lng.gen_sent(text,nam)
					await message.channel.send(reply_by)
				print(f"miler:{reply_by}")
			else:
				while not repl:
					if repl:
						break
					smm = random.choices(sm, weights = [1,32])[0]
					print(smm)
					if smm:
						async with message.channel.typing():
							tl = lng.gen_sent("this is boring","miler")
							await message.channel.send(tl)
							print(f"miler:{tl}")
							time.sleep(1)
					time.sleep(1.5)
			
				
	async def restart_bot(self):
		# Use asyncio subprocess for restarting the bot without blocking the event loop
		process = await asyncio.create_subprocess_exec(
		"python3", "discord-chat.py", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await process.communicate()
		if process.returncode == 0:
			print("Bot restarted successfully.")
		else:
			print(f"Error restarting bot: {stderr.decode()}")
		await self.close()  # Close the current bot instance
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run('MTM2OTI2NTc4NTY3MDg2NDk1OA.GQIGni.Jc2A2qvAiKJHJKylK1EWd013DBiBl01ANLlcng')
