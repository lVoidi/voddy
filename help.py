# Carga todos los modulos de discord necesarios
from discord.ext import commands
import discord

# Importa la funcion que maneja los errores inesperados
from templates.error_handler import on_unexpected_error

# Inicializa la clase y hereda los métodos de la clase
# discord.ext.commands.Cog 
class Help(commands.Cog):

     # Método constructor, con la instancia del bot
     def __init__(self, bot : commands.Bot):
          self.bot = bot     
     
     @commands.command(
                     aliases=[
                          "ayuda",
                          "Ayuda",
                          "h"
                     ])
     async def help(self, ctx : commands.Context, command=''):
          """
Comando de ayuda, en este encontrarás todos los comandos
disponibles en el bot
          """
          try:

               # Crea un objeto de tipo embed
               embed=discord.Embed()
               embed.set_thumbnail(url=self.bot.user.avatar_url)
               embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
               embed.add_field(
                    name="Info",
                    value="[Github](https://github.com/lVoidi) \n [Telegram](https://t.me/lVoidi)",
                    inline=False
               )
               
               # Si el usuario no ha especificado el comando, la descripción será esta
               if command=='':
                    
                    embed.description = """
**Comando de ayuda de** [Voiddy](https://discord.com/api/oauth2/authorize?client_id=854166740498251777&permissions=8&scope=bot)
**Prefix:** **``=``**

<a:tux_programando:858807224645058581> ── **diversión**

**``cowsay``** 
<a:tux_programando:858807224645058581> ── **Miscelaneo**

**``ping``** **``help``** **``whois``** **``phone``** **``qr_make``** **``qr_read``** 
**``crypto``** **``proxy``** **``img``** **``findin``** **``random``** **``grep``**
**``fancy``** **``clone``**
<a:tux_programando:858807224645058581> ── **Encriptado**

**``hex``** **``ascii85``** **``encrypt``** **``base64``** 
**``shellcode``** **``md5``** **``bin``**
**``sha1``** **``sha256``** **``sha512``** 

<a:tux_programando:858807224645058581> ── **Desencriptado**
**``dhex``** **``dascii85``** **``dbase64``** **``dshellcode``**
**``dbin``**
                    """    
               
               # si el usuario ha especificado un comando,
               # pondrá de descripcion el nombre del comando junto
               # con su documentación respectiva
               elif command != '':

                    # Revisa si el comando está en la lista de comandos
                    if command in [command.name.lower() for command in self.bot.commands]:
                         
                         # Itera por cada comando
                         for com in self.bot.commands:

                              # si encuentra un comando con el mismo nombre que
                              # el comando pasado por argumentos
                              if com.name.lower() == command.lower() :

                                   # Pues pone de descripción el comando respectivo
                                   embed.description = f"""
     **{com.name}** 

     {com.help}
                                   """
                                   break 

                              # Si no lo logra encontrar, seguirá iterando
                              else:
                                   continue
                    
                    # Si de ninguna manera encuentra el comando,
                    # pone este mensaje
                    else:
                         embed.description = f"""

     No se ha logrado encontrar **``{command}``** en nuestra lista de comandos,
     escribe thelp para ver una simple lista de comandos <a:tux_programando:858807224645058581>


                                   """  
               
               # Envía el embed con toda la información
               await ctx.reply(embed = embed, mention_author=False)
               
               
          # En caso de un error inesperado 
          except Exception as e:

               # Crea el embed importado antes, pasandole
               # por parametros el error
               em = on_unexpected_error(e)
               
               # Envía el error
               await ctx.reply(content="<a:tux_programando:858807224645058581>",embed = em,
                               mention_author=False)

# Setup del cog
def setup(bot):

     # añade el cog
     bot.add_cog(Help(bot))