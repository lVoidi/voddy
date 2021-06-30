#    Bienvenido a los eventos de voddy

# Importa los módulos de discord necesario
from discord.ext import commands
import discord

# Template
from templates.error_handler import on_unexpected_error

class Events(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot
     
     # Evento cuando el bot se conecta
     @commands.Cog.listener()
     async def on_ready(self):
          """
Cambia su estado a "jugando a x servers | thelp"
          """
          
          # len(self.bot.guilds) → número de servidores en el que el bot está conectado
          status = f"{len(self.bot.guilds)} servers | =help"

          # En el estado aparecerá que es de tipo juego
          game = discord.Game(name=status)

          await self.bot.change_presence(activity=game)
          
#         Imprime por pantalla que el bot está listo
          print("Bot listo")          
     
#    Evento de los errores
#    Errores globales o en común
     @commands.Cog.listener()
     async def on_command_error(self, ctx:commands.Context, error):

          # Si el comando está en cooldown...
          #    isinstance → bool: true si el objeto pasado por el primero parametro
          #                        es una instancia de la clase del segundo parámetro
          if isinstance(error, commands.CommandOnCooldown):
               em = discord.Embed(color=0xFF0033)
               em.title="Cuidado! comando en cooldown!"
               em.description = f"Intenta de nuevo en {error.retry_after:.2f} segundos"
               await ctx.reply(embed = em)

          elif isinstance(error, commands.BadArgument):
               await ctx.reply('Ese comando no recibe ese tipo de argumentos')

          elif isinstance(error, commands.MissingRequiredArgument):
               await ctx.reply('Al comando le falta un argumento! escribe ``=h <comando>`` para ver los argumentos que ocupa!')
          
          elif isinstance(error, commands.CommandNotFound):
               try:

                    message_content = str(ctx.message.content)
                    hashmap_coincidences = {}
                    for command in self.bot.commands:
                         hashmap_coincidences[command.name] = 0
                         for letter in command.name:
                              if letter in message_content.replace('=', ''):
                                   hashmap_coincidences[command.name] += 1

                    most_congruent_name = ''
                    list_num_coincidences = [hashmap_coincidences[key] for key in hashmap_coincidences.keys() if hashmap_coincidences[key] != 0 and hashmap_coincidences[key] > len(message_content.replace('=', ''))//2]
                    
                    list_iter_changes = []
                    for key in hashmap_coincidences.keys():    

                         if hashmap_coincidences[key] > sorted(list_num_coincidences, reverse=True)[0]:
                              congruent_name = list(hashmap_coincidences.keys())[list(hashmap_coincidences.values()).index(list_num_coincidences[0])]
                              for name in hashmap_coincidences.keys():
                                   if str(name).startswith(congruent_name) or name in str(congruent_name):
                                        most_congruent_name += f'{name}\n'
                                        

                         try:
                              if list_num_coincidences[0] > list_num_coincidences[1]:

                                   del list_num_coincidences[1]


                              else:
                                   if list_num_coincidences[1] == list_num_coincidences[0]:
                                        pass

                                   else:
                                        del list_num_coincidences[0]
                         except IndexError:
                              break

                         else:
                              most_congruent_name = f'{list(hashmap_coincidences.keys())[list(hashmap_coincidences.values()).index(list_num_coincidences[0])]}\n'
                              break

                         list_iter_changes.append(len(list_num_coincidences))

                         if len(list_iter_changes) > 3:
                              if list_iter_changes[len(list_iter_changes)-1] == list_iter_changes[len(list_iter_changes)-2] and list_iter_changes[len(list_iter_changes)-2] == list_iter_changes[len(list_iter_changes)-3]:
                                   break

                    embed = discord.Embed(color=0xFF0033)
                    embed.description = 'No se ha encontrado ese comando'

                    embed.add_field(
                         name='Quiziste decir...',
                         value=f'**``{most_congruent_name}``?**'
                    )

                    await ctx.reply(embed = embed)

               except Exception as e:
                    embed = on_unexpected_error(e)
                    await ctx.reply(embed = embed)

#    Setup
def setup(bot : commands.Bot):
     bot.add_cog(Events(bot=bot))