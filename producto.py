class Producto:
    restaurant="Saman Caribbean"
    def __init__(self,nombre,tipo,precio):
        self.nombre=nombre
        self.tipo=tipo
        self.precio=precio

    def iva(self,precio):
        """Verifica si el precio es el correcto y le suma al mismo 
        la cantidad correspondiente de IVA """
        if precio<=0 or precio>100:
            return False
        self.precio+= (self.precio*0.16)    
        return True

        
