
import subprocess #Librería para ejecutar programas y comandos del sistema operativo
import asyncio #Librería para trabajar con programación asíncrona en Python
import time #Librería para medir el tiempo

#Función para ejecutar Notepad de forma síncrona
def notepadSincrona():
    try:
        print("Ejecutando Notepad de manera síncrona")
        #Guardamos el tiempo actual al iniciar Notepad
        tiempoInicial = time.time()

        #Utilizamos subprocess.run para ejecutar 'Notepad.exe'. Esto es una llamada síncrona, por lo que bloquea el programa hasta que Notepad se cierre
        subprocess.run(['Notepad.exe', ])

        #Guardamos el tiempo después de cerrar Notepad
        tiempoFinal = time.time()
        print(f"Tiempo de ejecución síncrona: {tiempoFinal - tiempoInicial} segundos")
    except subprocess.CalledProcessError:
        #Capturamos las excepciones si la ejecución de Notepad falla
        print("Error al ejecutar Notepad de manera síncrona")


# Función asíncrona para ejecutar Notepad de forma asíncrona
async def notepadAsincrona():
    try:
        print("Ejecutando Notepad de manera asíncrona")
        #Guardamos el tiempo actual al iniciar Notepad
        tiempoInicial = time.time()

        #Iniciamos Notepad de forma asíncrona, el programa principal continúa ejecutándose sin esperar a que Notepad se cierre
        Notepad = await asyncio.create_subprocess_exec('Notepad.exe')
        await Notepad.wait()

        #Guardamos el tiempo después de cerrar Notepad
        tiempoFinal = time.time()
        print(f"Tiempo de ejecución síncrona: {tiempoFinal - tiempoInicial} segundos")
    except subprocess.CalledProcessError:
        #Capturamos las excepciones
        print("Error al ejecutar Notepad de manera asíncrona")

#Función principal para seleccionar el modo de ejecución
def main():
    print("Selecciona el modo de ejecución para el Bloc de notas:")
    print("1. Ejecución síncrona")
    print("2. Ejecución asíncrona")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        notepadSincrona()
    elif opcion == '2':
        #Ejecutamos el modo asíncrono usando asyncio
        asyncio.run(notepadAsincrona())
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()