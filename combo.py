from producto import Producto

class Combo(Producto):
    def __init__(self,nombre,tipo,precio,cantidad,productos):
        Producto.__init__(self,nombre,tipo,precio)
        self.cantidad=cantidad
        self.productos=productos
       
    def iva(self,precio):
        if precio<=0 or precio>2000:
            return False
        self.precio+= (self.precio*0.16)    
        return True
   
    def show(self):
        return "\n •Nombre: {}, Tipo: {}, Precio: ${}, Cantidad: {}, Productos: {} ".format(self.nombre,self.tipo,self.precio,self.cantidad,self.productos)