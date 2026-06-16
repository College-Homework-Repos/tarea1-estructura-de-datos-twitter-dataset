import time

from data_structs.graph import SocialGraph
from inverted_index.users import UsersInvertedIndex

# DATA_DIR = "./data/test_data"  # 100 max rows
DATA_DIR = "./data/less_data"  # 1500 max rows
FRIENDS_CSV = DATA_DIR + "/friends.csv"
LIKES_CSV = DATA_DIR + "/likes.csv"
USERS_CSV = DATA_DIR + "/user_info.csv"
POSTS_CSV = DATA_DIR + "/user_tweets.csv"


def main() -> None:
    start_time = time.time()

    users_index = UsersInvertedIndex()
    social_graph = SocialGraph()

    print("Cargando usuarios en indice invertido...")
    users_by_id = users_index.load_data_from_csv(USERS_CSV, FRIENDS_CSV)

    print("Cargando relaciones en el grafo social...")
    social_graph.load_data_from_inverted_index(users_index.index, users_by_id)

    print(
        "\nLas relaciones son simétricas?: ",
        social_graph.validate_symmetric_relations(),
    )

    user1_connections = social_graph.bfs_get_connections("160881623")
    user2_connections = social_graph.bfs_get_connections("907848145")
    user3_connections = social_graph.bfs_get_connections("89903824")

    print("\nConexiones de usuario 1:")
    print("Grado 1:", user1_connections[0])
    print("Grado 2:", user1_connections[1])
    print("Grado 3:", user1_connections[2])

    print("\nConexiones de usuario 1:")
    print("Grado 1:", user2_connections[0])
    print("Grado 2:", user2_connections[1])
    print("Grado 3:", user2_connections[2])

    print("\nConexiones de usuario 1:")
    print("Grado 1:", user3_connections[0])
    print("Grado 2:", user3_connections[1])
    print("Grado 3:", user3_connections[2])

    end_time = time.time()
    print(f"\nTiempo total de ejecución: {end_time - start_time:.2f} segundos.")


if __name__ == "__main__":
    main()
