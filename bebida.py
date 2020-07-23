from producto import Producto

class Bebida(Producto):
    def __init__(self,nombre,tipo,precio,size):
        Producto.__init__(self,nombre,tipo,precio)
        self.size=size

    def show(self):
        return "\n •Nombre: {}, Tipo: {}, Precio: ${}, Tamaño: {} ".format(self.nombre,self.tipo,self.precio,self.size)