from discord.ext import commands
import discord
import asyncio
from templates.error_handler import on_unexpected_error
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
import re

class Img(commands.Cog):
	def __init__(self, bot : commands.Bot):
		self.bot = bot

	def isforbidden(self,query):
		list = [
				'porno',
				'hentai',
				'porn',
				'pene',
				'dick',
				'gore',
				'forogore',
				'nsfw',
				'r34',
				'rule34',
				'cojiendo',
				'cogiendo',
				'cojer',
				'coger',
				'culos',
				'culo',
				'tetas',
				'teta',
				'pussy',

			] 
		for word in query.lower().split():
			if word in list:
				return True
			else:
				return False

	def return_results(self, query):

		search = quote_plus(query)

		url = f'https://www.google.com/search?q={search}&sxsrf=ALeKk00QzbSnry1Kub4qeyiG_QgxvpN_pg:1624658815667&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi_ttrc5bPxAhVDdt8KHVMeAdsQ_AUoAXoECAEQBA&biw=1517&bih=686'

		req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

		response = urlopen(req)

		getImages = re.findall(r'src="(https://[\w\.\/\?\=\:\-]+)', response.read().decode())

		return getImages

	@commands.command()
	async def img(self, ctx, *, query:str):
		"""
		Busca imagenes en google
		**Sintaxis:** **``=img <busqueda>``**
		"""
		try:
			list_urls = self.return_results(query)
			
			if self.isforbidden(query):
				embed = discord.Embed(title='Ey, palabra prohibida mano')
				embed.color = 0xff0000
				warn = await ctx.reply(embed = embed)
				await warn.delete(delay=5)
				return

			embed = discord.Embed(title="Resultados")
			embed.description = 'Escribe **n** para ir a la siguiente imagen; **b** para la imagen que había antes y **s** para salir'
			embed.color = 0x0fff00

			embed.set_image(url=list_urls[0])
			
			page = 0
			embed.set_footer(text=f'| página {page}/{len(list_urls)}', icon_url=self.bot.user.avatar_url)
			message = await ctx.reply(embed = embed, mention_author = False)
			for num in range(1, len(list_urls)-1):
				try:
					resp = await self.bot.wait_for('message',
						check=lambda m: m.author == ctx.author and m.content.lower() in ('n', 'b', 's',),
						timeout=17)
				
				except asyncio.TimeoutError:
					await message.edit(content='> **se ha pasado el tiempo para reaccionar**')
				
				if resp.content == 'n':
					page += 1
					embed.set_image(url=list_urls[page])
					embed.set_footer(text=f'| página {page}/{len(list_urls)}', icon_url=self.bot.user.avatar_url)

					await resp.delete()
					await message.edit(embed = embed)
					

				elif resp.content == 'b':
					if page == 0:
						pass

					else:
						page -= 1
						embed.set_image(url=list_urls[page])
						embed.set_footer(text=f'| página {page}', icon_url=self.bot.user.avatar_url)
						await resp.delete()
						await message.edit(embed = embed)
					

				elif resp.content == 's':
					embed.title = 'Se ha cancelado'
					await message.edit(embed = embed)
					await resp.delete()
					break

		except Exception as e:
			em = on_unexpected_error(e)

			await ctx.reply(embed = e)

def setup(bot):
	bot.add_cog(Img(bot))
