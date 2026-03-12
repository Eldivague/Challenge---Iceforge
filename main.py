from dominio import Guerrero, Mago, Robot
from motor import GameEngine
import interfaz

def comenzar():
    # 1. Configuración inicial usando la Interfaz
    opcion_elegida = interfaz.menu_clase()
    nombre = input("Nombre de tu unidad: ")

    if opcion_elegida == "1": heroe = Guerrero(nombre, 120, 100)
    elif opcion_elegida == "2": heroe = Mago(nombre, 80, 100)
    else: heroe = Robot(nombre, 100, 100)

    rival = Robot("Centinela-X9", 100, 50)

    # 2. Inicializar Motor
    juego = GameEngine(heroe, rival)
    
    # 3. Game Loop
    while heroe.esta_vivo and rival.esta_vivo:
        juego.mostrar_estado()
        accion = interfaz.menu_acciones()
        
        # Procesar Jugador
        danio = 0
        if accion == "1": danio = 15
        elif accion == "2": danio = heroe.habilidad_especial()
        else: heroe.modificar_energia(30)
        
        rival.recibir_danio(danio)
        
        # Procesar Rival
        if rival.esta_vivo:
            interfaz.imprimir_mensaje(f"Turno de {rival.nombre}...")
            heroe.recibir_danio(juego.ejecutar_turno_ia())

    # 4. Resultado
    if juego.finalizar():
        interfaz.imprimir_mensaje("¡VICTORIA!")
    else:
        interfaz.imprimir_mensaje("DERROTA...")

if __name__ == "__main__":
    comenzar()