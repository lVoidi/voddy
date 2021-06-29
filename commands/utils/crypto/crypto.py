# Importa los modulos de discord
from discord.ext import commands
import discord

# Imporat el error handler
from templates.error_handler import on_unexpected_error

# Importa el metodo correspondiente
from commands.utils.crypto.scrapper import get_info

# Inicializa la clase de las crypto
class Crypto(commands.Cog):
  def __init__(self, bot : commands.Bot):
    self.bot = bot
  
  # cooldown de 10 segundos
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.command()
  async def crypto(self, ctx : commands.Context, cryptoname : str):
    """
    Devuelve la informacion de la criptomoneda que el usuario pida,
    por ejemplo: ``=crypto BTC``
    **Sintaxis:** **``=crypto <cryptomoneda>``**
    """
    try:

      # usa el metodo para sacar informacion
      dict_info = get_info(crypto=cryptoname)
      
      # cryptocompare retorna Nonetype si no ha encontrado la criptomoneda
      if dict_info == None:
        await ctx.reply('Vaya, esa crypto no la reconozco, podrías ser tan amable de poner un simbolo valido?')
        return
      
      # crea el embed
      embed = discord.Embed()
      
      embed.title = f"Precio actual de **{cryptoname}**"
      
      embed.description = f'''
Precio mas bajo en 24hrs → **{dict_info['low']}**$ 
Precio mas alto en 24hrs → **{dict_info['high']}**$ 
Precio actual → **{dict_info['actual']}**$ 
      '''
      
      # Responde el mensaje
      await ctx.reply(embed = embed,
                      mention_author = False)

    # En caso de un error inesperado
    except Exception as e:
      em = on_unexpected_error(e)
      
      await ctx.reply(embed = em)
  
def setup(bot):
  bot.add_cog(Crypto(bot))
  