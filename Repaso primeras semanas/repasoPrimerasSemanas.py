def cuenta4en4(inicio,fin):
    """Funcion que cuenta de 4 en 4 dado un rango"""
    for num in range(inicio,fin+1,4):
        print(num)
        
def cuentaAtrasDiv7(inicio,fin):
    """Funcion que recibe un rango y cuenta hacia atras
        indicando cuales son los divibles entre 7 y
        regresa la cantidad de ellos"""
    cont = 0
    for num in range(fin,inicio-1,-1):
        res = num % 7
        if (res == 0):
            print(num)
            cont += 1
    return cont
            
def preguntaOpcion():
    opcion = input("Si o no? ")
    while opcion.lower() != "no":
        opcion = input("Si o no? ")
    print("ya dijiste que no")

