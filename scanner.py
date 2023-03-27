
from TipoToken import *

sig=('(',')','{','}',"'",'.',';','-','+','*','/','!','!=','=','==','<','<=','>','>=')
pareser=()
alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
digitos=('0','1','2','3','4','5','6','7','8','9')

cadena="<="
estado=0
i_lexema=0
f_lexema=0
lexema=""



for i in cadena:
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
        lexema=cadena[i_lexema:f_lexema]    
    elif estado==3:#estado final
        pass
    elif estado==4:#estado final con *
        pass    
    elif estado==5:#estado final 
        pass
    elif estado==6:
        if i =='=':
            estado=7
        else:
            estado=8    
    elif estado==7:#estadado final 
        pass
    elif estado==8:#estado final 
        pass    
    elif estado==9:
        if i in alfabeto:
            estado=10
        else:
            estado=12
    elif estado==10:
        if i in alfabeto or i in digitos:
            estado=10
        else:
            estado=11 
    elif estado==11:#estado final
        pass
    elif estado==12:
        if i in digitos:
            estado=13
        else:
            estado=22    
    elif estado==13:
        if i in digitos:
            estado=13
        elif i ==".":
            estado=14
        elif i =="E":
            estado=16
        else:
            estado=20
    elif estado==14:
        if i in digitos:
            estado=15    
    elif estado==15:
        if i in digitos:
            estado=15
        elif i =="E":
            estado=16
        else:
            estado=21
    elif estado==16:
        if i in digitos:
            estado=18
        elif i =="+" or i=="-":
            estado=17    
    elif estado==17:
        if i in digitos:
            estado=18
    elif estado==18:
        if i in digitos:
            estado=18
        else:
            estado=19
    elif estado==19:#estado final
        pass
    elif estado==20:#estado final
        pass
    elif estado==21:#estado final
        pass    
    elif estado==22:
        if i==" ":
            estado=23
    elif estado==23:
        if i==" ":
            estado=23
        else:
            estado=24
    elif estado==24:#estado final
        pass
    



print(estado,"-", lexema,"-",f_lexema)
print(cadena[i_lexema:f_lexema])