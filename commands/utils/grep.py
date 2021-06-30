from discord.ext import commands


class Grep(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def grep(self, ctx, type: str):
        """
        Filtra algo en el canal del contexto
        tiene un alcance de solo 200 mensajes
        **Sintaxis:** **``=grep <tipo(message o user)>`**
        """

        # Manda el primer mensaje para decirle al usuario que escriba a
        # continuación la cosa a filtrar
        msg = await ctx.send("Escribe a continuación el contenido a buscar")

        # Guarda el mensaje del usuario dentro de la variable content
        content = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        # Borra el primer mensaje
        await msg.delete()

        # Itera sobre todos los mensajes con un alcance de 200
        async for message in ctx.channel.history(limit=200):

            # Si la id del mensaje original es diferente al mensaje del usuario
            # con el contenido a buscar
            if message.id != content.id:

                # Si el tipo que el usuario especificó es 'message'
                if type == 'message':

                    # Si el contenido concuerda
                    if content.content.lower() in message.content.lower():
                        # Responde al mensaje indicando que encontró un mensaje
                        # con el contenido dicho
                        await message.reply('‌', mention_author=False)
                        break

                # En el caso de que el tipo sea user
                elif type == 'user':

                    # Si el nombre del contenido concuerda con el autor del mensaje
                    # iterado, ejecuta el siguiente código
                    if content.content.lower() in str(message.author).lower():
                        # Responde al mensaje indicando que encontró un mensaje
                        # con el contenido dicho
                        await message.reply('‌', mention_author=False)
                        break

    @grep.error
    async def on_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Tienes que poner el tipo a filtrar! **``=grep <user/message>``**')


def setup(bot):
    bot.add_cog(Grep(bot))
