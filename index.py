#                                    @@@                   @@  *@@@                                 
#                                   @@@@@                  @@@  *@                                   
#                                 @@@@@@@                @@@@@                                       
#                                 @@@@@@@*               @@@@@                                       
#                                 @@@@@@/$            @  @@@@                                        
#                                 (@@@ @@@          *@@  @@%                                         
#                                  @@@@@@@         @@@@  @                                           
#                                  @@@@@@@       @@@@@@                                              
#                                  @@@@@@@      @@@@@@&                                              
#                                  @@@@@@@    @@@@@@@                                                
#                                  @@@@@@@   @@@@@@.$                                                
#                                  @  @@@@ @@@@@@@                                                   
#                                   @@@@@@@@@@@@                                                     
#                                   @@@@@@@@@@.                                                      
#                                   @@@@@@@@@                                                        
#                                   @@@@@@@
# Bot by lvoidi
# lVoid#6969
# @VoidVoidi en twitter
#
#
# Cualquiera puede basarse en este código, siempre y cuando de los
# créditos respectivos 
#
# ····································································#

# Importa el método load para cargar
# el archivo json como un hashmap
from json import load

# Importa desde el módulo discord las
# clases necesarias, como el embed para poder
# hacer mensajes con mas métodos y capacidades
# decorativas
from discord import Embed, Intents
# Importa el módulo commands para poder
# usar varias instancias de éste (Context, Bot)
from discord.ext import commands

# Abre el archivo con las configuraciones del bot
with open("bot.json") as bot_info:
    bot = load(bot_info)
    token = bot["TOKEN"]
    prefix = commands.when_mentioned_or(bot["PREFIX"])
    VERSION = bot["VERSION"]

# Los intents para poder usar más comandos
it = Intents().all()

# El objeto de la clase discord.ext.commands.Bot
client = commands.Bot(command_prefix=prefix,
                      help_command=None,
                      description="Bot mas troll que conocerás",
                      intents=it)

# La lista de archivos donde se encuentran los comandos
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
    "commands.utils.binary",
    "commands.utils.random",
    "commands.utils.proxy",
    "commands.utils.font",
    "commands.utils.crypto.crypto",
    #   Diversión
    "commands.fun.tux",

    #   Management
    # "commands.manage.emoji",
]


# Prueba de ping
@client.command()
async def ping(ctx: commands.Context):
    """
Devuelve el ping del bot

**Sintaxis:** **``=ping``**
    """

    # Objeto de la clase embed
    # redondea la propiedad del bot latency, a 2 decimales
    embed = Embed(title=f"Ping de {client.user.name}",
                  description="**{0:.2f}ms**".format(client.latency * 1000), color=ctx.author.color)

    # Envía el mensaje
    await ctx.reply(embed=embed, mention_author=False)


# Si no está siendo importado...
if __name__ == "__main__":

    #    Cargará todas las extensiones
    for cog in cogList:
        try:
            client.load_extension(name=cog)

            # Imprime cuando una extensión es cargada
            print("Cargado: " + cog)

        except Exception as e:

            # En caso de un error, imprimirá un mensaje en pantalla con el
            # error respectivo
            exc = f"{type(e).__name__} : {e}"

            # Imprime el errror
            print(exc)

    #    Carga el token del bot
    client.run(token)
