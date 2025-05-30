import os

#Definir la ruta
ruta_carpeta = "C:/Users/itzel/Documents/Escuela/9no Cuatrimestre/Automatización de Infrestructura digital I/Unidad I/Actividad 5/Renombrar archivos"

# Obtener la lista de archivos
archivos = os.listdir(ruta_carpeta)

# Renombrar los archivos
def renombrar_archivos():
    for i, nombre_original in enumerate(archivos, start=1):
        extension = os.path.splitext(nombre_original)[1]  # obtener la extensión (.txt, .jpg, etc.)
        nuevo_nombre = f"archivo_{i}{extension}"
        ruta_original = os.path.join(ruta_carpeta, nombre_original)
        nueva_ruta = os.path.join(ruta_carpeta, nuevo_nombre)
        
        os.rename(ruta_original, nueva_ruta)
        print(f"{nombre_original} -> {nuevo_nombre}")

# Ejecutar el script
if __name__ == "__main__":
    renombrar_archivos()
