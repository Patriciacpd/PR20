from habitacion import Habitacion

class Premium(Habitacion):
    def __init__(self,letra,numero,capacidad,referencia,permite="Vista al mar",tipo="premium"):
        Habitacion.__init__(self,letra,numero,capacidad,referencia,permite)
        self.tipo=tipo
    
