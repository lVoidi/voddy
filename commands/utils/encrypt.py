from discord.ext import commands
from templates.error_handler import on_unexpected_error
from index import VERSION
import discord
import base64

class Encrypt(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot

     @commands.command()
     async def encrypt(self, ctx : commands.Context, *, data:str):
          """
          Encripta el mensaje que el usuario diga usando 3 metodos:
               **Base85**
                    ↓
                    **Base64**     
                         ↓
                         **Hex**
          **Sintaxis** **``=encrypt <data>``**
          """
          try:
               bytes = data.encode("utf-8")
               base85_bytes = base64.a85encode(bytes)
               base85_str = base85_bytes.decode("utf-8")
               
               bytes = base85_str.encode("utf-8")
               base64_bytes = base64.b64encode(bytes)
               base64_string = base64_bytes.decode("utf-8")
               
               ntext = base64_string.encode('utf-8')
               encode = ntext.hex()
               
               if len(encode) > 1024:
                    embed = discord.Embed().add_field(name="El resultado supera los 1024 caracteres", value="Intenta encriptarlo **por partes**")
                    embed.color = discord.Color.red()
                    await ctx.reply(embed = embed)
                    return
               
               embed = discord.Embed(
                    title=f"Encriptado de 3 capas",
                    color=ctx.message.author.color
               )
               
               embed.add_field(
                    name=f"Texto codificado",
                    value=f"``{encode}``",
                    inline=False
               )
               
               embed.set_footer(text=f"  |  {VERSION}",
                                icon_url=self.bot.user.avatar_url)
               
               await ctx.reply(embed = embed,
                              mention_author=False)
               
          except Exception as e:
               em = on_unexpected_error(e)
               await ctx.reply(embed = em)
               
          
     
def setup(bot):
     bot.add_cog(Encrypt(bot))
