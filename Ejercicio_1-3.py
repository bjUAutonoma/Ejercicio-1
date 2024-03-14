# Ejercicio 1-3
# Benjamin Juanillo

from os import system
system('cls')

# Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero que el teatro deja de percibir por cada una
# de las categorías. Tomar en cuenta que los niños menores de 5 años no pueden entrar al teatro y que existe un precio único en
# los asientos.

# system('cls') para limpiar terminal

# Contador de pérdidas
perdidas=0

# Precio único de entradas
v_inicial=int(input("Ingrese el valor único de entrada al teatro:\n"))

# Ciclo para menú básico
while True:

    system('cls')

    option=int(input("¿Cómo desea operar?\n\n(1) Vender Entrada\n(2) Conocer Pérdidas\n(3) Finalizar ventas\n"))

    # Menú
    if option==1:

        system('cls')

        edad=int(input(f"El valor inicial de la entrada es ${v_inicial}\n\nIngrese la edad del cliente para calcular su descuento:\n"))

        # Restricción
        if edad<5:
            input("MENORES A 5 AÑOS NO PUEDEN ENTRAR")
        # Categoría 1
        elif edad>=5 and edad<=14:
            input(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*35)/100))}")
            perdidas+=int((v_inicial*35)/100)
        # Categoría 2
        elif edad>=15 and edad<=19:
            input(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*25)/100))}")
            perdidas+=int((v_inicial*25)/100)
        # Categoría 3
        elif edad>=20 and edad<=45:
            input(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*10)/100))}")
            perdidas+=int((v_inicial*10)/100)
        # Categoría 4
        elif edad>=46 and edad<=65:
            input(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*25)/100))}")
            perdidas+=int((v_inicial*25)/100)
        # Categoría 5
        elif edad>=66:
            input(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*35)/100))}\n")
            perdidas+=int((v_inicial*35)/100)

    elif option==2:
        input(f"EL TOTAL DE PÉRDIDAS EN DESCUENTO DE ENTRADAS ES DE ${perdidas}")

    elif option==3:
        input("VENTAS FINALIZADAS")
        system('cls')
        break

    else:
        input("OPCIÓN INVÁLIDA")