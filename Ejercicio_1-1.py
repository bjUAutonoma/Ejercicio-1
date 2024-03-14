# Ejercicio 1-1
# Benjamin Juanillo

from os import system

# Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero que el teatro deja de percibir por cada una
# de las categorías. Tomar en cuenta que los niños menores de 5 años no pueden entrar al teatro y que existe un precio único en
# los asientos.

perdidas=0

v_inicial=int(input("Ingrese el valor único de entrada al teatro:\n"))
system('cls')

edad=int(input(f"El valor inicial de la entrada es ${v_inicial}\n\nIngrese la edad del cliente para calcular su descuento:\n"))
system('cls')

# Restricción
if edad<5:
    print("MENORES A 5 AÑOS NO PUEDEN ENTRAR")
# Categoría 1
if edad>=5 and edad<=14:
    print(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*35)/100))}")
    perdidas+=int((v_inicial*35)/100)
# Categoría 2
if edad>=15 and edad<=19:
    print(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*25)/100))}")
    perdidas+=int((v_inicial*25)/100)
# Categoría 3
if edad>=20 and edad<=45:
    print(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*10)/100))}")
    perdidas+=int((v_inicial*10)/100)
# Categoría 4
if edad>=46 and edad<=65:
    print(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*25)/100))}")
    perdidas+=int((v_inicial*25)/100)
# Categoría 5
if edad>=66:
    print(f"EL VALOR DE SU ENTRADA ES ${int(v_inicial-((v_inicial*35)/100))}")
    perdidas+=int((v_inicial*35)/100)

input("\nPRESIONE ENTER PARA CONTINUAR")
system('cls')

print(f"EL TOTAL DE PÉRDIDAS EN DESCUENTO DE ENTRADAS ES DE ${perdidas}")
input()
system('cls')