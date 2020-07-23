from habitacion import Habitacion

class Vip(Habitacion):
    def __init__(self,letra,numero,capacidad,referencia,permite="Fiestas privadas",tipo="vip"):
        Habitacion.__init__(self,letra,numero,capacidad,referencia,permite)
        self.tipo=tipo
    
