class Token:

    tokens=[]

    def generar_1(self,tipo,cadena,literal):
        self.cadena=cadena
        self.tipo=tipo
        self.literal=literal
        
        token=Token
        valor=self.tipo+","+self.cadena+","+self.literal
        token.tokens.append(valor)
    
    def generar_2(self,tipo,cadena):
        self.tipo=tipo
        self.cadena=cadena
        
        token=Token
        valor=self.tipo+","+self.cadena
        token.tokens.append(valor)

token=Token()
cadena='var'
tipo='var'
literal='var'

token.generar_2(tipo,cadena)          
print(Token.tokens)
token.generar_1('izquierdo','derecho','derecho')
print(Token.tokens)