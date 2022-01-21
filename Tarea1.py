"""
Tarea 1: Fizz Buzz
Nombre: Pedro Alberto Juan Velazquez

Indicaciones:

Escribe un programa en Python que dados dos números de inicio y fin de una secuencia, recorra la secuencia y escriba el número o la cadena "Fizz", "Buzz" correspondiente.
"""

# Inicio del programa
a = 0
lista_resultados = []
lista_numero = []

# Solicitud de datos:
print( "Ingrese un rango comprendido por dos numeros separados por un espacio" )
numeros = input()
lista_numero = numeros.split()

#Adaptando la informacion dependiendo que numero es mas grande
if lista_numero[0]<lista_numero[1]: 
    numero1 = lista_numero[0]
    numero2 = lista_numero[1]
    valoracion = True
elif lista_numero[0]>lista_numero[1]: 
    numero1 = lista_numero[1]
    numero2 = lista_numero[0]
    valoracion = True
else: 
    print( "Los numeros son iguales, favor de introducir otros." )
    valoracion = False 

rango1 = int( numero1 )
rango2 = int( numero2 )

# inicio del FIZZ BUZZ
if valoracion == True:
    for i in range( rango1,rango2 ):
        divisor3 = i % 3
        divisor5 = i % 5
        if i == 0:
            lista_resultados.append( i )
        elif (divisor3 == 0) and (divisor5 == 0):
          lista_resultados.append( "FIZZ BUZZ" )
        elif divisor3 == 0:
            lista_resultados.append( "FIZZ" )
        elif divisor5 == 0:
            lista_resultados.append( "BUZZ" )
        else:
            lista_resultados.append( i )  

# Impresion de FIZZ BUZZ
if valoracion == True: 
    for i in lista_resultados:
        print( lista_resultados[a], end=" " )
        a = a+1


print( "\nGracias por usar el programa" )
# Fin del programa
