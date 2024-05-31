def factorial (n):
    """Funcion que calcula el factorial de un numero entero positivo.
    Parámetros 
    n: es un numero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1 
    for i in range (n):
        tmp *= i+1
    return tmp 
print(factorial(4))
print(factorial(20))