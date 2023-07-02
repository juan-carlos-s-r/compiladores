

class Token:

    tokens=[]

    #genera el token de las variables y los numeros
    def generar_1(self,tipo,cadena,literal):
        self.cadena=cadena
        self.tipo=tipo
        self.literal=literal
        
        #guarda los tokens generados en una lista para posteriormente imprimirlos
        token=Token
        valor=self.tipo,self.cadena,self.literal
        token.tokens.append([valor])
        
        
    #genera la variable de tipo reservado
    def generar_2(self,tipo,cadena):
        self.tipo=tipo
        self.cadena=cadena
        
        #guarda los tokens generados en una lista para posteriormente imprimirlos
        token=Token
        valor=self.tipo,self.cadena
        token.tokens.append([valor])
