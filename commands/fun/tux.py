# Importa los modulos necesarios de discord
# Importa los metodos necesarios de subprocess
from subprocess import check_output

from discord.ext import commands
import cowsay

class Cowsay(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def cowsay(self, ctx, *, text: str):
        """
        Comando cowsay de linux
        **Sintaxis:** **``=cowsay <texto>``**
        """

        str_chars = ''
        for char in ['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']:
          str_chars += f'{char}\n'
        
        msg = await ctx.reply(f'''
Escoje entre uno de los siguientes personajes:
```
{str_chars}
```
			''')

        choice = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        try:
            output = cowsay.get_output_string(choice.content.lower(),f'{text}')

            await msg.delete()
            await choice.delete()
        except:
            await choice.reply('pero ctm te dije que uno de los personajes que estaban ahi')
            return

        await ctx.reply(f'''
```
{output}
```
			''', mention_author=False)

    @cowsay.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Por favor, pon el texto necesario para que el comando funcione correctamente')


def setup(bot):
    bot.add_cog(Cowsay(bot))
