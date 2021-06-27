from subprocess import check_output
import subprocess
from discord.ext import commands
import discord

class Cowsay(commands.Cog):
	def __init__(self, bot : commands.Bot):
		self.bot = bot 

	@commands.command()
	async def cowsay(self, ctx, *, text:str):
		"""
		Comando cowsay de linux
		**Sintaxis:** **``=cowsay <texto>``**
		"""


		msg = await ctx.reply('''
Escoje entre uno de los siguientes personajes:
```
beavis.zen         elephant-in-snake  milk               supermilker
blowfish           eyes               moofasa            surgery
bong               flaming-sheep      moose              telebears
bud-frogs          ghostbusters       mutilated          three-eyes
bunny              head-in            ren                turkey
cheese             hellokitty         satanic            turtle
cower              kiss               sheep              tux
daemon             kitty              skeleton           udder
default            koala              small              vader
dragon             kosh               sodomized          vader-koala
dragon-and-cow     luke-koala         stegosaurus        www
elephant           meow               stimpy
```
			''')

		choice = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

		try:
			stdout = check_output(['cowsay', '-f', choice.content.lower(), f'{text}'])
			output = stdout.decode('utf-8')
			await msg.delete()
			await choice.delete()
		except:
			await choice.reply('pero ctm te dije que uno de los personajes que estaban ahi')
			return

		await ctx.reply(f'''
```
{output}
```
			''', mention_author = False)


def setup(bot):
	bot.add_cog(Cowsay(bot))