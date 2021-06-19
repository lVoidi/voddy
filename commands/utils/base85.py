from discord.ext import commands
import discord
import base64

class Base85(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot
     
     @commands.command()
     async def base85(self, ctx : commands.Context, *, data:str):
          """
Codifica en base85 el texto que el usuario diga

**Sintaxis:** **``=base85 <texto>``**
          """
          bytes = data.encode("utf-8")
          base85_bytes = base64.b85encode(bytes)
          base85_str = base85_bytes.decode("utf-8")
          
          embed = discord.Embed(
               title=f"Codificador base85",
               color=ctx.message.author.color
          )
          
          embed.add_field(
               name=f"Texto codificado",
               value=f"``{base85_str}``",
               inline=False
          )
          
          
          await ctx.reply(embed = embed,
                          mention_author=False)

def setup(bot):
     bot.add_cog(Base85(bot))