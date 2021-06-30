from discord import Embed


def return_embed(client, **kwargs) -> Embed:
    """
Retorna un embed para diferentes situaciones,
ahorrando lineas de código

argumentos:
    fields || field
    Diccionario con los campos que
    se agregarán al embed

    description || desc
    La descripción del embed

    footer || foot
    Footer del embed, diccionario en el
    que irá el texto y la url del icono
    """
    embed = Embed()

    for key, value in kwargs:
        if key == "fields" or key == "field":
            for name, desc in value:
                if name == "inline" and desc == True:
                    embed.add_field(name=name, value=desc, inline=True)

                else:
                    embed.add_field(name=name, value=desc, inline=False)

        elif key == "description" or key == "desc":
            embed.description = value

        elif key == "footer" or key == "foot":
            for txt, icon in value:
                embed.set_footer(text=txt, icon_url=icon)

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    return embed
