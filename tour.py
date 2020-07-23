class Tour:
    def __init__(self,nombre,precio,maxi,hora,cupo="No tiene límite"):
        self.nombre=nombre
        self.precio=precio
        self.maxi=maxi
        self.hora=hora
        self.cupo=cupo


    def mostrar(self):
        print(f"\n •Nombre del tour: {self.nombre} \nPrecio por persona: {self.precio} \nLímite de personas: {self.maxi} \nHora en la que empieza: {self.hora}:00 horas \nCupos disponibles: {self.cupo} ")