# Discord
# Regex
import re
from urllib.parse import quote_plus
# Web scrapping
from urllib.request import Request, urlopen

import discord
from discord.ext import commands

# Templates
from templates.error_handler import on_unexpected_error


class Findin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def findin(self, ctx, site: str, user: str):
        """
        Encuentra al usuario en el sitio web que diga
        **Sintaxis:** **``=findin <sitio> <usuario>``**
        """
        try:

            # Inicializa la url
            # Este comando usa google dorks
            url = f'https://google.com/search?q={quote_plus(f"site:{site} intext:{user}")}'

            # Crea el objeto de tipo request
            req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

            # La respuesta de google
            response = urlopen(req)

            # Encuentra todas las urls
            geturls = re.findall(r'href="/url\?q=([\w\.\/\?\=\:\-\_]+/[$&+,:;=?^@#\'<>.^*()%!-]*[\w\.\/\?\=\:\-\_]+)',
                                 response.read().decode('utf-8', 'ignore'))

            # Crea el embed
            embed = discord.Embed(title=f'Se ha encontrado a {user} en {site}')

            # Inicializa la variable donde se van a guardar las urls
            str_urls = ''

            # Itera sobre todas las urls encontradas
            for url in geturls:
                str_urls += f'{str(url).replace("%40", "@")}\n' if 'google' not in url else ''

            # Entra en este condicional si no encuentra ningun resultado
            if len(str_urls) < 1:
                embed = discord.Embed()
                embed.color = 0xff0000
                embed.title = f"No se ha encontrado a {user} en {site}"
                embed.description = 'Prueba usando otros nombres de usuario y otros sitios'

                await ctx.reply(embed=embed)
                return

            # Crea la descripcion del embed con todos los links
            embed.description = f'Se ha encontrado en las siguientes urls:\n {str_urls}'

            # Color del embed (azul)
            embed.color = 0x0000ff

            # Responde al mensaje
            await ctx.reply(embed=embed, mention_author=False)

        # En caso de un error inesperado,
        # va a llamar al template antes
        # importado para dar mas informacion
        # sobre el error
        except Exception as e:
            em = on_unexpected_error(e)
            await ctx.reply(embed=em)

    # Error handler de discord
    @findin.error
    async def on_error(self, ctx, error):

        # Entra en este condicional si el usuario no ha puesto algun\
        # argumento necesario para que el comando funcione
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Este comando requiere de **dos argumentos!** Sintaxis: **``=findin <sitio> <usuario>``**')


def setup(bot):
    bot.add_cog(Findin(bot))
