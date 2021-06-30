import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def server(self, ctx: commands.Context):
        """
        Devuelve un mensaje con toda la información del servidor
        **Sintaxis:** **``=server``**
        """
        embed = discord.Embed();
        embed.color = discord.Color.random();

        embed.set_thumbnail(url=ctx.guild.icon_url);

        try:
            embed.set_image(url=ctx.guild.banner_url);
        except:
            pass;

        embed.add_field(

            name="Owner",
            value=ctx.guild.owner,
            inline=True
        )

        embed.add_field(
            name="Fecha de creación (DD/MM/YY)",
            value=f"**{ctx.guild.created_at.now().day}/{ctx.guild.created_at.now().month}/{ctx.guild.created_at.now().year}**\n{ctx.guild.created_at.now().hour}:{ctx.guild.created_at.now().minute}hrs",
            inline=True
        )

        embed.add_field(
            name="Cantidad de miembros",
            value=f"{ctx.guild.member_count}",
            inline=True
        )

        cat_str = ''
        for cat in ctx.guild.categories:
            cat_str += f"{cat.name}\n"

        embed.add_field(
            name="Categorías del server",
            value=f"**{len(list(ctx.guild.categories))}**",
            inline=True
        )

        chan_str = ''
        for ch in ctx.guild.channels:
            chan_str += f'{ch.name}\n'

        embed.add_field(
            name="Canales",
            value=f"**{len(list(ctx.guild.channels))}**",
            inline=True
        )

        embed.add_field(
            name="Region",
            value=f"{str(ctx.guild.region).capitalize()}",
            inline=True
        )

        embed.add_field(
            name="Canales",
            value=f"Canales de texto: **{len(ctx.guild.text_channels)}**\nCanales de voz: **{len(ctx.guild.voice_channels)}**"
        )

        await ctx.reply(embed=embed,
                        mention_author=False)


def setup(bot):
    bot.add_cog(Info(bot))
