from discord.ext import commands
import discord
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
          if len(data) > 1024:
               await ctx.send("Ey, el texto tiene que ser mas corto")
               return
          
          bytes = data.encode("utf-8")
          base85_bytes = base64.a85encode(bytes)
          base85_str = base85_bytes.decode("utf-8")
          
          embed = discord.Embed(
               title=f"Codificador ascii85",
               color=ctx.message.author.color
          )
          
          embed.add_field(
               name=f"Texto codificado",
               value=f"{base85_str}",
               inline=False
          )
          
          
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
          
          bytes = data.encode("utf-8")
          base85_bytes = base64.a85decode(bytes)
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
          
          
          await ctx.reply(embed = embed,
                          mention_author=False)

     
     
def setup(bot):
     bot.add_cog(Base85(bot))