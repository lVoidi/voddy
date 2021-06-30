#	Idea de luijait
#	https://github.com/luijait

import string

import discord
from discord.ext import commands

from templates.error_handler import on_unexpected_error


class Bin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def binaryToDecimal(self, binary):
        return int(binary, 2)

    @commands.command()
    async def bin(self, ctx: commands.Context, *, data: str):
        """
        Convierte en binario lo que el usuario diga
        **Sintaxis:** **``=bin <texto/numero>``**
        """
        try:
            # Inicializa la variable con el binario
            binary = ''

            # Crea el embed
            embed = discord.Embed()
            embed.color = 0xaaffaa
            embed.title = f'Convertidor binario'
            embed.set_footer(text=' · luijait',
                             icon_url='https://images-ext-2.discordapp.net/external/hHltjO-_i0FwFY6V9AXdCuHT2h0GypQ3AkF0gwwLXno/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/399646865894932493/5e8d484a3a4169b68883821b32dc32a9.webp')

            try:
                # Si es un numero entero, lo convierte a binario
                # usando el método bin
                binary = bin(int(data)).replace("0b", "")

            except ValueError:

                # Si es un string, lo va a convertir en binario considerandolo como una
                # cadena de texto
                # src: https://www.geeksforgeeks.org/python-convert-string-to-binary/
                binary = ' '.join(format(ord(i), '08b') for i in data)

            # Crea la descripcion del embed con el string en binario
            embed.description = f'''\n
**``{binary}``**
			'''

            # Responde el mensaje
            await ctx.reply(content="<a:tux_programando:858807224645058581>",
                            embed=embed,
                            mention_author=False)

        # Si hay algún error inesperado
        except Exception as e:
            em = on_unexpected_error(e)
            await ctx.reply(embed=em)

    @commands.command()
    async def dbin(self, ctx: commands.Context, *, data: str):
        """
        Decodifica el binario que el usuario diga
        **Sintaxis:** **``=dbin <texto/numero>``**
        """
        try:

            if ' ' in data:
                data = data.replace(' ', '')

            elif '\n' in data:
                data = data.replace('\n', '')

            if data == None:
                await ctx.reply('Pero chamo, poné un codigo binario')
                return

            try:
                byte_data = int(data, 2)

            except ValueError:
                await ctx.reply(f"Hmmm no me parece que eso es binario: {data}")
                return

            byte_int = byte_data.bit_length() + 7 // 8

            bin_string = byte_data.to_bytes(byte_int, 'big')
            try:
                ascii_text = ''
                for b in bin_string.decode():
                    ascii_text += b if b in f'\t {string.punctuation}{string.ascii_letters}{string.digits}' else ''

            except UnicodeDecodeError:
                ascii_text = ''
                for b in str(byte_data):
                    ascii_text += b if b in f'\t {string.punctuation}{string.ascii_letters}{string.digits}' else ''

            embed = discord.Embed()
            embed.color = 0xaaffaa
            embed.title = f'Decodificador binario'

            embed.description = f'''\n
**``{ascii_text}``**
			'''

            await ctx.reply(content="<a:tux_programando:858807224645058581>",
                            embed=embed,
                            mention_author=False)

        except Exception as e:
            em = on_unexpected_error(e)
            await ctx.reply(embed=em)

    @bin.error
    @dbin.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Por favor, introduce los **datos necesarios** a convertir!')


def setup(bot):
    bot.add_cog(Bin(bot))
