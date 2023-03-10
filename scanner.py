

sig=('(',')','{','}',"'",'.',';','-','+','*','/','!','!=','=','==','<','<=','>','>=')
pareser=()
alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
digitos=('0','1','2','3','4','5','6','7','8','9')

cadena="="
estado=0





for i in cadena:
    if estado==0:
        if i =='<':
            estado=1
        elif i == '=':
            estado=5
        elif i == '>':
            estado=6
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
        pass    
    if estado==7:#estadado final 
        pass
    if estado==8:#estado final 
        pass    
    if estado==9:
        pass
    if estado==10:
        pass    
    if estado==11:
        pass
    if estado==12:
        pass    
    if estado==13:
        pass
    if estado==14:
        pass    
    if estado==15:
        pass
    if estado==16:
        pass    
    if estado==17:
        pass
    if estado==18:
        pass    
    if estado==19:
        pass
    

print(estado)