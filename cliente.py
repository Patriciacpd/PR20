class Cliente:
    def __init__(self,nombre,dni,edad,discapacidad,habitacion,monto_total,con_descuento,impuestos,total,tour):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        self.discapacidad=discapacidad
        self.habitacion=habitacion
        self.monto_total=monto_total
        self.con_descuento=con_descuento
        self.impuestos=impuestos
        self.total=total
        self.tour=tour

    def impuesto(self,con_descuento,impuestos,total):
        self.impuestos=self.con_descuento*0.16
        self.total=self.impuestos+con_descuento    
        return True

    def mostrar_factura(self):
        print (f'\n 📃  •Nombre: {self.nombre} \n\n   •Documento de identidad: {self.dni} \n\n   •Edad: {self.edad} \n\n   •Discapacidad: {self.discapacidad} \n\n   •Habitación: {self.habitacion.tipo,self.habitacion.letra,self.habitacion.numero} \n\n   •Monto total: ${self.monto_total} \n\n   •Monto con descuento: ${self.con_descuento} \n\n   •Impuestos: ${self.impuestos} \n\n   •Total: ${self.total} ')
