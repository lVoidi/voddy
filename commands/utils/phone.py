# Importa los modulos de discord
from discord.ext import commands
import discord

# Importa los metodos necesarios para generar los numeros
from commands.utils.core.phoneMethods import Methods

class Phone(commands.Cog):
     def __init__(self, bot:commands.Bot):
          self.bot = bot
          # Instancia de la clase Methods 
          self.methods = Methods()

     @commands.command()
     async def phone(self, ctx : commands.Context, *, country):
          """
          
Genera números de telefonos de distintos paises
**Sintaxis:** **``=phone <pais>``**

          """

          


          # Valora si el pais figura en la lista de paises
          if country in self.methods.countries_list:

               # Genera un numero para el pais dicho
               countryCode = self.methods.countries[str(country)]['code']
               
               # Inicializa las variables necesarias
               desc = ''
               count = 0

               # mientras el contador sea menor o igual a 30...
               while count <= 30:

                    # va a generar un numero del pais dicho
                    number = self.methods.generate(self.methods.countries[str(country)]['length'])
                    
                    # y si el numero es real...
                    if self.methods.check(f'{countryCode}{number}'):

                         # va a agregar a la descripcion el numero
                         desc += f'\nhttps://wa.me/+{countryCode}{number}'

                         # y aumentara el contador en 1
                         count += 1

                    #  y si no es real...
                    else:

                         # continuara con el loop
                         continue
               
               # crea el embed
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
     
     @phone.error 
     async def on_error(self, ctx, error):
          if isinstance(error, commands.MissingRequiredArgument):
               await ctx.reply('te falta poner el pais del cual quieres generar numeros')

          


def setup(bot):
     bot.add_cog(Phone(bot))