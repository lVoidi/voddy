from urllib import request
from json import loads
from discord.ext import commands
from discord import Embed, Color
from sys import exc_info
from os import path

class Whois(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot
     
     @commands.command()
     async def whois(self, ctx: commands.Context, ip : str):
          """
Muestra información detallada de una dirección ip

**Sintaxis:** **``=whois <dirección ip>``**
          """
          try:
               site= f"https://ipinfo.io/{ip}/json"
               
               hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}

               req = request.Request(site, headers=hdr)
               response = request.urlopen(site)
               
               resp_dict = loads(response.read().decode())
               
               embed = Embed()
               
               embed.color = Color.random()
               
               for value in resp_dict:
                    
                    embed.add_field(
                         name=value,
                         value=resp_dict[value],
                         inline=False
                    )
                    
               await ctx.reply(embed = embed,
                              mention_author=False)

          except Exception as error:
               embed = Embed()
               exc_type, exc_obj, exc_tb = exc_info()
               fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
               
               exc = f"""
          ```
Error en el archivo {__file__}:
Nombre del error: {type(error).__name__}
Descripción del error: {error}
Información detallada: {exc_type} 
Archivo: {fname} 
Línea: {exc_tb.tb_lineno}
          ```
                         """
     
               embed.description = exc
               
               await ctx.reply(embed = embed,
                              mention_author=False)
               
def setup(bot):
     bot.add_cog(Whois(bot))
          
          