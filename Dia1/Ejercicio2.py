cantidadTerminos = int (input("la cantidad de terminos son"))
print (cantidadTerminos)
if cantidadTerminos <= 0:
    print ("0")
else:
    sumatoria = 0
    for i in range (1,cantidadTerminos +1):
      if  (i % 2 == 0 ): 
        sumatoria -= 1/i
    else :
     sumatoria += 1/i
print("La sumatoria dio:", sumatoria)
        