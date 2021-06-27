from discord.ext import commands
from templates.error_handler import on_unexpected_error
from commands.utils.crypto.scrapper import get_info
import discord
import cryptocompare

class Crypto(commands.Cog):
  def __init__(self, bot : commands.Bot):
    self.bot = bot
  
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.command()
  async def crypto(self, ctx : commands.Context, cryptoname : str):
    """
    Devuelve la informacion de la criptomoneda que el usuario pida,
    por ejemplo: ``=crypto BTC``
    **Sintaxis:** **``=crypto <cryptomoneda>``**
    """
    try:
      dict_info = get_info(crypto=cryptoname)
      
      if dict_info == None:
        await ctx.reply('Vaya, esa crypto no la reconozco, podrías ser tan amable de poner un simbolo valido?')
        return
      
      embed = discord.Embed()
      
      embed.title = f"Precio actual de **{cryptoname}**"
      
      embed.description = f'''
Precio mas bajo en 24hrs → **{dict_info['low']}**$ 
Precio mas alto en 24hrs → **{dict_info['high']}**$ 
Precio actual → **{dict_info['actual']}**$ 
      '''
      
      await ctx.reply(embed = embed,
                      mention_author = False)

    except Exception as e:
      em = on_unexpected_error(e)
      
      await ctx.reply(embed = em)
  
def setup(bot):
  bot.add_cog(Crypto(bot))
  