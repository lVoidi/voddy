from discord.ext import commands
from discord import Embed, Intents
from json import load

with open("bot.json") as bot_info:
     bot = load(bot_info)
     token = bot["TOKEN"]
     prefix = commands.when_mentioned_or(bot["PREFIX"])
     VERSION = bot["VERSION"]

it = Intents().all()

client = commands.Bot(command_prefix=prefix,
                      help_command=None,
                      description="Bot mas troll que conocerás",
                      intents=it)


cogList = [
#    eventos        #
     "events.events",

#    Comandos       #
#    Utilidad
     "help",
     "commands.utils.encrypt",
     "commands.utils.sha",
     "commands.utils.md5",
     "commands.utils.base64",
     "commands.utils.base85",
     "commands.utils.hex",
     "commands.utils.shellcode",
     "commands.utils.phone",
     "commands.utils.whois",
     "commands.utils.qr",
     "commands.utils.clone",
     "commands.utils.findin",
     "commands.utils.grep",
     "commands.utils.info",
     "commands.utils.img",
     "commands.utils.random",
     "commands.utils.proxy",
     "commands.utils.font",
     "commands.utils.crypto.crypto",
#   Diversión
     "commands.fun.tux",

#   Management
     #"commands.manage.emoji",
]

@client.command()
async def ping(ctx : commands.Context):
     """
Devuelve el ping del bot

**Sintaxis:** **``=ping``**
     """
     embed = Embed(title=f"Ping de {client.user.name}",
                   description="**{0:.2f}ms**".format(client.latency*1000),color=ctx.author.color)
     
     await ctx.reply(embed=embed, mention_author=False)




if __name__ == "__main__":
     
#    Carga todas las extensiones
     for cog in cogList:
          try:
               client.load_extension(name=cog)
               print("Cargado: "+cog)
               
          except Exception as e:
               exc = f"{type(e).__name__} : {e}"
               print(exc)
          
#    Carga el token del bot
     client.run(token)