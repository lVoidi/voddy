# importa todos los módulos necesarios
from discord.ext import commands
import discord

# Importa los módulos necesarios de requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Errores inesperados
from templates.error_handler import on_unexpected_error

# Importa el módulo subprocess para despues borrar el archivo de texto
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

			# Si no ha puesto la url
			if url == None:
				await ctx.reply("Y la url para clonar capo?")
				return

			# Si la url no inicia con http:// o https://
			elif not url.startswith('http'):
				await ctx.reply("Ponle el http/s al principio")
				return

			# Crea una instancia de la clase urllib.request.Request
			req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

			# La respuesta html del sitio web
			response = urlopen(req)

			# crea una instancia de Beautiful soup para poder hacer legible el texto 
			soup = BeautifulSoup(response.read().decode(), 'html.parser')
			
			# Crea un archivo de texto
			with open(f'commands/utils/.temp/{ctx.author.id}.txt', 'w+') as html:

				# Escribe en el archivo de texto el contenido html de la página,
				# usando el metodo prettify() para poder hacer más legible el 
				# documento
				html.write(soup.prettify())

			# Responde al mensaje 
			await ctx.reply(content='<a:tux_programando:858807224645058581>',file = discord.File(f'commands/utils/.temp/{ctx.author.id}.txt'))

			# Elimina el archivo de texto para ahorrar espacio en memoria
			subprocess.run(f"rm commands/utils/.temp/{ctx.author.id}.txt", shell=True)

		# Por si hay algún error inesperado
		except Exception as e:
			em = on_unexpected_error(e)
			await ctx.reply(embed = em)
def setup(bot):
	bot.add_cog(Clone(bot))