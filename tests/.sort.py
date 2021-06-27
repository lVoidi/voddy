def sortArr(lista : list) -> list:
  n_list = len(lista)
  
  
  for num in range(n_list-1):
# Primero recorremos un bucle que 
# num significaría los index de la lista
# Si no sabe que es index, es la ubicacion de
# un elemento de lista, por ejemplo, si tenemos
# esta lista: [1, 2, 3], el numero 1 representaría el index
# 0, ya que este es el primer elemento de lista, es 0 porque
# los index se cuentan desde 0. El metodo len(lista) devuelve
# el numero de elementos contando desde 1, asi que hay que restarle 1
# para poder usar la variable "num" como index de la lista para que
# no haya ningun error. Si no estuviera restando 1, al final intentará
# usar como index de la lista un numero que está fuera del rango de numero
# de elementos, por ejemplo: 
# lista         =   [0, 3, 2]
# los index     =    0  1  2 
#
# len(lista) -> 3
# 
# for num in range(len(lista)):
#   print(f"Elemento: {lista[num]}")
#
# Por cada numero en el rango de 0 a el numero de elemntos de la lista,
# va a intentar acceder al elemento de la lista con el elemento que tenga
# de index el numero que actualmente se está recorriendo
# Aquí el problema radica en que al final va a dar error, porque en 
# "range(len(lista))" al final va a intentar buscar el index "3", el cual no existe
#

    for index in range(n_list-num-1):
# Este bucle va a recorrer por cada index de atrás para adelante,
# pero al decirle "-1", estamos empezando desde el penultimo elemento
      if lista[index] > lista[index+1]:
        # Ejemplo:
        # Si tenemos la lista [4, 2, 1, 3], va a comparar si 1 es  mayor
        # que 3 primero, y si lo es, va a cambiar de lugar los 2 numeros
        
        lista[index], lista[index+1] = lista[index+1], lista[index] 
        # Los elementos intercambian lugares
  
  return lista

listaPrueba = [10, 15, 2, 42, 3, 5, 12]
for element in sortArr(listaPrueba):
  print(element)
  
  # Resultado :
  # 2
  # 3
  # 5
  # 10
  # 12
  # 15
  # 42