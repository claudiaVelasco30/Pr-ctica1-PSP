import subprocess #Librería para ejecutar programas y comandos del sistema operativo
import win32clipboard #Librería para interactuar con el portapapeles de Windows
import time #Librería para medir el tiempo de las verificaciones

#Creamos un proceso utilizando subprocess
p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Creamos la lista de comandos que se enviarán al programa FTP
comandos = [
        b"verbose\n",
        b"open test.rebex.net\n",
        b"demo\n",
        b"password\n",
        b"get readme.txt\n",
        b"bye\n"
    ]

#Iteramos sobre cada comando en la lista y lo enviamos al proceso FTP
for cmd in comandos:
    p1.stdin.write(cmd)

#Esperamos hasta 5 segundos a que el proceso termine y capturamos la salida
respuesta = p1.communicate(timeout=5)[0]
#Imprimimos la respuesta del servidor FTP, decodificándola con la codificación 'cp850'
print(respuesta.decode("cp850", "ignore"))

#Enviamos los datos del archivo al portapapeles
try:
    win32clipboard.OpenClipboard()  #Abre el portapapeles para manipularlo
    win32clipboard.EmptyClipboard()  #Limpia el contenido actual del portapapeles
    win32clipboard.SetClipboardText(open("readme.txt", "r").read())  #Establece el contenido del fichero "readme.txt" en el portapapeles
    win32clipboard.CloseClipboard()  #Cierra el portapapeles para liberar el acceso
    print("Contenido del archivo copiado al portapapeles.\n")
except FileNotFoundError:
    print("El archivo 'readme.txt' no se encontró") #Excepción si no encuentra el archivo

#Obtener datos del portapapeles
win32clipboard.OpenClipboard()  #Abre el portapapeles para leer su contenido
datosIniciales = win32clipboard.GetClipboardData()  #Obtiene los datos actuales del portapapeles.
win32clipboard.CloseClipboard()  #Cierra el portapapeles para liberar el acceso

print("Verificando si el contenido del portapapeles ha cambiado:")
#Bucle para comprobar el contenido del portapapeles
for _ in range (5):
    time.sleep(5) #Verificamos cada 5 segundos

    #Obtenemos de nuevo los datos del portapapeles
    win32clipboard.OpenClipboard()
    datosActuales = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    #Comprobamos si los nuevos datos son iguales que los anteriores
    if(datosIniciales != datosActuales):
        print("-El contenido del portapapeles ha cambiado")
        datosIniciales = datosActuales
    else:
        print("-El contenido del portapapeles no ha cambiado")
