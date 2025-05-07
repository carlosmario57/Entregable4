import sqlite3

# Conectarse a la ba de datos creada anteriormente
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Consultar todos los usuarios
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# Mostrar los resultados
print("=== LISTA DE USUARIOS ===")
for usuario in usuarios:
    print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}")

conexion.close()
