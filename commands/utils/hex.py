import discord
from discord.ext import commands


class Hex(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hex(self, ctx: commands.Context, *, text: str):
        """
Codifica en hexadecimal el texto que el usuario diga

**Sintaxis:** **``=hex <texto>``**
        """
        ntext = text.encode('utf-8')

        encode = ntext.hex()

        embed = discord.Embed(
            title=f"Codificador hexadecimal",
            color=discord.Color.from_rgb(0, 255, 0)
        )

        embed.add_field(
            name=f"Texto a cifrar",
            value=f'``{text}``'
            , inline=False
        )
        embed.add_field(
            name=f"Texto cifrado",
            value=f'``{encode}``'
            , inline=False
        )

        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command()
    async def dhex(self, ctx: commands.Context, *, text: str):
        """
Decodifica en hexadecimal el texto que el usuario diga

**Sintaxis:** **``=dhex <texto>``**
        """
        if len(text) > 1024:
            await ctx.send("Ey, el texto tiene que ser mas corto")
            return

        bytes_object = bytes.fromhex(text)

        ascii_string = bytes_object.decode("utf-8")

        embed = discord.Embed(
            title=f"Decodificador hexadecimal",
            color=discord.Color.from_rgb(0, 255, 0)
        )

        embed.add_field(
            name=f"Texto a descifrar",
            value=f'``{text}``'
            , inline=False
        )
        embed.add_field(
            name=f"Texto descifrado",
            value=f'``{ascii_string}``'
            , inline=False
        )

        await ctx.reply(embed=embed,
                        mention_author=False)

    @hex.error
    @dhex.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Tienes que poner el contenido a cifrar o descifrar!')


def setup(bot):
    bot.add_cog(Hex(bot))
