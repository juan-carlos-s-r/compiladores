class TipoToken:

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

    def esta(self,cadena):
        print("hola")
        self.cadena=cadena
        if cadena in TipoToken.reservadas:
            print("cadena en reservadas",self.cadena)
        elif cadena in TipoToken.signos:
            print("cadena en signos",self.cadena)
        else:
            print("la cadena no esta")
