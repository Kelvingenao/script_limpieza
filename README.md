# 📌 Script de Limpieza de Datos

Este script en Python permite limpiar datasets en formato CSV con solo unos pocos clics. Automatiza la detección y eliminación de valores duplicados, además de ofrecer opciones para manejar valores nulos.

## 🚀 Características
- 📊 Muestra información del dataset antes de limpiarlo.
- 🔍 Detecta y elimina registros duplicados.
- ❓ Permite al usuario elegir cómo tratar los valores nulos:
  - Eliminar filas con valores nulos.
  - Rellenar valores numéricos con el promedio de la columna.
- 💾 Guarda el dataset limpio en un nuevo archivo CSV.

## 📂 Dataset de Prueba
En la carpeta `dataset`, encontrarás un archivo CSV con valores duplicados y nulos. Puedes usarlo para probar el script y verificar su funcionamiento.

## 🛠️ Requisitos
- Python 3.x
- Pandas (`pip install pandas`)

## 📌 Uso
1. Descarga o clona este repositorio.
2. Asegúrate de tener instalado Python y Pandas.
3. Ejecuta el script con:
   ```bash
   python script_limpieza.py
   ```
4. Introduce la ruta o el nombre del archivo CSV cuando se te solicite.
5. Sigue las instrucciones en pantalla para limpiar los datos.
6. El archivo limpio se guardará como `archivo_limpio.csv`.

## 📝 Notas
- El script solo funciona con archivos `.csv`.
- Si ingresas un archivo inexistente, se mostrará un mensaje de error.

¡Esperamos que este script te ayude a limpiar tus datos de manera rápida y sencilla! 🚀

