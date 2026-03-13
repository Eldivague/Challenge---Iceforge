# Se importan las clases necesarias para iniciar el juego
from dominio import Robot
from motor import GameEngine

# Se crean los personajes para iniciar el juego
heroe = GameEngine.elegir_jugador()
rival = Robot("ROBOT CENTINELA X9", 200, 80)
juego = GameEngine(heroe, rival)

# Se inicia el juego
juego.iniciar_juego()