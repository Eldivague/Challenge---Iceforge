def menu_clase():
    print("--- SELECCION DE PERSONAJE ---")
    print("1. Guerrero | 2. Mago | 3. Robot")
    return input("Selecciona tu unidad: ")

def menu_acciones():
    print("\n¿Qué deseas hacer?")
    print("1. Ataque Básico\n2. Habilidad Especial\n3. Descansar")
    return input("Acción: ")

def imprimir_mensaje(msg):
    print(f">> {msg}")