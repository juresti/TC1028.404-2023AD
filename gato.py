def crearMatriz(numRen,numCol,inicializador):
    matriz = []
    for _ in range(numRen):
        renglon = [inicializador] * numCol
        matriz.append(renglon)
    return matriz

def imprimeMatriz(matriz):
    cont = 0
    print("  0 1 2")
    for renglon in matriz:
        salida = f"{cont} "
        for dato in renglon:
            salida += dato + " "
        print(salida)
        cont += 1

def preguntaUsuario(matriz):
    print("\nEscoge donde vas a tirar")
    imprimeMatriz(matriz)
    ren = int(input("En que renglon quieres tirar? "))
    col = int(input("En que columna quieres tirar? "))
    return ren,col

def asignaTiro(ren,col,ficha,tablero):
    tablero[ren][col] = ficha
    return tablero

def gato():
    tablero = crearMatriz(3,3,".")
    print("Bienvenido al juego de gato")
    imprimeMatriz(tablero)
    
    for num in range(9):
        nRen,nCol = preguntaUsuario(tablero)
        if (num % 2 == 0):
            tablero = asignaTiro(nRen,nCol,"X",tablero)
        else:
            tablero = asignaTiro(nRen,nCol,"O",tablero)
    
gato()
