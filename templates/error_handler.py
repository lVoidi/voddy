from discord import Embed 
import sys, os

def on_unexpected_error(error) -> Embed:
     exc_type, exc_obj, exc_tb = sys.exc_info()
     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

     stringInfo = f"""
```json

Ha ocurrido un error inesperado
Archivo: {fname}
Línea de código exacta: {exc_tb.tb_lineno}
Tipo de error: {type(error).__name__}
Clase: {exc_type}
Error: {error}

```
     """
     
     em = Embed().add_field(name="Error inesperado, notificar al creador!",value=stringInfo).add_field(
          name="__Contacto__",
          value="""
Discord:       lVoid#6969
[Twitter](https://twitter.com/VoidVoidi)
[Telegram](https://t.me/lVoidi)
          """
     )
     
     return em


     
     