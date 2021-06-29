# Importa todos los módulos de discord
from discord.ext import commands
import discord

# Importa el metodo md5 de hashlib
from hashlib import md5

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

          # crea el hash
          hash = md5(data.encode("utf-8"))

          # lo convierte en hex
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