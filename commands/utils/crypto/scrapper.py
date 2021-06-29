# Archivo que saca la informacion de las criptos
#
#
#
#```````````````````````````````````````````````#

# Importa el modulo necesario
import cryptocompare

# Esta funcion devuelve un diccionario con los datos necesarios
def get_info(crypto : str) -> dict:
  crypto = cryptocompare.get_avg(crypto.upper())
  
  # Cryptocompare retorna nonetype cuando no encuentra la cryptomoneda,
  # lo cual nos ayudara para alertar al usuario de que la moneda ingresada 
  # no es valida
  if crypto == None:
    return None
  
  # Retorna el diccionario correspondiente
  return dict(
  	# Accede al precio mas bajo en 24hrs
    low=crypto['LOW24HOUR'],

    # Accede al precio mas alto en 24hrs
    high=crypto['HIGH24HOUR'],

    # Accede al precio actual
    actual = crypto['PRICE']
  )
