from discord.ext import commands
import discord

class Hex(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot

     @commands.command()
     async def hex(self, ctx : commands.Context, *, text : str):
          """
Codifica en hexadecimal el texto que el usuario diga

**Sintaxis:** **``=hex <texto>``**
          """
          ntext = text.encode('utf-8')
          
          encode = ntext.hex()
          
          embed = discord.Embed(
               title=f"Codificador hexadecimal",
               color=discord.Color.from_rgb(0,255,0)
          )
          
          embed.add_field(
               name=f"Texto a cifrar",
               value=f'``{text}``'
               ,inline=False
          )
          embed.add_field(
               name=f"Texto cifrado",
               value=f'``{encode}``'
               ,inline=False
          )
          
          await ctx.reply(embed = embed,
                          mention_author=False)

def setup(bot):
     bot.add_cog(Hex(bot))