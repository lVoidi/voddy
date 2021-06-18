import base64
from discord.ext import commands
import discord

class Base64(commands.Cog):
     def __init__(self, bot : commands.Bot) -> None:
         self.bot = bot
     
     @commands.command()
     async def base64(self, ctx : commands.Context, *, text : str):
          """
Codifica en base64 el texto que el usuario diga

**Sintaxis:** **``tbase64 <texto>``**
          """
          bytes = text.encode("utf-8")
          
          base64_bytes = base64.b64encode(bytes)
          base64_string = base64_bytes.decode("ascii")
          
          embed = discord.Embed(
               title=f"Codificador base64",
               color=ctx.message.author.color
          )
          
          embed.add_field(
               name=f"Texto sin codificar",
               value=f"``{text}``",
               inline=False
          )
          
          embed.add_field(
               name=f"Texto codificado",
               value=f"``{base64_string}``",
               inline=False
          )
          
          
          await ctx.reply(embed = embed)
          
def setup(bot):
     bot.add_cog(Base64(bot=bot))
          
          