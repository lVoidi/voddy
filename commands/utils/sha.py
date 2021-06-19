from discord import mentions
from discord.ext import commands
from index import VERSION
import discord
import hashlib

class Sha1(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot

     @commands.command()
     async def sha1(self, ctx : commands.Context, *, data : str):
          """
          Encripta los datos que el usuario diga en sha1,
          para despeus dar el resultado en hex
          
          **Sintaxis:** **``=sha1 <datos a encriptar>``**
          """
          hash = hashlib.sha1(data.encode("utf-8"))
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
     
     
     @commands.command()
     async def sha256(self, ctx : commands.Context, *, data : str):
          """
          Encripta los datos que el usuario diga en sha256,
          para despeus dar el resultado en hex
          
          **Sintaxis:** **``=sha256 <datos a encriptar>``**
          """
          hash = hashlib.sha256(data.encode("utf-8"))
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
     
     @commands.command()
     async def sha512(self, ctx : commands.Context, *, data : str):
          """
          Encripta los datos que el usuario diga en sha512,
          para despeus dar el resultado en hex
          
          **Sintaxis:** **``=sha512 <datos a encriptar>``**
          """
          hash = hashlib.sha512(data.encode("utf-8"))
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
     bot.add_cog(Sha1(bot))

