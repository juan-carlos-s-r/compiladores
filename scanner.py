
from TipoToken import *

sig=('(',')','{','}',"'",'.',';','-','+','*','/','!','!=','=','==','<','<=','>','>=')
pareser=()
alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
digitos=('0','1','2','3','4','5','6','7','8','9')

cadena="int main(){print(b);}"
estado=0
i_lexema=0
f_lexema=0
lexema=""



for i in cadena+" ":
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
        else:
            estado=9
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
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    elif estado==3:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    elif estado==4:#estado final con *
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0  
    elif estado==5:#estado final 
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
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
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    elif estado==8:#estado final 
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0  
    elif estado==9:
        if i in alfabeto:
            estado=10
            f_lexema+=1
        else:
            estado=12
    elif estado==10:
        if i in alfabeto or i in digitos:
            estado=10
            f_lexema+=1
        else:
            estado=11 
    elif estado==11:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    elif estado==12:
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
        elif i =="E":
            estado=16
            f_lexema+=1
        else:
            estado=20
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
    elif estado==19:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    elif estado==20:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    elif estado==21:#estado final
        buscar=TipoToken()
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0   
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
        buscar.esta(cadena[i_lexema:f_lexema])
        i_lexema=f_lexema
        estado=0
    



print(estado,"-", lexema,"-",f_lexema)
print(cadena[i_lexema:f_lexema])