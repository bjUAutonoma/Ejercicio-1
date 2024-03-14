# Ejercicio 2-1
# Benjamin Juanillo

from os import system
system('cls')

# Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones:
# Si los ingresos del comprador son de $80.000 o más el pie será del 15% del costo de la casa y el resto se
# distribuirá en pagos mensuales, a pagar en 10 años.
# Si los ingresos del comprador son menos de $80.000 el pie será del 30% del costo de la casa y el resto se
# distribuirá en pagos mensuales, a pagar en 7 años.
# La empresa quiere obtener cuánto debe pagar un comprador por concepto de pie y cuánto por cada pago mensual.

input("BIENVENIDO/A AL GESTOR DE PAGOS MENSUALES Y PIE\n\nPresione ENTER para comenzar")
system('cls')

vivienda=int(input("Ingrese el valor de la vivienda:\n"))
salario=int(input("\nIngrese el salario del comprador:\n"))
system('cls')

print(f"CON UN SALARIO DE ${salario} LOS PAGOS RESULTAN:\n")
if salario>=80000:
    print(f"    PIE: ${(vivienda*0.15) }\n\
    MENSUAL: ${(vivienda-(vivienda*0.15))/(10*12)}")
if salario<80000:
    print(f"    PIE: ${vivienda*0.3}\n\
    MENSUAL: ${(vivienda-(vivienda*0.3))/(7*12)}")

input("\nPresione ENTER para finalizar")