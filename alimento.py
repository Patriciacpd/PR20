from producto import Producto

class Alimento(Producto):
    def __init__(self,nombre,tipo,precio,modo):
        Producto.__init__(self,nombre,tipo,precio)
        self.modo=modo
    def show(self):
        return "\n •Nombre: {}, Tipo: {}, Precio: ${}, Modo: {} ".format(self.nombre,self.tipo,self.precio,self.modo)

