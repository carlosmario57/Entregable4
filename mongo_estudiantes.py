import pymongo

# Conectarse al servidor local de MongoDB
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
db = cliente["mi_basedatos"]
coleccion = db["Estudiantes"]

# Insertar documentos
estudiantes = [
    {"nombre": "Juan", "edad": 20, "ciudad": "Bogotá"},
    {"nombre": "Ana", "edad": 22, "ciudad": "Medellín"},
    {"nombre": "Luis", "edad": 19, "ciudad": "Cali"}
]

coleccion.insert_many(estudiantes)

# Consultar todos los documentos
print("=== TODOS LOS ESTUDIANTES ===")
for estudiante in coleccion.find():
    print(estudiante)

# Filtrar por ciudad
print("\n=== ESTUDIANTES DE MEDELLÍN ===")
for estudiante in coleccion.find({"ciudad": "Medellín"}):
    print(estudiante)

# Filtrar mayores de 20 años
print("\n=== ESTUDIANTES MAYORES DE 20 ===")
for estudiante in coleccion.find({"edad": {"$gt": 20}}):
    print(estudiante)
