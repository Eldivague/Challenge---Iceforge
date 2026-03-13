
from dominio import Guerrero, Mago, Robot
from interfaz import Interfaz

class GameEngine:
    def __init__(self, jugador, rival):
        self.jugador = jugador
        self.rival = rival

    def mostrar_estado(self):
        print(f"\n[ {self.jugador.nombre} HP: {self.jugador.consultar_vida()} EN: {self.jugador.consultar_energia()} ] vs [ {self.rival.nombre} HP: {self.rival.consultar_vida()} EN: {self.rival.consultar_energia()} ]")

    def ejecutar_turno_ia(self):
        # Lógica de "pensamiento" del rival
        if self.rival.consultar_energia() >= 40:
            return self.rival.habilidad_especial()
        else:
            return 10 

    def finalizar(self):
        return self.jugador.esta_vivo
    
    @staticmethod
    def elegir_jugador():
        personaje_elegido = Interfaz.menu_clase()
        nombre = input("Elige el nombre de tu heroe: ")

        if personaje_elegido == '1':
            heroe = Guerrero(nombre, 150, 50)
        elif personaje_elegido == '2':
            heroe = Mago(nombre, 100, 120)
        else:
            heroe = Robot(nombre, 120, 80)
        
        return heroe
    
    def batalla(self):
        accion_elegida = Interfaz.menu_acciones()
        danio = 0

        if accion_elegida == '1':
            danio = 20
        elif accion_elegida == '2':
            danio = self.jugador.habilidad_especial()
        else:
            self.jugador.descansar()

        self.rival.recibir_danio(danio)
        
        Interfaz.imprimir_mensaje(f"Hiciste {danio} de daño !!!")

        if self.rival.consultar_vida() > 0:
            danio_ia = self.ejecutar_turno_ia()
            self.jugador.recibir_danio(danio_ia)
            Interfaz.imprimir_mensaje(f"El rival te hizo {danio_ia} de daño.")
        else:
            Interfaz.imprimir_mensaje("¡Has derrotado al rival!")
    
    
    def iniciar_juego(self):
        while self.jugador.consultar_vida() > 0 and self.rival.consultar_vida() > 0:
            self.mostrar_estado()
            self.batalla()

        if self.jugador.consultar_vida() > 0:
            print("¡GANASTE!")
        else:
            print("HAS SIDO DERROTADO...")