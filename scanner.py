
from TipoToken import * #importaciones de las classes
from Token import *

sig=('(',')','{','}',"'",'.',';','-','+','*','/','!','!=','=','==','<','<=','>','>=')
alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
digitos=('0','1','2','3','4','5','6','7','8','9')

cadena=""

with open('archivo.txt', 'r') as archivo:  #Esta parte lee el archivo txt y lo guarda en la variable cadena para su uso posterior
    cadena = archivo.read()


estado=0  #estado del automata estado cero como inicial
i_lexema=0     #inicio del lexema para llevar un contro de donde empieza
f_lexema=0     #y donde termina
flotante=True  #un identificador para saber cuando sea flotante el numero

def palabra(i): #funcion donde se guardan los estados del automata para las palabras 
            global estado
            global f_lexema
            global i_lexema
            global flotante
            if estado==9:
                if i in alfabeto:
                    estado=10
                    f_lexema+=1
                else:
                    estado=12
                    numeros(i)
            elif estado==10:
                if i in alfabeto or i in digitos:
                    estado=10
                    f_lexema+=1
                else:
                    estado=11
                    palabra(i)
            elif estado==11:#estado final
                buscar=TipoToken()
                buscar.esta(cadena[i_lexema:f_lexema],flotante)
                i_lexema=f_lexema
                estado=0
def numeros(i): #funcion donde se guardan los estados del automata de numeros
    global estado
    global f_lexema
    global i_lexema
    global flotante
    if estado==12:
        if i in digitos:
            estado=13
            f_lexema+=1
            
            
        else:
            estado=22    
    elif estado==13:
        if i in digitos:
            estado=13
            f_lexema+=1
        elif i ==".":
            estado=14
            f_lexema+=1
            flotante=False
        elif i =="E":
            estado=16
            f_lexema+=1
            flotante=True
        else:
            estado=20
            if i ==" ":
                numeros(i)
    elif estado==14:
        if i in digitos:
            estado=15
            f_lexema+=1    
    elif estado==15:
        if i in digitos:
            estado=15
            f_lexema+=1
        elif i =="E":
            estado=16
            f_lexema+=1
        else:
            estado=21
            if i ==" ":
                numeros(i)
    elif estado==16:
        if i in digitos:
            estado=18
            f_lexema+=1
        elif i =="+" or i=="-":
            estado=17  
            f_lexema+=1  
    elif estado==17:
        if i in digitos:
            estado=18
            f_lexema+=1
    elif estado==18:
        if i in digitos:
            estado=18
            f_lexema+=1
            
        else:
            estado=19
            if i ==" ":
                numeros(i)
    elif estado==19:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
    elif estado==20:#estado final
        flotante=True
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        print(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    elif estado==21:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0  

for i in cadena+" ": #for donde se hace el bucle para recorrer la cadena y dar inicio al automata
    if estado==0:
        if i =='<':
            estado=1
            f_lexema+=1
        elif i == '=':
            estado=5
            f_lexema+=1
        elif i == '>':
            estado=6
            f_lexema+=1
        elif i in sig:
            buscar=TipoToken()
            buscar.esta(i)
            i_lexema=f_lexema
            estado=0
        else:
            estado=9
            f_lexema+=1
            palabra(i)
    elif estado==1:
        if i =='=':
            estado=2
            f_lexema+=1
        elif i == '>':
            estado=3
            f_lexema+=1
        else:
            estado=4
    elif estado==2:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
    elif estado==3:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
    elif estado==4:#estado final con *
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0  
    elif estado==5:
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
    elif estado==5.5:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
    elif estado==6:
        if i =='=':
            estado=7
            f_lexema+=1
        else:
            estado=8    
    elif estado==7:#estadado final 
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
    elif estado==8:#estado final 
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0  
    elif estado==9 or estado==10 or estado==11: #estados para llamar a las funciones
        palabra(i)
    elif estado==12 or estado==13 or estado==14 or estado==15 or estado==16 or estado==18 or estado==17 or estado==19 or estado==20 or estado==21: #estados para llamar a las funciones
        numeros(i) 
    #inicio del automata para detectar espacios en blanco
    elif estado==22:
        if i==" ":
            estado=23
            f_lexema+=1
    elif estado==23:
        if i==" ":
            estado=23
            f_lexema+=1
        else:
            estado=24
    elif estado==24:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema],flotante)
        i_lexema=f_lexema
        estado=0
    

print(Token.tokens) #impresion de tokens

