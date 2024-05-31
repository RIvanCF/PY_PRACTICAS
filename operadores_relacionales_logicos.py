'''
Los operadores relacionales son los siguientes: 
    * > : Mayor que ...
    * < : Menor que ...
    * >= : Mayor o igual que ... 
    * <= : Menor o igual que ... 
    * == : Igual a ... 
    * != : Diferente ...
Nota: Doble signo igual (==) para los operadores relacionales es a una equivalencia entre dos valores del mismo valor, mientras que un signo igual (=) es una asignación
de datos.

Al comparar dos valore con estos aoperadores, la consola nos soltará un valor Booleano 
'''
print("Operadores relacionales \n")
number_1 = 40 
number_2 = 70
result_1 = 40 > 70
result_2 = 70 > 40
print("Operador 'Mayor que...' (>)")
print("¿",number_1,"es mayor que ", number_2,"? ",result_1)
print("¿",number_2,"es mayor que", number_1,"? ",result_2,"\n")

result_3 = 40 < 70 
result_4 = 70 < 40 
print("Operador 'Menor que...' (<)")
print("¿",number_1,"es menor que",number_2,"? ",result_3)
print("¿",number_2,"es menor que",number_1,"? ",result_4,"\n")

number_3 = 89
number_4 = 168
result_5 = number_3 >= number_3
result_6 = number_3 >= number_2
result_7 = number_3 >= number_4
print("Operador 'Mayor o igual que...'(>=)")
print("¿",number_3,"es mayor o igual a",number_3,"?",result_5)
print("¿",number_3,"es mayor o igual a",number_2,"?",result_6)
print("¿",number_3,"es mayor o igual a",number_4,"?",result_7,"\n")

number_5 = 15
result_8 = number_1 <= number_1
result_9 = number_1 <= number_4
result_10 = number_1 <= number_5
print("Operador 'Menor o igual que...' (<=)")
print("¿",number_1,"es menor o igual a",number_1,"?",result_8)
print("¿",number_1,"es menor o igual a",number_4,"?",result_9)
print("¿",number_1,"es menor o igual a",number_5,"?",result_10,"\n")

print("Operador 'Igual a...' (==)")
print("¿",number_5,"es igual a",number_5,"? ",number_5 == number_5)
print("¿",number_5,"es igual a",number_3,"? ",number_5 == number_3,"\n")

print("Operador 'diferente de...' (!=)")
print("¿",number_5,"es diferente de",number_5,"? ",number_5 != number_5)
print("¿",number_1,"es diferente de",number_5,"? ",number_1 != number_5,"\n")

'''
Los operadores lógicos son 
AND -> && [PYTHON -> and]
OR -> || [PYTHON -> or]
NOT 
La implementación de estos operadores, nos dara como resultado valores del tipo Booleano (TRUE y FALSE)
'''
print("Operadores Lógicos \n")
v1 = True
v2 = False

print("Tabla de verdad AND")
print(v1," && ",v2," = ",v1 and v2)
print(v1," && ",v1," = ",v1 and v1)
print(v2," && ",v2," = ",v2 and v2)
print(v2," && ",v1," = ",v2 and v1,"\n")

print("Tabla de verdad OR")
print(v1," || ",v2," = ",v1 or v2)
print(v2," || ",v1," = ",v2 or v1)
print(v1," || ",v1," = ",v1 or v1)
print(v2," || ",v2," = ",v2 or v2,"\n")

print("tabla de verdad NOT")
print("not ",v1," = ",not v1)
print("not ",v2," = ",not v2,"\n")

'''
Para conocer el tipo de variable que se está almacenando, se hace uso de la función 
"type"
'''
letter = 'GANESHA'
number_6 = 7.90

tipo1 = type(v1)
tipo2 = type(number_5)
tipo3 = type(letter)
tipo4 = type(number_6)

print("El valor: ", v1,"; Es de tipo: ",tipo1)
print("El valor: ", number_5,"; Es de tipo: ",tipo2)
print("El valor: ", letter,"; Es de tipo: ",tipo3)
print("El valor: ", number_6,"; Es de tipo: ",tipo4)
'''ligero cambio en el codigo '''
