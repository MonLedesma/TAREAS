#Mónica Ledesma 
#Tarea: Ejercicio Fizzbuzz

#Valores iniciales
ini= 5
fin=15
tres="fizz" 
cinco="Buzz"

#Palabras que sustituyen si es divisible entre 3 o 5 por fizz o buzz, respectivamente
for i in range(ini,fin):
  if i%3 == 0 and i%5 == 0 : 
    print(tres+" "+cinco)
  elif  i%3 == 0:
        print(tres)
  elif  i%5 == 0:
        print(cinco)
  else :
    print(i)
