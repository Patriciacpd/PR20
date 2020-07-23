class Habitacion:
    def __init__(self,letra,numero,capacidad,referencia,permite):
        self.letra=letra
        self.numero=numero
        self.capacidad=capacidad
        self.referencia=referencia
        self.permite=permite
    def show_me(self):
        return "Letra: {}\n Número: {}\n Capacidad: {}\n Referencia: {}\n Comodidad que ofrece: {}".format(self.letra,self.numero,self.capacidad,self.referencia,self.permite)
    

        
