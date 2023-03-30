from Token import *

alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
digitos=('0','1','2','3','4','5','6','7','8','9')


class TipoToken:

    #diccionario de signos para obtener el tipo mediante una llave
    signos={'(':'parentesis izquierdo',
        ')':'parenteis derecho',
        '{':'llave izquierda',
        '}':'llave derecha',
        "'":'comilla simple',
        '.':'punto',
        ';':'punto y coma',
        '-':'guion',
        '+':'mas',
        '*':'asterisco',
        '/':'diagonal',
        '!':'negador',
        '!=':'diferente',
        '=':'asignacion',
        '==':'igual',
        '<':'menor que',
        '<=':'menor igual',
        '>':'mayor que',
        '>=':'mayor igual'}
    
    #Diccionario de palabras reservadas para obtener el tipo mediante una llave
    reservadas={'y':'y',
        'clase':'clase',
        'ademas':'ademas',
        'falso':'falso',
        'para':'para',
        'fun':'fun',
        'si':'si',
        'nulo:':'nulo',
        'o':'o',
        'imprimir':'imprimir',
        'retomar':'retomar',
        'super':'super',
        'este':'este',
        'verdadero':'verdadero',
        'var':'var',
        'mientras':'mientras'}

    #funcion donde se busca si esta en signos o en palabras resevadas para posteriormente generar el token a esta funcion le llega cadena que en realidad es el lexema y flotante solo para verficar el numero
    def esta(self,cadena,flotante):
        self.cadena=cadena
        #se verifica si esta en reservadas de ser asi manda 2 parametros 
        if cadena in TipoToken.reservadas:
            token=Token()
            token.generar_2(TipoToken.reservadas[cadena],cadena)

        #se verifica si esta en signos de ser asi manda 2 parametros 
        elif cadena in TipoToken.signos:
            token=Token()
            token.generar_2(TipoToken.signos[cadena],cadena)
        
        #se verifica si empieza con una letra del alfabeto de ser asi como ya sabemos del automata es una cadena y envia 3 parametos 
        elif cadena[0] in alfabeto:
            token=Token()
            token.generar_1("'cadena'",cadena,cadena[0:len(cadena)-1])
        
        #se verifica si empieza con un digito de ser asi como ya sabemos del automata es una numero y envia 3 parametos solamente se verifica si es entero o flotante
        elif cadena[0] in digitos:
            if flotante==True:
                token=Token()
                token.generar_1("'entero'",cadena,cadena[0:len(cadena)-1])
                
            else:
                token=Token()
                token.generar_1("'flotante'",cadena,cadena[0:len(cadena)-1])
        else:
            print("Error lexico",cadena)
                
