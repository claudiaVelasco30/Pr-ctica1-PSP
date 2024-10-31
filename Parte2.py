#Importamos la librería os para poder usar funciones del sistema operativo, como pipe y fork.
import os

#Función para la primera parte del ejercicio
def parte2_ej1():
    # Creamos los descriptores de archivo. fd[0] se usará para leer, y fd[1] se usará para escribir.
    fd = os.pipe()

    # Mensaje que el padre enviará al hijo
    saludoPadre = "Buenas tardes\n"

    # Creamos un nuevo proceso
    pid = os.fork()

    # Si el pid es menor que 0 ha habido un error al crear el proceso hijo
    if pid < 0:
        print("No se ha podido crear el proceso hijo.")

    # Código del proceso hijo
    elif pid == 0:
        # Leemos el mensaje del pipe
        mensajeHijo = os.read(fd[0], 80).decode("utf-8")

        # Escribimos el mensaje en el pipe en mayúsculas
        os.write(fd[1], mensajeHijo.upper().encode("utf-8"))

        # Cerramos el descriptor de lectura y escritura
        os.close(fd[0])
        os.close(fd[1])

    else:
        # Escribimos el mensaje en el pipe
        os.write(fd[1], saludoPadre.encode("utf-8"))

        # Cerramos el descriptor de escritura y esperamos a que el proceso hijo termine
        os.close(fd[1])
        os.wait()

        # Leemos el mensaje del pipe y lo imprimimos
        mensajePadre = os.read(fd[0], 80).decode("utf-8")
        print(f"El padre recibe algo del pipe: {mensajePadre}")

        # Cerramos el descriptor de lectura
        os.close(fd[0])

#Función para la segunda parte del ejercicio
def parte2_ej2():

    #Creamos los descriptores de archivo. fd[0] se usará para leer, y fd[1] se usará para escribir.
    fdArchivo = os.pipe()

    #Mensaje que el padre enviará al hijo

    #Creamos un nuevo proceso
    pid = os.fork()

    #Si el pid es menor que 0 ha habido un error al crear el proceso hijo
    if pid < 0:
        print("No se ha podido crear el proceso hijo.")

    #Código del proceso hijo
    elif pid == 0:

        contenidoFichero = os.read(fdArchivo[0], 1024).decode("utf-8")
        os.close(fdArchivo[0])

        lineas = contenidoFichero.splitlines()
        numLineas = len(lineas)
        numPalabras = sum(len(linea.split()) for linea in lineas)

        mensajeArchivoHijo = f"Número de líneas: {numLineas}, Número de palabras: {numPalabras}\n"

        os.write(fdArchivo[1], mensajeArchivoHijo.encode("utf-8"))
        os.close(fdArchivo[1])

    else:
            fichero = open("ficheroParte2.txt", "r")
            os.write(fdArchivo[1], fichero.read().encode("utf-8"))
            os.close(fdArchivo[1])

            os.wait()

            mensajeArchivoPadre = os.read(fdArchivo[0], 1024).decode("utf-8")
            print(f"El padre recibe algo del pipe: {mensajeArchivoPadre}")

            os.close(fdArchivo[0])

#Llamamos a las dos funciones
parte2_ej1()
parte2_ej2()
