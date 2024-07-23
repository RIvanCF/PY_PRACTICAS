'''El ingreso de valores de cualquier tipo es esencial en la iplementacion de programas cuyos valores sean 
variables y de libre definición, basicamente es ingresar un dato desde el teclado 
'''
dato_in = input("Ingresa un dato: ") #Ingreso de datos desde el teclado, EL VALOR INGRESADO RETORNARA CON UN VALOR STR
print("El valor que ingresaste es: ", dato_in)#Impresión del dato

'''Para que el dato ingresado tenga las propiedades deseadas, se debe definir el tipo de dato correspondiente'''
dato_input = input("Ingresa un dato del tipo entero: ") #Aqui el dato a ingresar sera del tipo string (str)
dato_input = int(dato_input)#El dato generado sera del tipo entero (int)
print("Dato ingresado: ", dato_input)
print("Es un valor del tipo: ",type(dato_input))