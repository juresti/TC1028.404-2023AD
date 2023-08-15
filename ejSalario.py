salario = float(input("Dime tu salario: "))
ISR = salario * 0.2136
real = salario - ISR
print(f"Toman de tu salario por ISR: ${ISR}")
print(f"Te dejaron para ti: ${real}")
