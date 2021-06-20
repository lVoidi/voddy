from hashlib import md5
from discord.ext import commands
import discord

class Md5(commands.Cog):
     def __init__(self, b : commands.Bot):
          self.bot = b
          
     @commands.command()
     async def md5(self, ctx : commands.Context, *, data : str):
          """
          Encripta los datos que el usuario diga en md5,
          para despeus dar el resultado en hex
          
          **Sintaxis:** **``=md5 <datos a encriptar>``**
          """
          hash = md5(data.encode("utf-8"))
          hex = hash.hexdigest()
          embed=discord.Embed(color=discord.Color.green())
          
          embed.add_field(
               name="Resultado",
               value=f"{hex}",
               inline=False
          )
          
          embed.add_field(
               name="Tamaño",
               value=f"**Hash** → {hash.block_size}B\n**Resultado hex** → {hash.digest_size}B",
               inline=False
          )
          
          await ctx.reply(embed = embed,
                          mention_author=False)

    
     
def setup(bot):
     bot.add_cog(Md5(bot))