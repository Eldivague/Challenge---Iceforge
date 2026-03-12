class Entidad:
    def __init__(self, nombre, vida, energia):
        if type(self) == Entidad:
            raise Exception("No puedes instanciar la clase base directamente.")
        self.nombre = nombre
        self.__vida = vida
        self.__energia = energia
        self.esta_vivo = True

    def consultar_vida(self): return self.__vida
    def consultar_energia(self): return self.__energia

    def recibir_danio(self, cantidad):
        self.__vida -= cantidad
        if self.__vida <= 0:
            self.__vida = 0
            self.esta_vivo = False

    def modificar_energia(self, cantidad):
        self.__energia += cantidad
        if self.__energia < 0: self.__energia = 0
        if self.__energia > 100: self.__energia = 100

class Guerrero(Entidad):
    def habilidad_especial(self):
        if self.consultar_energia() >= 30:
            self.modificar_energia(-30)
            return 40
        return 0

class Mago(Entidad):
    def habilidad_especial(self):
        if self.consultar_energia() >= 40:
            self.modificar_energia(-40)
            return 60
        return 0

class Robot(Entidad):
    def habilidad_especial(self):
        if self.consultar_energia() >= 25:
            self.modificar_energia(-25)
            return 30
        return 0