class Crucero:
    def __init__(self,name,route,departure,cost,rooms,capacity,sells,clients,tours,restaurant):
        self.name=name
        self.route=route
        self.departure=departure
        self.cost=cost
        self.rooms=rooms
        self.capacity=capacity
        self.sells=sells
        self.clients=clients
        self.tours=tours
        self.restaurant=restaurant
    def muestra(self):
        """"[Muestra info] """
        print (f'\n 🌴  Nombre: {self.name} \n\n   •Ruta: {self.route} \n\n   •Fecha de salida: {self.departure} \n\n   •Costos: {self.cost} \n\n   •Habitaciones por pasillo: {self.rooms} \n\n   •Capacidad de cada habitación: {self.capacity} \n')

        
