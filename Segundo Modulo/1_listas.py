'''Las listas son una estructura de datos que nos permite la manipulacion de una enorme cantidad de estos mismos 
hasta el momento me proporcionaron dos formas de declarar una lista: lista = [], haciendo uso de los corchetes puedo declarar 
una lista en donde se puede ingresar todo tipo de datos. O tambien list(), equivalente al caso contrario pero aqui declaramos
la funcion, donde ingresaremos los datos dentro de los parentesis'''
lista1 = ['GYARADOS', 130, 5.27, True]
lista2 = list(('Elgyem', 605, 0.458, False))
print("Lista 1: ",lista1)
print("Lista 2: ",lista2)
#Es recomendable que las listas almacenen un tipo de dato
lista_string = ['PIKACHU', 'SWAMPERT', 'SNORLAX']
lista_int = [23, -56, 43]
lista_float = [45.67, -345.678743, 17.783]
lista_boolean =[True, False, (34<56), (4>3 and 10 != 11)]
print("Lista de caracteres: ",lista_string)
print("Lista de enteros: ",lista_int)
print("Lista de Booleanos: ",lista_boolean)
print("Lista de flotantes: ",lista_float)

'''En este ejemplo vamos a extraer cada uno de los datos que conforma la siguiente lista'''
pokelist =  ['GENGAR', 'TYRANITAR', 'ARTICUNO', 'AZULMARILL', 'DEOXIS']
poke_1 = pokelist[1]
poke_2 = pokelist[0]
poke_3 = pokelist[4]
poke_5 = pokelist[-3]
poke_6 = pokelist[-2]
print("Los datos obtenidos de la lista son: ", poke_1, poke_2, poke_3)
print("Los datos obtenidos son: ", poke_5, poke_6)

'''En este apartado, actualizaremos uno de los datos que conforma la lista 
se usara la lista anterior (pokelist) y se rempalzara el dato "Articuno" por "Metagross"'''
pokelist[2] = 'METAGROSS'
print(pokelist) #sE IMPRIMIRA LA LISTA CON LA ACTUALIZACIÓN DENTRO DE LA LISTA (CAMBIÓ Articuno -> Metagross)

#Sublistas 