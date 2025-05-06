# Determinar si un número es par o impar
numero = int(input("Escribe un número: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

# Bucle for: cuadrados
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(f"{n} al cuadrado es {n**2}")

# Bucle while: contraseña
clave = ""
while clave != "python123":
    clave = input("Introduce la contraseña correcta: ")
print("¡Acceso concedido!")
