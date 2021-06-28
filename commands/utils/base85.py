# Importa los módulos de discord
from discord.ext import commands
import discord

# importa el módulo necesario para codificar en ascii85
import base64

class Base85(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot
     
     @commands.command()
     async def ascii85(self, ctx : commands.Context, *, data:str):
          """
Codifica en ascii85 el texto que el usuario diga

**Sintaxis:** **``=ascii85 <texto>``**
          """

          # Si el texto es demasiado largo, cancela el comando
          if len(data) > 1024:
               await ctx.send("Ey, el texto tiene que ser mas corto")
               return
          
          # Codifica el texto en bytes
          bytes = data.encode("utf-8")

          # Convierte los bytes en ascii85
          base85_bytes = base64.a85encode(bytes)

          # Convierte los bytes en ascii85 en un string legible
          base85_str = base85_bytes.decode("utf-8")
          
          # Crea el embed
          embed = discord.Embed(
               title=f"Codificador ascii85",
               color=ctx.message.author.color
          )
          
          # Crea el campo correspondiente con el texto codificado
          embed.add_field(
               name=f"Texto codificado",
               value=f"{base85_str}",
               inline=False
          )
          
          # Responde al mensaje
          await ctx.reply(embed = embed,
                          mention_author=False)

     @commands.command()
     async def dascii85(self, ctx : commands.Context, *, data:str):
          """
Decodifica en ascii85 el texto que el usuario diga

**Sintaxis:** **``=dascii85 <texto>``**
          """
          if len(data) > 1024:
               await ctx.send("Ey, el texto tiene que ser mas corto")
               return
          
          # Vuelve a codificar el texto en bytes para
          # poder interpretarlo
          bytes = data.encode("utf-8")

          # Decodifica los bytes de ascii85 en bytes-string
          base85_bytes = base64.a85decode(bytes)

          # Convierte los bytes de ascii85 a un string
          base85_str = base85_bytes.decode("utf-8")
          
          embed = discord.Embed(
               title=f"Decodificador ascii85",
               color=ctx.message.author.color
          )
          
          embed.add_field(
               name=f"Texto decodificado",
               value=f"``{base85_str}``",
               inline=False
          )
          
          # Responde el mensaje
          await ctx.reply(embed = embed,
                          mention_author=False)

     
     # Por si falta algun argumento al comando
     @ascii85.error 
     @dascii85.error 
     async def on_error(self, ctx, error):
          if isinstance(error, commands.MissingRequiredArgument):
               await ctx.send("Recuerda que este comando recibe como parámetro el texto a codificar/decodificar")

def setup(bot):
     bot.add_cog(Base85(bot))