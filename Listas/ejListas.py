def listaNombresEdades(cuantos):
    lista = []
    for num in range(1,cuantos+1):
        nombre = input(f"{num}. Dime el nombre: ")
        edad = int(input(f"{num}. Dime la edad: "))
        #lista.append((nombre,edad))
        lista += [(nombre,edad)]
    return lista

def insertaLetras(pal,letras,pos):
    """Funcion que inserta las letras en la palabra
        en la posicion (pos) indicada por el usuario.
    Regresa una nueva palabra con las letras en el lugar
        indicado.
    """
    return pal[:pos] + letras + pal[pos:]

def cuantasVocalesConsonantes(palabra):
    """Funcion que regresa el numero de consonantes y el
        numero de vocales en la palabra"""
    if (palabra.isalpha()):
        vocales = 0
        conso = 0
        palabra = palabra.lower()
        for letra in palabra:
            if (letra in "aeiou"):
                vocales += 1
            else:
                conso += 1
        return vocales, conso
    else:
        return "La palabra tiene que tener solamente letras"
    
    