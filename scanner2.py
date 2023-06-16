from TipoToken import * #importaciones de las classes
from Token import *

sig=('(',')','{','}',"'",'.',';','-','+','*','/','!','!=','=','==','<','<=','>','>=')
alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
digitos=('0','1','2','3','4','5','6','7','8','9')

cadena=input()
cadena+=" "
a=0
estado=0  #estado del automata estado cero como inicial
i_lexema=0     #inicio del lexema para llevar un contro de donde empieza
f_lexema=0     #y donde termina
flotante=True  #un identificador para saber cuando sea flotante el numero
cerrar=False



def signos():
    global i_lexema
    global estado
    global f_lexema
    global a

    if estado==0:
        if cadena[a]=='<':
            estado=1
            f_lexema+=1
            a+=1
        elif cadena[a]=="=":
            estado=5
            f_lexema+=1
            a+=1
        elif cadena[a]=='>':
            estado=6
            f_lexema+=1
            a+=1
        elif cadena[a] in sig:
            estado=4
            f_lexema+=1
            a+=1
        else:
            estado=9
            palabra()
    elif estado==1:
        if cadena[a] =='=':
            estado=2
            f_lexema+=1
            a+=1
        elif cadena[a] == '>':
            estado=3
            f_lexema+=1
            a+=1
        else:
            estado=4
    elif estado==2:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
        a+=1
    elif estado==3:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
        a+=1
    elif estado==4:#estado final con asterisco
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
        
    elif estado==5:
        if cadena[a]=="=":
            estado=5.5
            f_lexema+=1
            a+=1
        else:
            buscar=TipoToken()
            buscar.esta(cadena[i_lexema:f_lexema],flotante)
            i_lexema=f_lexema
            estado=0
            a+=1
    elif estado==5.5:#estadado final 
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
        a+=1
    elif estado==6:
        if cadena[a] =='=':
            estado=7
            f_lexema+=1
            a+=1
        else:
            estado=8
    elif estado==7:#estadado final 
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
        a+=1
    elif estado==8:#estado final 
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0

def palabra():
    global i_lexema
    global estado
    global f_lexema
    global a
    if estado==9:
        if cadena[a] in alfabeto:
            estado=10
            f_lexema+=1
            a+=1
        else:
            estado=12
            numeros()
    elif estado==10:
        if cadena[a] in alfabeto or cadena[a] in digitos:
            estado=10
            f_lexema+=1
            a+=1
        else:
            estado=11
    elif estado==11:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0

def numeros():
    global i_lexema
    global estado
    global f_lexema
    global a
    global flotante

    if estado==12:
        if cadena[a] in digitos:
            estado=13
            f_lexema+=1
            a+=1    
        else:
            estado=22
            espacios()    
    elif estado==13:
        if cadena[a] in digitos:
            estado=13
            f_lexema+=1
            a+=1 
        elif cadena[a] ==".":
            estado=14
            f_lexema+=1
            flotante=False
            a+=1 
        elif cadena[a] =="E":
            estado=16
            f_lexema+=1
            flotante=True
            a+=1 
        else:
            estado=20
            if cadena[a] ==" ":
                numeros()
    elif estado==14:
        if cadena[a] in digitos:
            estado=15
            f_lexema+=1
            a+=1     
    elif estado==15:
        if cadena[a] in digitos:
            estado=15
            f_lexema+=1
            a+=1 
        elif cadena[a] =="E":
            estado=16
            f_lexema+=1
            a+=1 
        else:
            estado=21
            if cadena[a] ==" ":
                numeros()
    elif estado==16:
        if cadena[a] in digitos:
            estado=18
            f_lexema+=1
            a+=1 
        elif cadena[a] =="+" or cadena[a]=="-":
            estado=17  
            f_lexema+=1
            a+=1   
    elif estado==17:
        if cadena[a] in digitos:
            estado=18
            f_lexema+=1
            a+=1 
    elif estado==18:
        if cadena[a] in digitos:
            estado=18
            f_lexema+=1
            a+=1 
            
        else:
            estado=19
            if cadena[a] ==" ":
                numeros()
    elif estado==19:#estado final con *
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
        
    elif estado==20:#estado final con *
        flotante=True
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        print(cadena[i_lexema:f_lexema],"hola")
        i_lexema=f_lexema
        estado=0
        
    elif estado==21:#estado final con *
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0

def espacios():
    global i_lexema
    global estado
    global f_lexema
    global a
    if estado==22:
        if cadena[a]==" ":
            estado=23
            f_lexema+=1
            a+=1
    elif estado==23:
        if cadena[a]==" ":
            estado=23
            f_lexema+=1
            a+=1
        else:
            estado=24
    elif estado==24:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0


while(cerrar!=True):
    if a!=len(cadena):
        if estado==0 or estado==1 or estado==2 or estado==3 or estado==4 or estado==5 or estado==5.5 or estado==6 or estado==7 or estado==8:
            signos()
        elif estado==9 or estado==10 or estado==11: #estados para llamar a las funciones
            palabra()
        elif estado==12 or estado==13 or estado==14 or estado==15 or estado==16 or estado==18 or estado==17 or estado==19 or estado==20 or estado==21: #estados para llamar a las funciones
            numeros() 
        #inicio del automata para detectar espacios en blanco
        elif estado==22 or estado==23 or estado==24:
            espacios()
    else:
        print(Token.tokens) #impresion de tokens
        seleccion=input("continuar: ")
        if (seleccion=="1"):
            print("va")
            a=0
            cadena=""
            cadena=input()
            print(cadena)
        else:
            print("cerrar")
            cerrar=True
