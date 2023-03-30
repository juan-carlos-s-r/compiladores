class Token:

    tokens=[]

    def generar_1(self,tipo,cadena,literal):
        self.cadena=cadena
        self.tipo=tipo
        self.literal=literal
        
        token=Token

        token.tokens.add(self.tipo," ",self.cadena," ",self.literal)
    
    def generar_2(self,tipo,cadena):
        self.tipo=tipo
        self.cadena=cadena
        
        token=Token

        token.tokens.add(self.tipo," ",self.cadena)

token=Token
cadena='var'
tipo='var'

token.generar_2('var','var')       
print(Token.tokens)


