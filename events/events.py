from discord.ext import commands
import discord

class Events(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot
     
     @commands.Cog.listener()
     async def on_ready(self):
          """
Cambia su estado a "jugando a x servers | thelp"
          """
          
          status = f"{len(self.bot.guilds)} servers | =help"
          game = discord.Game(name=status)
          await self.bot.change_presence(activity=game)
          
#         Imprime por pantalla que el bot está listo
          print("Bot listo")          
          
     @commands.Cog.listener()
     async def on_command_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
               em = discord.Embed(color=0xFF0033)
               em.title="Cuidado! comando en cooldown!"
               em.description = f"Intenta de nuevo en {error.retry_after:.2f} segundos"
               await ctx.reply(embed = em)
     
          
def setup(bot : commands.Bot):
     bot.add_cog(Events(bot=bot))