'''Implementar multiples variables en pocas lineas de codigo'''
#Declaramos ,multiples variables
nombre = 'Jason'
apellido = 'Todd'
alias = 'Capucha Roja'
'''Impresióm de las cadenas declaradas por variable'''
print(nombre)
print(apellido)
print(alias)
'''Existe una forma eficiente de declarar variables sin ocupar multiples lineas de codigo. 
para este ejemplo solo se usará una sola linea'''
nombre,apellido,alias = 'Jason','Tood','Capucha Roja' #De esta forma, los valores se van a almacenar respecto a su posición 
'''Lo mismo se puede implementar para la impresion de estas variables'''
print(nombre,"\n",apellido,"\n",alias)
#De esta manera solo ocupamos dos lineas de codigo a comparación de la forma intuitiva de programación, que son 6 lineas 