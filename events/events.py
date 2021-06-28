#    Bienvenido a los eventos de voddy

# Importa los módulos de discord necesario
from discord.ext import commands
import discord

class Events(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot
     
     # Evento cuando el bot se conecta
     @commands.Cog.listener()
     async def on_ready(self):
          """
Cambia su estado a "jugando a x servers | thelp"
          """
          
          # len(self.bot.guilds) → número de servidores en el que el bot está conectado
          status = f"{len(self.bot.guilds)} servers | =help"

          # En el estado aparecerá que es de tipo juego
          game = discord.Game(name=status)

          await self.bot.change_presence(activity=game)
          
#         Imprime por pantalla que el bot está listo
          print("Bot listo")          
     
#    Evento de los errores
#    Errores globales o en común
     @commands.Cog.listener()
     async def on_command_error(self, ctx, error):

          # Si el comando está en cooldown...
          #    isinstance → bool: true si el objeto pasado por el primero parametro
          #                        es una instancia de la clase del segundo parámetro
          if isinstance(error, commands.CommandOnCooldown):
               em = discord.Embed(color=0xFF0033)
               em.title="Cuidado! comando en cooldown!"
               em.description = f"Intenta de nuevo en {error.retry_after:.2f} segundos"
               await ctx.reply(embed = em)
     
#    Setup
def setup(bot : commands.Bot):
     bot.add_cog(Events(bot=bot))