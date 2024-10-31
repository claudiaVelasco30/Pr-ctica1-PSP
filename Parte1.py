#Importamos la librería psutil para gestionar procesos del sistema operativo.
import psutil

#Pedimos por pantalla los nombres de los procesos separados por comas
nombresProcesos = input("Introduce los nombres de los procesos de los que quieras obtener información separados por comas: ")

#Creamos una lista de nombres de procesos, eliminando espacios y convirtiéndolos a minúsculas
listaNombres = [nombre.strip().lower() for nombre in nombresProcesos.split(",")]

#Creamos un diccionario para saber si los procesos están o no activos
procesosActivos = {nombre: False for nombre in listaNombres}

#Pedimos al usuario el nombre del proceso para finalizar
finalizarProceso = input("Introduce el proceso que quieras finalizar: ").lower()
procesoFinalizado = False #Booleano para saber si se ha finalizado el proceso

try:
    print("\nProcesos que se están ejecutando:")

    #Iteramos sobre todos los procesos activos en el sistema
    for proc in psutil.process_iter():

        #Buscamos el proceso para finalizar
        if proc.name().lower() == finalizarProceso:
            #Utilizamos el metodo .terminate() para finalizar el proceso.
            proc.terminate()
            procesoFinalizado = True

        for nombre in listaNombres:
            #Comprobamos si el nombre del proceso coincide con alguno de la lista del usuario
            if nombre in proc.name().lower():
                procesosActivos[nombre] = True
                #Imprimimos el nombre del proceso, su PID y el porcentaje que ocupa en memoria
                print(f"Nombre: {proc.name()}, PID: {proc.pid}, Memoria: {proc.memory_percent()} %")

#Excepción si el proceso ha terminado antes de que podamos interactuar con él o si no tengamos permisos.
except(psutil.NoSuchProcess, psutil.AccessDenied):
    print("Error")

print("\nProcesos que no se están ejecutando:")
#Recorremos el diccionario para imprimir los procesos que no se encontraron
for nombre, encontrado in procesosActivos.items():
    if encontrado == False:
        print(f"Nombre: {nombre}")

#Imprimimos si el proceso fue o no finalizado
if procesoFinalizado == True:
    print(f"\nEl proceso {finalizarProceso} se ha finalizado correctamente")
else :
    print(f"\nEl proceso {finalizarProceso} no se pudo finalizar")