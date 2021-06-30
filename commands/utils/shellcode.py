import discord
from discord.ext import commands

from templates.error_handler import on_unexpected_error


class Shellcode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def shellcode(self, ctx: commands.Context, *, data: str):
        """
Codifica en shellcode el texto que el usuario diga

**Sintaxis:** **``=shellcode <texto>``**
        """

        try:
            if '*' in data:
                try:
                    num = int(data.split('*')[1])
                    text = data.split('*')[0] * num
                    ntext = text.encode('utf-8')

                    encode = ntext.hex()

                    c = 0
                    all_str = ''
                    for letter in str(encode):

                        if c % 2 == 0:
                            all_str += '\\x'

                        c += 1
                        all_str += letter

                    if len(all_str) > 1024:
                        await ctx.send("Ey, el texto tiene que ser mas corto")
                        return

                except ValueError:
                    await ctx.send("Tiene que ser un numero entero para poder multiplicar")
                    return

            else:
                text = data
                ntext = text.encode('utf-8')

                encode = ntext.hex()

                c = 0
                all_str = ''
                for letter in str(encode):

                    if c % 2 == 0:
                        all_str += '\\x'

                    c += 1
                    all_str += letter

                if len(all_str) > 1024:
                    await ctx.send("Ey, el texto tiene que ser mas corto")
                    return

            embed = discord.Embed(
                title=f"Codificador shellcode",
                color=discord.Color.from_rgb(0, 255, 0)
            )

            embed.add_field(
                name=f"Texto a cifrar",
                value=f'``{text}``'
                , inline=False
            )
            embed.add_field(
                name=f"Texto cifrado",
                value=f'``{all_str}``'
                , inline=False
            )

            await ctx.reply(embed=embed,
                            mention_author=False)

        except Exception as e:
            em = on_unexpected_error(e)
            await ctx.reply(embed=e)

    @commands.command()
    async def dshellcode(self, ctx: commands.Context, *, data: str):
        """
Decodifica de shellcode el texto que el usuario diga

**Sintaxis:** **``=dshellcode <texto>``**
        """
        if len(data) > 1024:
            await ctx.send("Ey, el texto tiene que ser mas corto")
            return
        text = ''
        for word in data.split('\\x'):
            text += word

        bytes_object = bytes.fromhex(text)

        ascii_string = bytes_object.decode("utf-8")

        embed = discord.Embed(
            title=f"Decodificador shellcode",
            color=discord.Color.from_rgb(0, 255, 0)
        )

        embed.add_field(
            name=f"Texto a descifrar",
            value=f'``{data}``'
            , inline=False
        )
        embed.add_field(
            name=f"Texto descifrado",
            value=f'``{ascii_string}``'
            , inline=False
        )

        await ctx.reply(embed=embed,
                        mention_author=False)

    @shellcode.error
    @dshellcode.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('a ese comando le falta un parametro, el texto a cifrar/descifrar')


def setup(bot):
    bot.add_cog(Shellcode(bot))
