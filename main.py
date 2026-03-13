from dominio import Robot
from motor import GameEngine



heroe = GameEngine.elegir_jugador()
rival = Robot("Centinela", 200, 80)
juego = GameEngine(heroe, rival)

juego.iniciar_juego()