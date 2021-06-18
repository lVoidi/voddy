from discord.ext import commands
from discord import Embed, Intents

it = Intents().all()

client = commands.Bot(command_prefix=commands.when_mentioned_or("t", "t/"),
                      help_command=None,
                      description="Bot mas troll que conocerás",
                      intents=it)


cogList = [
#    eventos        #
     "events.events",

#    Comandos       #
#    Utilidad
     "help",
     "commands.utils.base64",
     "commands.utils.hex",
     "commands.utils.phone",
     "commands.utils.whois"
]

@client.command()
async def ping(ctx : commands.Context):
     """
*Devuelve el ping del bot*

**Sintaxis:** **``tping``**
     """
     embed = Embed(title="Ping de trollencio",
                   description="**{0:.2f}ms**".format(client.latency*1000),color=ctx.author.color)
     
     await ctx.reply(embed=embed, mention_author=False)


if __name__ == "__main__":
     
#    Carga todas las extensiones
     for cog in cogList:
          client.load_extension(name=cog)

#    Carga el token del bot
     # client.run("ODUwMDY4ODQ1MjE2Mzk5NDcw.YLkWTg.C6shAU5Q2z29spoWSd8pF2QziYI")
     client.run("ODU0MTY2NzQwNDk4MjUxNzc3.YMf-xA.ea5xJOooFdv3Tj11X32U58Ad6jo")