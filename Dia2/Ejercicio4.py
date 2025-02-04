grande = 0
pequeno = 0
for i in range (1,11):
 numerito = int (input("regresa el numero: "))
 if grande == 0 or pequeno == 0:
  grande = numerito
  pequeno = numerito
 else:
  if numerito > grande:
   grande = numerito 
   if numerito < pequeno:
    pequeno = numerito

    print ("grande", grande)
    print("pequeno", pequeno)

    ##Desarrollado por Santiago Jaimes Perez / T.I 1095307854
