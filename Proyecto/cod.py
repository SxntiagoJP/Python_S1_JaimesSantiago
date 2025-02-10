import json
from menus import *
def abrirJSON(Ruta):
    dicFinal={}
    with open(f'./{Ruta}.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal
zzz={}
m()
def guardarJSON(dic,Ruta):
    with open(f"./{Ruta}.json",'w') as outFile:
        json.dump(dic,outFile)


lie=True
while lie==True:
    print("Seleccione el tipo de perfil")
    print("1 para campers || 2 para trainers || 3 para coordinador")
    seleccion=int(input(": "))
    if seleccion==1:
        menu_campers_registro ()
        ruta="campers"

        opc = int(input(":"))

        if opc == 1:
            menu_campers
        else: 
            print ("Espere su registro")
        zzz=abrirJSON(ruta)


        lie=False 
    elif seleccion==2:
        menu_trainers()
        ruta="trainers"
        zzz=abrirJSON(ruta)
        lie = False
    elif seleccion==3:
        menu_coordinador()
        ruta="coordinador"
        zzz=abrirJSON(ruta)
        lie = False
    