from TipoToken import * #importaciones de las classes
from Token import *

class parser:
    index=0

    def siguiente(self):
        self.index+=1
        if self.index < len(Token.tokens):
            self.token_actual=