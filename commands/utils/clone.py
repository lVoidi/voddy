from discord.ext import commands
from urllib.request import Request, urlopen
from templates.error_handler import on_unexpected_error
from bs4 import BeautifulSoup
import discord
import subprocess

class Clone(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command()
	async def clone(self, ctx, url=None):
		"""
		Clona el codigo fuente de la página dicha
		**Sintaxis:** **```=clone <url>``**
		"""
		try:
			if url == None:
				await ctx.reply("Y la url para clonar capo?")
				return

			req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

			response = urlopen(req)
			soup = BeautifulSoup(response.read().decode(), 'html.parser')
			

			with open(f'commands/utils/.temp/{ctx.author.id}.txt', 'w+') as html:
				html.write(soup.prettify())

			await ctx.reply(content='<a:tux_programando:858807224645058581>',file = discord.File(f'commands/utils/.temp/{ctx.author.id}.txt'))

			subprocess.run(f"rm commands/utils/.temp/{ctx.author.id}.txt", shell=True)

		except Exception as e:
			em = on_unexpected_error(e)
			await ctx.reply(embed = em)
def setup(bot):
	bot.add_cog(Clone(bot))