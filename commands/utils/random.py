# Comando de relleno lol
from discord.ext import commands
import discord
from random import randint

class Random(commands.Cog):
	def __init__(self, bot : commands.Cog):
		self.bot = bot

	@commands.command()
	async def random(self, ctx, from_:int, limit:int):
		"""
		Devuelve un numero aleatorio entre los numeros 
		establecidos

		**Sintaxis:** **``=random <numero a> <numero limite>``**
		"""
		random_number = randint(from_, limit)

		embed = discord.Embed()
		embed.color=0x00ff00
		embed.title = f'Número aleatorio entre {from_} y {limit}'
		embed.description = f'**``{random_number}``**'

		await ctx.reply(embed = embed, mention_author = False)

	@random.error 
	async def on_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.reply('Recuerda que este comando recibe 2 argumentos, los cuales definen el rango para generar el numero aleatorio: sintaxis: **``=random <num1> <num2>``**')
def setup(bot):
	bot.add_cog(Random(bot))