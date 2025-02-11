import pandas as pd  # Importamos pandas para la limpieza de datos

# Pedimos al usuario el nombre o ruta del archivo
try:
    datos = input("Introduzca el nombre del archivo o la dirección del archivo: ").strip()  
    if not datos.endswith(".csv"):  
        raise ValueError("El archivo debe tener la extensión .csv")

    df = pd.read_csv(datos)  # Intentamos leer el archivo CSV

except FileNotFoundError:
    print("❌ Error: El archivo no existe. Verifique el nombre o la ruta.")
    exit()
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    exit()

# Mostramos los datos antes de limpiarlos
print("\n📊 Datos antes de limpiarlos:")
print(df.info())  

# Mostramos la cantidad de valores nulos en cada columna
print("\n🔍 Cantidad de valores nulos por columna:")
print(df.isna().sum())  

# Mostramos la cantidad de registros duplicados
print("\n📌 Cantidad de registros duplicados:", df.duplicated().sum())

# Eliminamos los duplicados
df = df.drop_duplicates()
print("\n✅ Registros duplicados eliminados.")

# Opciones para manejar valores nulos
opcion = input("\n¿Qué desea hacer con los valores nulos?\n1: Eliminar filas con valores nulos\n2: Rellenar con el promedio\n👉 Opción: ").strip()

if opcion == "1":
    df = df.dropna()
    print("\n✅ Valores nulos eliminados.")
elif opcion == "2":
    df = df.fillna(df.mean(numeric_only=True))  
    print("\n✅ Valores nulos rellenados con el promedio.")
else:
    print("\n⚠️ Opción no válida. No se realizaron cambios en los valores nulos.")

# Guardamos el archivo limpio
archivo = "archivo_limpio.csv"
df.to_csv(archivo, index=False)
print(f"\n✅ Los datos limpios se guardaron con el nombre: {archivo}")
