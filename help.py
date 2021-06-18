from discord.ext import commands
import discord
from templates.error_handler import on_unexpected_error


class Help(commands.Cog):
     def __init__(self, bot : commands.Bot):
          self.bot = bot     
     
     @commands.command(
                     aliases=[
                          "ayuda",
                          "Ayuda"
                     ])
     async def help(self, ctx : commands.Context, command=''):
          """
Comando de ayuda, en este encontrarás todos los comandos
disponibles en el bot
          """
          try:
               embed=discord.Embed()
               embed.set_thumbnail(url=self.bot.user.avatar_url)
               embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
               embed.add_field(
                    name="Info",
                    value="[Github](https://github.com/lVoidi) \n [Telegram](https://t.me/lVoidi)",
                    inline=False
               )
               
               if command=='':
                    
                    embed.description = """
**Comando de ayuda de** [trollencio](https://discord.com/api/oauth2/authorize?client_id=850068845216399470&permissions=8&scope=bot)

<:trollcoin:850173125114200094> ── **Utilidad**
**``ping``** **``help``** **``hex``** **``base64``** **``phone``**
                    """
                    
                    
               
               elif command != '':
                    if command in [command.name.lower() for command in self.bot.commands]:
                         for com in self.bot.commands:
                              if com.name.lower() == command.lower() :
                                   embed.description = f"""
     **{com.name}** 

     {com.help}
                                   """
                              
                              else:
                                   continue
               
                    else:
                         embed.description = f"""

     No se ha logrado encontrar **``{command}``** en nuestra lista de comandos,
     escribe thelp para ver una simple lista de comandos


                                   """
               

               else:
                    await ctx.send('que')
                    
               await ctx.reply(embed = embed, mention_author=False)
               
               
                  
          except Exception as e:
               em = on_unexpected_error(e)
               
               await ctx.reply(embed = em,
                               mention_author=False)

     
     
def setup(bot):
     bot.add_cog(Help(bot))
               
               