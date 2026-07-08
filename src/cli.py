from data_structs.graph import SocialGraph
from data_structs.hash_table import HashTable

def start_interactive_menu(social_graph: SocialGraph, hash_table: HashTable) -> None:
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Consultar relaciones de amistad de un usuario")
        print("2. Consultar top N términos más usados")
        print("3. Salir")
        
        choice = input("Seleccione una opción: ").strip()
        
        match choice:
            case "1":
                user_id = input("Ingrese el ID del usuario: ").strip()
                if not user_id:
                    print("El ID del usuario no puede estar vacío.")
                    continue
                    
                try:
                    connections = social_graph.bfs_get_connections(user_id)
                    if connections:
                        print(f"\nConexiones de usuario {user_id}:")
                        print(f"Grado 1: \n{connections[0]}")
                        print(f"\nGrado 2: \n{connections[1] if len(connections) > 1 else 'Ninguna'}")
                        print(f"\nGrado 3: \n{connections[2] if len(connections) > 2 else 'Ninguna'}")
                    else:
                        print(f"No se encontraron conexiones para el usuario {user_id}.")
                except Exception as e:
                    print(f"Ocurrió un error al consultar las conexiones: {e}")
                    
            case "2":
                n_str = input("Ingrese la cantidad de términos top a consultar (N): ").strip()
                if not n_str.isdigit() or int(n_str) <= 0:
                    print("Por favor, ingrese un número entero positivo válido.")
                    continue
                
                n = int(n_str)
                try:
                    top_terms = hash_table.get_top_n(n)
                    if top_terms:
                        print(f"\nTop {n} términos más frecuentes:")
                        for i, entry in enumerate(top_terms, 1):
                            print(f"{i}. {entry.hashtag}: {entry.count}")
                    else:
                        print("No se encontraron términos.")
                except Exception as e:
                    print(f"Ocurrió un error al consultar los términos: {e}")
                    
            case "3":
                print("Saliendo del programa...")
                break
                
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
