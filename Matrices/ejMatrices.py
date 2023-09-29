def creaMatrizCeros(numRen,numCol):
    matriz = []
    for fila in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon.append(0)
        matriz.append(renglon)
    return matriz

def imprimeMatriz(matriz):
    for renglon in matriz:
        salida = ""
        for dato in renglon:
            salida += str(dato) + " "
        print(salida)
    
        

def tamanoMatriz(matriz):
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz:
        if (len(renglon) != numCol):
            print("Los renglones deben de tener el mismo numero de columnas")
            return -1,-1
    return numRen,numCol
