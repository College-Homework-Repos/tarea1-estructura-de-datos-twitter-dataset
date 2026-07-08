from data_structs.graph import SocialGraph
from data_structs.hash_table import HashTable
from inverted_index.users import UsersInvertedIndex
from stopwords import ALL_STOPWORDS
from cli import start_interactive_menu

# DATA_DIR = "./data/less_data"  # 1500 max rows
DATA_DIR = "./data/release_data"  # 5000 max rows
FRIENDS_CSV = DATA_DIR + "/friends.csv"
LIKES_CSV = DATA_DIR + "/likes.csv"
USERS_CSV = DATA_DIR + "/user_info.csv"
POSTS_CSV = DATA_DIR + "/user_tweets.csv"

# Funcionamiento del programa en vivo
# 1. Consulta de contacots grado 1, 2 y 3.
# 2. Consulta top-N hashtags más frecuentes.


def main() -> None:
    # Inicializamos las estructuras de datos
    users_index = UsersInvertedIndex()
    social_graph = SocialGraph()
    hash_table = HashTable()

    # Cargamos los datos en las estructuras de datos
    print("Cargando usuarios en indice invertido...")
    users_by_id = users_index.load_data_from_csv(USERS_CSV, FRIENDS_CSV)
    print("Cargando relaciones en el grafo social...")
    social_graph.load_data_from_inverted_index(users_index.index, users_by_id)
    print("Cargando posts en tabla hash...")
    hash_table.load_data_from_csv(POSTS_CSV, ALL_STOPWORDS)

    # Se comprueba que las relaciones del grafo sean simétricas.
    print("Datos cargados correctamente.")
    print(
        "\nLas relaciones del grafo son simétricas?: ",
        social_graph.validate_symmetric_relations(),
    )

    # Iniciamos el menú interactivo
    start_interactive_menu(social_graph, hash_table)


if __name__ == "__main__":
    main()
