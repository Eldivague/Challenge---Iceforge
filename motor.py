
class GameEngine:
    def __init__(self, jugador, rival):
        self.jugador = jugador
        self.rival = rival

    def mostrar_estado(self):
        print(f"\n[ {self.jugador.nombre} HP: {self.jugador.consultar_vida()} ] vs [ {self.rival.nombre} HP: {self.rival.consultar_vida()} ]")

    def ejecutar_turno_ia(self):
        # Lógica de "pensamiento" del rival
        if self.rival.consultar_energia() >= 40:
            return self.rival.habilidad_especial()
        else:
            return 10 # Ataque básico

    def finalizar(self):
        return self.jugador.esta_vivo