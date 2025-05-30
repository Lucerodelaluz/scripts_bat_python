import pywhatkit as kit # type: ignore
import datetime

# Paso 4.1: Definir variables
numero_destino = "+521234567890"  # Reemplaza con el número real con clave del país
mensaje = "Hola, este es un mensaje automático enviado con Python 🤖"
hora_envio = datetime.datetime.now().hour
minuto_envio = datetime.datetime.now().minute + 1  # Se enviará en el minuto siguiente

# Paso 4.2: Función para enviar el mensaje
def enviar_mensaje():
    kit.sendwhatmsg(numero_destino, mensaje, hora_envio, minuto_envio)

# Paso 5: Ejecutar la función principal
if __name__ == "__main__":
    enviar_mensaje()
