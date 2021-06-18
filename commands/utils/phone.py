from discord.ext import commands
import discord
from commands.utils.core.phoneMethods import Methods

class Phone(commands.Cog):
     def __init__(self, bot:commands.Bot):
          self.bot = bot
          self.methods = Methods()
          
     @commands.command()
     async def phone(self, ctx : commands.Context, *, country):
          """
          
Genera números de telefonos de distintos paises
**Sintaxis:** **``tphone <pais>``**

          """
          if country in self.methods.countries_list:
               countryCode = self.methods.countries[str(country)]['code']
               desc = ''
               count = 0
               while count <= 30:
                    number = self.methods.generate(self.methods.countries[str(country)]['length'])
                    if self.methods.check(f'{countryCode}{number}'):
                         desc += f'\nhttps://wa.me/+{countryCode}{number}'
                         count += 1
                    else:
                         continue
               
               embed = discord.Embed(
                    color=ctx.message.author.color
               )

               embed.add_field(
                    name=f"Números de ***{country}*** generados",
                    value=f'{desc}'
               )
               
               await ctx.reply(embed = embed,
                               mention_author = False)

               
          else:
               desc = ''
               for c in self.methods.countries_list:
                    desc += f'\n{c}'
                    
               embed = discord.Embed(
                    title="Ese país __no figura en nuestra lista de países__",
                    color=discord.Color.from_rgb(255, 2, 1)
               )
               
               embed.add_field(
                    name="Países __disponibles__",
                    value=desc
               )
               
               embed.set_author(
                    name=ctx.message.author.name,
                    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    icon_url=ctx.message.author.avatar_url
               )
               
               embed.set_footer(
                    text=f"{self.bot.user.name} in {ctx.guild.name}",
                    icon_url=ctx.guild.icon_url
               )
               
               embed.set_image(
                    url="https://i.ytimg.com/vi/Vh3yIY3Gg98/mqdefault.jpg"
               )
               await ctx.reply(embed = embed,
                               mention_author=False)
               
def setup(bot):
     bot.add_cog(Phone(bot))