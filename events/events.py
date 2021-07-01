#    Bienvenido a los eventos de voddy

import discord
# Importa los módulos de discord necesario
from discord.ext import commands

from index import VERSION
# Template
from templates.error_handler import on_unexpected_error


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
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
    async def on_command_error(self, ctx: commands.Context, error):

        # Si el comando está en cooldown...
        #    isinstance → bool: true si el objeto pasado por el primero parametro
        #                        es una instancia de la clase del segundo parámetro
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(color=0xFF0033)
            em.title = "Cuidado! comando en cooldown!"
            em.description = f"Intenta de nuevo en {error.retry_after:.2f} segundos"
            await ctx.reply(embed=em)

        elif isinstance(error, commands.BadArgument):
            await ctx.reply('Ese comando no recibe ese tipo de argumentos')

        elif isinstance(error, commands.CommandNotFound):
            try:
                wrong_command = str(ctx.message.content).replace('=', '')
                embed = discord.Embed(color=0xFFAAAB)
                embed.description = '**No se ha encontrado un comando con ese nombre**'

                coincidences = {}
                aproximate_names = ''

                for command in self.bot.commands:
                    coincidences[command.name] = 0

                    for letter in str(command.name):
                        if letter in wrong_command:
                            coincidences[command.name] += 1

                    if coincidences[command.name] in range(len(wrong_command) - (len(wrong_command) - 1),
                                                           len(wrong_command) // 2):
                        del coincidences[command.name]

                    else:
                        if coincidences[command.name] > len(wrong_command) // 2 and str(command.name).startswith(
                                wrong_command) == False:
                            aproximate_names += f'**``{command.name}``**\n'

                        elif str(command.name).startswith(wrong_command):
                            aproximate_names += f'**``{command.name}``**\n'
                            break

                del coincidences

                if len(aproximate_names) < 1:
                    embed.add_field(
                        name='Aproximados',
                        value=f'No se ha encontrado nada parecido'
                    )

                else:
                    embed.add_field(
                        name='Aproximados',
                        value=aproximate_names
                    )

                embed.set_footer(text=f' | Este aproximado puede ser poco acertado || v{VERSION}',
                                 icon_url=self.bot.user.avatar_url
                                 )

                await ctx.reply(embed=embed)

            except Exception as e:
                embed = on_unexpected_error(e)
                await ctx.reply(embed=embed)


#    Setup
def setup(bot: commands.Bot):
    bot.add_cog(Events(bot=bot))
