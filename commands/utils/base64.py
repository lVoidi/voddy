# Importa los módulos de discord
import discord
from discord.ext import commands

# Importa el módulo de base64
import base64


# Inicializa la clase del cog
class Base64(commands.Cog):
    # Método constructor
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # Comando
    @commands.command()
    async def base64(self, ctx: commands.Context, *, text: str):

        """
Codifica en base64 el texto que el usuario diga

**Sintaxis:** **``=base64 <texto>``**
        """

        # Si el texto es muy largo, va a cancelar el comando
        if len(text) > 1024:
            await ctx.send("Ey, el texto tiene que ser mas corto")
            return

        # Codifica el texto en bytes
        bytes = text.encode("utf-8")

        # Códifica los bytes en base64
        base64_bytes = base64.b64encode(bytes)

        # Codifica los  bytes en base64 en un string
        base64_string = base64_bytes.decode("ascii")

        # Crea el embed
        embed = discord.Embed(
            title=f"Codificador base64",
            color=ctx.message.author.color
        )

        # Crea el campo con el texto codificado
        embed.add_field(
            name=f"Texto codificado",
            value=f"``{base64_string}``",
            inline=False
        )

        # Responde al mensaje
        await ctx.reply(embed=embed,
                        mention_author=False)

    # Comando de decodificación
    @commands.command()
    async def dbase64(self, ctx: commands.Context, *, text: str):
        """
Decodifica en base64 el texto que el usuario diga

**Sintaxis:** **``=dbase64 <texto>``**
        """

        # Si el texto es muy largo, cancela el comando
        if len(text) > 1024:
            await ctx.send("Ey, el texto tiene que ser mas corto")
            return

        # convierte el string de base64 en bytes
        bytes = text.encode("utf-8")

        # decodifica los bytes de base64
        base64_bytes = base64.b64decode(bytes)

        # convierte el texto decodificado en un string legible
        base64_string = base64_bytes.decode("ascii")

        # crea el embed
        embed = discord.Embed(
            title=f"Decodificador base64",
            color=ctx.message.author.color
        )

        # Crea el campo con el texto decodificado
        embed.add_field(
            name=f"Texto decodificado",
            value=f"``{base64_string}``",
            inline=False
        )

        # responde al mensaje
        await ctx.reply(embed=embed,
                        mention_author=False)

    # Por si falta algun argumento al comando
    @base64.error
    @dbase64.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Recuerda que este comando recibe como parámetro el texto a codificar/decodificar")


def setup(bot):
    bot.add_cog(Base64(bot=bot))
