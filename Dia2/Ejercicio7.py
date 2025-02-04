##Numeros amiguitos 

##Para ingresar  un valor entero "int"
n1 = int (input("ingresa n1: "))
print("") ##Espacio estetica
n2 = int (input("ingresa n2: "))

#el valor incial sea cero
suma1 = 0.0
suma2 = 0.0

if n1 == 1:
    suma1=1
else:
    for i in range (1,n1-1):
        if n1%i==0:
            suma1=suma1+i
            
print("")
if n1 == 1:
    suma1=1
else:
    for i in range (1,n2-1):
        if n2%i==0:
            suma2=suma2+i

if suma1==n2 and suma2==n1:
    print("los numeros son parceritos")
else:
    print("los numeros no son parceritos")