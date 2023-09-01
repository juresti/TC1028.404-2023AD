def fibonacci(k):
    if (k <= 0):
        return "Error. Debe de ser un numero mayor a 0."
    else:
        if (k == 1) or (k == 2):
            return f"f({k}) = 1"
        else:
            veces = k - 2
            pen = 1
            ult = 1
            while (veces > 0):
                nuevo = ult + pen
                pen = ult
                ult = nuevo
                veces -= 1
            return f"f({k}) = {nuevo}"

def fibonacciFor(k):
    if (k <= 0):
        return "Error. Debe de ser un numero mayor a 0."
    else:
        if (k == 1) or (k == 2):
            return f"f({k}) = 1"
        else:
            veces = k - 2
            ult = 1
            pen = 1
            for cont in range(veces):
                nuevo = ult + pen
                pen = ult
                ult = nuevo
            return f"f({k}) = {nuevo}"
        
def otra(var1, var2, var3):
    return var1 + var3 / var2

def diHola():
    print("Hola")

def main():
    opcion = int(input("Cual ejercicio quieres correr? "))
    if (opcion == 1):
        #Ejercicio 1
        print("Ejercicio 1")
        diHola()
    elif (opcion == 2):    
        #Ejercicio 2
        print("Ejercicio 2")
        print(otra(3,4,5))
    elif (opcion == 3):    
        #Ejercicio 3
        print("Ejercicio 3")
        k = int(input("Dime el valor de k: "))
        print(fibonacci(k))
    elif (opcion == 4):    
        #Ejercicio 4
        print("Ejercicio 4")
        print(fibonacciFor(6))
    else:
        print("Ese ejercicio no existe")
        
