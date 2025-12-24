# Contexto global
p = 10
h = 20

# nombre_completo = nombre + apellido

nombre = "Emanuel"
apellido = "lasker"

nombre_completo = nombre + apellido

# func1()

def func1():
    apellido = "Lasker"

func1()

def saludar_2(nombre): # Comienza un nuevo contexto
    x = 15
    print(x)
    
    def saludar(nombre): # Comienza un nuevo contexto
        print(x)

        def despedir(): # Nuevo contexto que vive dentro de saludar
            print("Adiós", p)

    def despedir_2(): # Nuevo contexto que vive dentro de saludar
        print("Adiós", x)