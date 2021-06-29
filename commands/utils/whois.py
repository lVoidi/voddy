# Importa el modulo request de la libreria urllib
from urllib import request

# Importa el metodo loads del modulo json
from json import loads

# Importa los modulos de discord necesarios
from discord.ext import commands
from discord import Embed, Color

# Importa el error handler
from templates.error_handler import on_unexpected_error

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

               # Url de la api
               site= f"https://ipinfo.io/{ip}/json"
               
               # Los headers para que no salte ningun error
               hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}

               # Crea el objeto de clase Request
               req = request.Request(site, headers=hdr)

               # La respuesta de la api
               response = request.urlopen(site)
               
               # Carga los datos json de la pagina
               resp_dict = loads(response.read().decode())
               
               # Crea el embed
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
               embed = on_unexpected_error(error)
               
               await ctx.reply(embed = embed,
                              mention_author=False)
     
     @whois.error 
     async def on_error(self, ctx, error):
          if isinstance(error, commands.MissingRequiredArgument):
               await ctx.reply('Este comando requiere de un argumento para funcionar: la ip')

def setup(bot):
     bot.add_cog(Whois(bot))
          
          