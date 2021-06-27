from discord.ext import commands
import discord

class Grep(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot 

	@commands.command()
	async def grep(self, ctx, type:str):
		"""
		Filtra algo en el canal del contexto
		tiene un alcance de solo 200 mensajes
		**Sintaxis:** **``=grep <tipo(message o user)>`**
		"""

		msg = await ctx.send("Escribe a continuación el contenido a buscar")

		content = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

		await msg.delete()

		async for message in ctx.channel.history(limit=200):
			if message.id != content.id:
				if type == 'message':
					if content.content.lower() in message.content.lower() and message.id != content.id:
						await message.reply('‌', mention_author = False)
						break
				elif type == 'user':
					if content.content.lower() in str(message.author).lower() and message.id != content.id:
						await message.reply('‌', mention_author = False)
						break


def setup(bot):
	bot.add_cog(Grep(bot))