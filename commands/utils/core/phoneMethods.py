
import phonenumbers
import random
import string

class Methods:
     def __init__(self):
          self.countries = {
               'costa rica' : {
                    'code' : 506,
                    'length' : 8
               },
               
               'pakistan' : {
                    'code' : 92,
                    'length' : 9
               },
               
               'siria' : {
                    'code' : 963,
                    'length' : 9
               },
               
               'mexico' : {
                    'code' : 52,
                    'length' : 10
               },
               
               'argentina' : {
                    'code' : 54,
                    'length' : 10
               },
               
               'chile' : {
                    'code' : 56,
                    'length' : 9
               },
               
               'bolivia' : {
                    'code' : 591,
                    'length' : 9
               },
               
               'rusia' : {
                    'code' : 7,
                    'length' : 10
               },
               
               'usa' : {
                    'code' : 1,
                    'length' : 10
               },
               
               'españa' : {
                    'code' : 34,
                    'length' : 9
               },
               
               'china' : {
                    'code' : 86,
                    'length' : 10
               },
               
               'japon' : {
                    'code' : 81,
                    'length' : 10
               },

               'irak' : {
                    'code' : 964,
                    'length' : 9
               },
               
        
          }
          self.countries_list = []
          for key in self.countries.keys():
               self.countries_list.append(key)
          
     def generate(self, length : int) -> int:
          """Funcion que genera números deacuerdo al numero de dígitos
          pasados por parámetros

          Args:
              length (int): Numero de dígitos que el numero va a tener

          Returns:
              int: El numero entero con la cantidad de dígitos indicada
          """
          var = ''
          
          for _ in range(length):
               r="".join(random.choice(string.digits))
               var += r
          
          return int(var)

     def check(self, phone):
          self.phone_number = phonenumbers.parse(f'+{phone}', None)
          if phonenumbers.is_valid_number(self.phone_number):
               return True
          
          else:
               return False


