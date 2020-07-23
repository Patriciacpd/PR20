from habitacion import Habitacion

class Sencilla(Habitacion):
    def __init__(self,letra,numero,capacidad,referencia,permite="Servicio a la habitación",tipo="sencilla"):
        Habitacion.__init__(self,letra,numero,capacidad,referencia,permite)
        self.tipo=tipo
    
