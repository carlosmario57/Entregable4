# 3.1 Lista de estudiantes [cite: 250, 282]
estudiantes = ["Juan", "Ana", "Luis"]  # Lista de nombres
for estudiante in estudiantes:  # Itera sobre la lista
    print(f"Estudiante: {estudiante}")  # Imprime cada nombre

# 3.2 Diccionario de contactos [cite: 251, 283]
contactos = {  # Diccionario de información
    "Juan": "juan@example.com",
    "Ana": "ana@example.com"
}
for clave, valor in contactos.items():  # Itera sobre el diccionario
    print(f"Nombre: {clave}, Correo: {valor}")  # Imprime clave y valor

# 3.3 Agregar/Actualizar lista/diccionario [cite: 252, 284]
nuevo_estudiante = input("Introduce el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)  # Agrega a la lista
print("Lista actualizada de estudiantes:", estudiantes)

nuevo_contacto = input("Introduce un nombre para actualizar/agregar: ")
nuevo_correo = input("Introduce el correo de este contacto: ")
contactos[nuevo_contacto] = nuevo_correo  # Agrega/actualiza el diccionario
print("Contactos actualizados:", contactos)