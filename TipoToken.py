class TipoToken(object):

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

token="var"

print(TipoToken.reservadas[token])