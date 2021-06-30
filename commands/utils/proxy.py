# Basado en el código de https://github.com/Cuchillos/ProxyScraper
# 
#
#
# Importa los módulos de discord
from discord.ext import commands
import discord

# Importa todo lo relacionado a requests
from urllib.request import Request, urlopen
from requests.structures import CaseInsensitiveDict

# Template error handler
from templates.error_handler import on_unexpected_error

class Proxy(commands.Cog):
	def __init__(self, bot : commands.Bot):
		self.bot = bot
		self.limit = 40

	@commands.command()
	async def proxy(self, ctx, type:str, number:int):
		"""
		Consigue proxies del tipo que quieras, ya sea http, https, socks4 o socks5

		**Sintaxis:** **``=proxy <tipo> <numero de proxys>``**
		"""
		try:

			# Revisa si el tipo de proxy es correcto
			if type.lower() not in ['http', 'https', 'socks5', 'socks4']:
				await ctx.reply("Ese tipo de proxy no es válido, prueba con una de las  siguientes: **http**, **socks4**, **socks5**")
				return

			if number <= 0:
				await ctx.reply("que pa? quieres 0 proxies o que coño")
				return
			# Url de la api
			url = f"https://api.proxyscrape.com/?request=displayproxies&proxytype={type.lower()}"

			# Si el numero es mayor a 40
			if number > self.limit:
				await ctx.reply(f"Tiene que ser un número menor a {self.limit}")
				return

			# Crea los headers
			# Basado en el código de https://github.com/Cuchillos/ProxyScraper


			headers = CaseInsensitiveDict()
			headers["Connection"] = "keep-alive"
			headers["Cache-Control"] = "max-age=0"
			headers["Upgrade-Insecure-Requests"] = "1"
			headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279"
			headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
			headers["Sec-Fetch-Site"] = "none"
			headers["Sec-Fetch-Mode"] = "navigate"
			headers["Sec-Fetch-User"] = "?1"
			headers["Sec-Fetch-Dest"] = "document"
			headers["Accept-Language"] = "es-ES,es;q=0.9"

			# Crea el objeto de la clase Request
			req = Request(url=url, headers=headers)

			# Guarda la respuesta en  esta variable
			response = urlopen(req)

			# Inicializa la variable con las proxies
			string_proxies = ''

			# Guarda el actual valor de number en otra variable auxiliar
			num = number

			# Itera sobre todas las proxies
			for proxy in response.read().decode().splitlines():
				
				# Si es 0, rompe el bucle
				if num <= 0:
					break

				# Cuenta las iteraciones
				num -= 1

				# Agrega al string de proxies la proxy sobre la cual
				# se itera
				string_proxies += f'**``{proxy}``**\n'

			# Crea el embed
			embed = discord.Embed(title=f'{number} proxies de tipo {type}')
			embed.color = 0xaaffaa
			embed.description = f"{string_proxies} \n consulta la api utilizada [aquí](https://api.proxyscrape.com)"

			# Responde
			await ctx.reply(embed = embed, mention_author = False)

		# En caso de un error inesperado
		except Exception as e:
			em = on_unexpected_error(e)
			await ctx.reply(embed = em)

	@proxy.error
	async def on_error(self, ctx:commands.Context, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('Al comando le faltan argumentos! recuerda que el comando recibe como parametros el **tipo** ***(http, https, socks4, socks5)*** y el numero de proxies **(maximo:40)**')

def setup(bot):
	bot.add_cog(Proxy(bot))



