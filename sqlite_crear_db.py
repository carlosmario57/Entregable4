import sqlite3

# Crear o conectar a la base de datos local SQLite
conexion = sqlite3.connect("usuarios.db")  # Aquí se creará el archivo .db

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla llamada 'usuarios'
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL
)
''')

# Insertar un par de usuarios de ejemplo
cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", ("Carlos Mario", "carlos@example.com"))
cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", ("Ana Torres", "ana@example.com"))

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos y tabla creada con éxito.")
