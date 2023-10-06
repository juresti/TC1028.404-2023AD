import os

print(os.getcwd())
os.chdir("C:\\Users\\L00423103\\OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey\\Desktop")
print(os.getcwd())

def imprimeArchivo(nombre):
    with open(nombre + ".txt","r") as miArchivo:
        for linea in miArchivo:
            print(linea)

def escribeArchivo(nombre,cuantas):
    """Escribe en el archivo <nombre>.txt el numero de
        lineas (cuantas) que se le indican.
        Cada linea se la pregunta al usuario
    """
    miArchivo = open(nombre + ".txt","w")
    for num in range(1,cuantas + 1):
        linea = input(f"Dime la linea {num} del archivo: ")
        miArchivo.write(linea + "\n")
    miArchivo.close()
    
def regresaListaArchivo(nombre):
    with open(nombre + ".txt","r") as miArchivo:
        lista = miArchivo.readlines()
    return lista
