def cuantasVocales(pal):
    """ Funcion que regresa 5 parametros.
        Primer parametro indica cuantas a tiene la palabra.
        Segundo parametro cuantas e.
        Tercer parametro cuantas i.
        Cuarto cuantas o y quinto cuantas u"""
    copia = pal.lower()
    contA = 0
    contE = 0
    contI = 0
    contO = 0
    contU = 0
    for letra in copia:
        if (letra == "a"):
            contA += 1
        elif (letra == "e"):
            contE += 1
        elif (letra == "i"):
            contI += 1
        elif (letra == "o"):
            contO += 1
        elif (letra == "u"):
            contU += 1
    return contA,contE,contI,contO,contU
    
def miSwap(pal):
    """Funcion que recibe una palabra y regresa otra
        en donde las minusculas fueron cambiadas por
        mayusculas y viceverza"""
    nueva = ""
    for letra in pal:
        if (letra.isspace() or letra.isdigit()):
            nueva += letra
        elif (letra.islower()):
            nueva += letra.upper()
        elif (letra.isupper()):
            nueva += letra.lower()
        elif (not(letra.isalnum())):
            nueva += letra
        else:
            print(f"Algo raro en el string: {letra}")
    return nueva


def listaPersonas(cuantas):
    lista = []
    for num in range(1,cuantas + 1):
        nombre = input(f"Dime el nombre de la persona {num}: ")
        lista += [nombre] #lista.append(nombre)
    return lista
