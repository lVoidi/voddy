# Importa los modulos de discord
from discord import mentions
from discord.ext import commands
import discord

# Importa la version desde el index
from index import VERSION

# Importa la libreria hashlib que es la encargada
# de crear el hash de tipo sha1
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

          # Crea el hash de tipo sha1 con la informacion 
          # que el usuario paso por argumentos
          hash = hashlib.sha1(data.encode("utf-8"))

          # Convierte el hash en hexadecimal
          hex = hash.hexdigest()

          # crea el embed
          embed=discord.Embed(color=discord.Color.green())
          
          embed.add_field(
               name="Resultado",
               value=f"{hex}",
               inline=False
          )
          
          # Crea un campo con el tamagno 
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

          # lo mismo que con sha1, nada mas que aqui crea el hash de tipo sha256
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
     
     
     @sha1.error
     @sha256.error 
     @sha512.error
     async def on_error(self, ctx, error):
          if isinstance(error, commands.MissingRequiredArgument):
               await ctx.reply('a ese comando le falta un parametro, el texto a convertir')
               
def setup(bot):
     bot.add_cog(Sha1(bot))

