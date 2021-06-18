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
          
          status = f"{len(self.bot.guilds)} servers | thelp"
          game = discord.Game(name=status)
          await self.bot.change_presence(activity=game)
          
#         Imprime por pantalla que el bot está listo
          print("Bot listo")          
          

def setup(bot : commands.Bot):
     bot.add_cog(Events(bot=bot))