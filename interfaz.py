# Creamos la clase interfaz para todo lo que se va mostrar en la pantalla
class Interfaz:    
    
    @staticmethod
    def menu_clase():
        print("--- SELECCION DE PERSONAJE ---")
        print("1. Guerrero | 2. Mago | 3. Robot")
        return input("Selecciona tu unidad: ")

    @staticmethod
    def menu_acciones():
        print("\n¿Qué deseas hacer?")
        print("1. Ataque Básico\n2. Habilidad Especial\n3. Descansar")
        return input("Acción: ")

    @staticmethod
    def perder():
        print(" ROBOT CENTINELA X9 a ganado... ")

    @staticmethod
    def ganar():
        print(" Has ganado a ROBOT CENTINELA X9 !!! ")

    @staticmethod
    def imprimir_mensaje(msg):
        print(f">> {msg}")