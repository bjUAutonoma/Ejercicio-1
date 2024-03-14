# Ejercicio 2-2
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

while True:

    option=int(input("¿Qué desea hacer?\n\n(1) Calcular pie\n(2) Calcular cuota mensual\n(3) Finalizar\n"))
    system('cls')

    if option==1 or option ==2:

        vivienda=int(input("\nIngrese el valor de la vivienda:\n"))
        salario=int(input("\nIngrese el salario del comprador:\n"))
        system('cls')

        if option==1:
            input(f"Con un salario de ${salario} el pie es de:\n{(vivienda*0.15) if salario>=80000 else vivienda*0.3}")
        elif option==2:
            input(f"Con un salario de ${salario} los pagos mensuales son de: ${(vivienda-(vivienda*0.15))/(10*12) if salario>=80000 else (vivienda-(vivienda*0.3))/(7*12)}")
        
    elif option==3:
        input("HASTA LUEGO")
        break
    
    else:
        input("OPCIÓN INVÁLIDA")
    
    system('cls')