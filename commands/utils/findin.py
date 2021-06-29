from discord.ext import commands
import discord
import re
from templates.error_handler import on_unexpected_error
from urllib.request import Request, urlopen
from urllib.parse import quote_plus

class Findin(commands.Cog):
	def __init__(self, bot : commands.Bot):
		self.bot = bot 

	@commands.command()
	async def findin(self, ctx, site:str, user:str):
		"""
		Encuentra al usuario en el sitio web que diga
		**Sintaxis:** **``=findin <sitio> <usuario>``**
		"""
		try:
			url = f'https://google.com/search?q={quote_plus(f"site:{site} intext:{user}")}'

			req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

			response = urlopen(req)

			geturls = re.findall(r'href="/url\?q=([\w\.\/\?\=\:\-\_]+)', response.read().decode())

			if len(geturls) == 0:
				embed = discord.Embed()
				embed.color = 0xff0000
				embed.title=f"No se ha encontrado a {user} en {site}"
				embed.description = 'Prueba usando otros nombres de usuario y otros sitios'

				await ctx.reply(embed = embed)
				return

			embed = discord.Embed(title=f'Se ha encontrado a {user} en {site}')
			str_urls = ''
			for url in geturls:
				str_urls += f'{url}\n' if 'google' not in url else ''

			embed.description = f'Se ha encontrado [aquí]({geturls[0]}) , en las siguientes urls:\n {str_urls}'
			embed.color = 0x0000ff

			await ctx.reply(embed = embed, mention_author = False)
		except Exception as e:
			em = on_unexpected_error(e)
			await ctx.reply(embed = em)
def setup(bot):
	bot.add_cog(Findin(bot))