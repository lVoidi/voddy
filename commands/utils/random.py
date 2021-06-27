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

def setup(bot):
	bot.add_cog(Random(bot))