from urllib import request, parse
from json import loads
from discord.ext import commands
from qrcode import QRCode, constants
import discord
import subprocess
from index import VERSION
from templates.error_handler import on_unexpected_error


class Qr(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot
     
     @commands.cooldown(1, 20, type=commands.BucketType.user)
     @commands.command()
     async def qr_make(self, ctx : commands.Context, *, data : str):
          """
          Crea tu propio código qr con este comando, ya sea links o texto
          **Sintaxis:** **``=qr_make <data>``**
          """
          
          try:
               qr = QRCode(
                    version=1,
                    error_correction=constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
               )
               qr.add_data(data)
               qr.make(fit=True)

               img = qr.make_image(fill_color="black", back_color="white")

               img.save(f"commands/utils/.temp/{ctx.author.id}.png", format="png")

               await ctx.reply(content="<a:tux_programando:858807224645058581>", file = discord.File(f"commands/utils/.temp/{ctx.author.id}.png", spoiler=True))
               
               subprocess.run(f"rm commands/utils/.temp/{ctx.author.id}.png", shell=True)

          except Exception as e:
               em = on_unexpected_error(error=e)
               
               await ctx.reply(content='<a:tux_programando:858807224645058581>',embed = em)
     
     @commands.cooldown(1, 20, type=commands.BucketType.user)
     @commands.command()
     async def qr_read(self, ctx : commands.Context, url = None):
          """
          Lee los códigos qr que quieras con este comando
          **Sintaxis:** **``=qr_read <url de la imagen || imagen adjunta>``**
          """
          if url != None:
               enc = parse.urlencode({"" : f"{url}"})

          else:
               try:
                    enc = parse.urlencode({"" : f"{ctx.message.attachments[0].url}"})

               except Exception as e:
                    await ctx.reply("al parecer no hay ninguna imagen en tu mensaje <a:tux_programando:858807224645058581>")
                         
          
          hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}

          
          req = request.Request(url=f"http://api.qrserver.com/v1/read-qr-code/?fileurl{enc}", headers=hdr)
          response = request.urlopen(req)
          s = loads(response.read())
          
          embed = discord.Embed()
          embed.add_field(
               name="Resultado",
               value=f"{s[0]['symbol'][0]['data']}"
          )
          
          embed.set_footer(
               text=f" | v{VERSION}",
               icon_url=self.bot.user.avatar_url
          )

          
          embed.color = discord.Color.gold()
          
          embed.set_image(url=url if url != None else ctx.message.attachments[0].url)
          
          
          await ctx.reply(content="<a:tux_programando:858807224645058581>",embed = embed,
                          mention_author=False)
          
       
def setup(bot):
     bot.add_cog(Qr(bot))