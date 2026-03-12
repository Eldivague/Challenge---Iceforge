from dominio import Guerrero, Mago, Robot
from motor import GameEngine
from interfaz import Interfaz
def iniciar():
# 1. Configuración
    heroe = GameEngine.elegir_jugador()
    rival = Robot("Centinela", 100, 50)
    juego = GameEngine(heroe, rival)

# 2. Ciclo de combate

    while heroe.consultar_vida() > 0 and rival.consultar_vida() > 0:
        juego.mostrar_estado()
        juego.batalla()

    # 3. Resultado
    if heroe.consultar_vida() > 0:
        print("¡GANASTE!")
    else:
        print("HAS SIDO DERROTADO...")

iniciar()