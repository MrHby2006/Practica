import re

pokemones = []

def validar_codigo(codigo):
    if len(codigo) < 8:
        return False
    if ' ' in codigo:
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    if not any(c.isalpha() for c in codigo):
        return False
    return True

def ingresar_pokemon():
    print("--- Ingresar Pokémon ---")
    
    while True:
        try:
            id_pokemon = int(input("Ingrese el Id de pokemon: "))
            if id_pokemon <= 0:
                print("El ID debe ser un número positivo.")
                continue
            if any(p['id'] == id_pokemon for p in pokemones):
                print("Este ID ya está en uso.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número válido para el ID.")
    
    while True:
        nombre = input("Ingrese nombre de pokemon: ").strip().lower()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        if any(p['nombre'] == nombre for p in pokemones):
            print("Este nombre de pokémon ya existe.")
            continue
        break
    
    while True:
        codigo = input("Ingrese código: ").strip()
        if not validar_codigo(codigo):
            print("El código debe tener al menos 8 caracteres, contener al menos 1 número, 1 letra y no tener espacios.")
            continue
        break
    
    tipos_validos = ["fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "eléctrico"]
    while True:
        tipo = input("Ingrese tipo: ").strip().lower()
        if tipo not in tipos_validos:
            print(f'Debe ingresar uno de los siguientes tipos: {", ".join(tipos_validos)}')
            continue
        break
    
    pokemones.append({
        'id': id_pokemon,
        'nombre': nombre,
        'codigo': codigo,
        'tipo': tipo
    })
    
    print("Pokémon ingresado con éxito!!")

def buscar_pokemon():
    print("--- Buscar Pokémon ---")
    nombre = input("Ingrese pokémon a buscar: ").strip().lower()
    
    encontrado = None
    for pokemon in pokemones:
        if pokemon['nombre'] == nombre:
            encontrado = pokemon
            break
    
    if encontrado:
        print(f"El tipo de pokémon es: {encontrado['tipo']} y su código es: {encontrado['codigo']}")
    else:
        print("Pokémon no encontrado.")
    
    print()

def eliminar_pokemon():
    print("--- Eliminar Pokémon ---")
    nombre = input("Ingrese pokémon a eliminar: ").strip().lower()
    
    eliminado = False
    for i, pokemon in enumerate(pokemones):
        if pokemon['nombre'] == nombre:
            del pokemones[i]
            eliminado = True
            break
    
    if eliminado:
        print("Pokémon eliminado con éxito!")
    else:
        print("No se pudo eliminar pokémon!")
    
    print()

def listar_pokemones():
    print("--- Listado de Pokémones ---")
    if not pokemones:
        print("No hay pokémones registrados.")
    else:
        for pokemon in pokemones:
            print(f"ID: {pokemon['id']}, Nombre: {pokemon['nombre']}, Tipo: {pokemon['tipo']}, Código: {pokemon['codigo']}")
    print()

def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1.- Ingresar pokemon.")
    print("2.- Buscar pokemon.")
    print("3.- Eliminar pokemon")
    print("4.- Listar pokemones")
    print("5.- Salir.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ").strip()
        
        if opcion == "1":
            ingresar_pokemon()
        elif opcion == "2":
            buscar_pokemon()
        elif opcion == "3":
            eliminar_pokemon()
        elif opcion == "4":
            listar_pokemones()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
