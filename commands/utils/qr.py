# Imports de discord
# Para poder borrar el código qr después
import subprocess
from json import loads
# Para poder acceder a la api que lee el código qr
from urllib import request, parse

import discord
from discord.ext import commands
# Creador de código qr
from qrcode import QRCode, constants

# Importa la versión del bot
from index import VERSION
# Importa el template del error handler
from templates.error_handler import on_unexpected_error


# Inicializa la clase
class Qr(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Pone un cooldown de 20 segundos
    @commands.cooldown(1, 20, type=commands.BucketType.user)
    @commands.command()
    async def qr_make(self, ctx: commands.Context, *, data: str):
        """
        Crea tu propio código qr con este comando, ya sea links o texto
        **Sintaxis:** **``=qr_make <data>``**
        """

        try:

            # Crea el objeto de tipo QRCode
            qr = QRCode(
                version=1,
                error_correction=constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            # Le pone los datos que el usuario pasó por args
            qr.add_data(data)

            # Crea el código qr
            qr.make(fit=True)

            # Crea una imagen
            img = qr.make_image(fill_color="black", back_color="white")

            # Guarda la imagen en formato png
            img.save(f"commands/utils/.temp/{ctx.message.id}.png", format="png")

            # Responde el mensaje
            await ctx.reply(content="<a:tux_programando:858807224645058581>",
                            file=discord.File(f"commands/utils/.temp/{ctx.message.id}.png", spoiler=True))

            # Borra el código qr para ahorrar espacio en memoria
            subprocess.run(f"rm commands/utils/.temp/{ctx.message.id}.png", shell=True)

        # Por si hay algún error inesperado
        except Exception as e:
            em = on_unexpected_error(error=e)

            await ctx.reply(content='<a:tux_programando:858807224645058581>', embed=em)

    # Cooldown de 20 segundos
    @commands.cooldown(1, 20, type=commands.BucketType.user)
    @commands.command()
    async def qr_read(self, ctx: commands.Context, url=None):
        """
        Lee los códigos qr que quieras con este comando
        **Sintaxis:** **``=qr_read <url de la imagen || imagen adjunta>``**
        """

        # Si la url es diferente a Nonetype
        if url != None:

            # codifica la url en urlencode
            enc = parse.urlencode({"": f"{url}"})

        # Y si no...
        else:
            try:

                # va a usar como url la imagen en el mensaje
                enc = parse.urlencode({"": f"{ctx.message.attachments[0].url}"})

            # Y si no es ningún caso de esos...
            except Exception as e:
                await ctx.reply("al parecer no hay ninguna imagen en tu mensaje <a:tux_programando:858807224645058581>")

        # Crea los headers correspondientes
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

        # Hace un request a la api para leer los códigos qr
        req = request.Request(url=f"http://api.qrserver.com/v1/read-qr-code/?fileurl{enc}", headers=hdr)

        # Guarda la respuesta en esta variable
        response = request.urlopen(req)

        # Guarda el json de la respuesta en esta variable
        s = loads(response.read())

        # Crea el embed
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

        # Pone la imagen correspondiente en el embed
        embed.set_image(url=url if url != None else ctx.message.attachments[0].url)

        # Responde al mensaje con el embed correspondiente
        await ctx.reply(content="<a:tux_programando:858807224645058581>",
                        embed=embed,
                        mention_author=False)

    @qr_make.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Escribe los datos para convertirlos en qr!')


def setup(bot):
    bot.add_cog(Qr(bot))
