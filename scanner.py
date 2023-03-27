
from TipoToken import *

sig=('(',')','{','}',"'",'.',';','-','+','*','/','!','!=','=','==','<','<=','>','>=')
pareser=()
alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
digitos=('0','1','2','3','4','5','6','7','8','9')

cadena=""
estado=0
i_lexema=0
f_lexema=0




for i in cadena:
    if estado==0:
        if i =='<':
            estado=1
        elif i == '=':
            estado=5
        elif i == '>':
            estado=6
        else:
            estado=9
    if estado==1:
        if i =='=':
            estado=2
        elif i == '>':
            estado=3
        else:
            estado=4
    if estado==2:#estado final
        pass    
    if estado==3:#estado final
        pass
    if estado==4:#estado final con *
        pass    
    if estado==5:#estado final 
        pass
    if estado==6:
        if i =='=':
            estado=7
        else:
            estado=8    
    if estado==7:#estadado final 
        pass
    if estado==8:#estado final 
        pass    
    if estado==9:
        if i in alfabeto:
            estado=10
        else:
            estado=12
    if estado==10:
        if i in alfabeto or i in digitos:
            estado=10
        else:
            estado=11 
    if estado==11:#estado final
        pass
    if estado==12:
        if i in digitos:
            estado=13
        else:
            estado=22    
    if estado==13:
        if i in digitos:
            estado=13
        elif i ==".":
            estado=14
        elif i =="E":
            estado=16
        else:
            estado=20
    if estado==14:
        if i in digitos:
            estado=15    
    if estado==15:
        if i in digitos:
            estado=15
        elif i =="E":
            estado=16
        else:
            estado=21
    if estado==16:
        if i in digitos:
            estado=18
        elif i =="+" or i=="-":
            estado=17    
    if estado==17:
        if i in digitos:
            estado=18
    if estado==18:
        if i in digitos:
            estado=18
        else:
            estado=19
    if estado==19:#estado final
        pass
    if estado==20:#estado final
        pass
    if estado==21:#estado final
        pass    
    if estado==22:
        if i==" ":
            estado=23
    if estado==23:
        if i==" ":
            estado=23
        else:
            estado=24
    if estado==24:#estado final
        pass
    

print(estado)