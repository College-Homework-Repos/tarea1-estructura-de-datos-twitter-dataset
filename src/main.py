import time

from data_structs.graph import SocialGraph
from data_structs.hash_table import HashTable
from inverted_index.posts import PostsInvertedIndex
from inverted_index.users import UsersInvertedIndex
from stopwords import ALL_STOPWORDS

# TODO: Remove 100 max rows implementation
# DATA_DIR = "./data/test_data"  # 100 max rows
# DATA_DIR = "./data/less_data"  # 1500 max rows
DATA_DIR = "./data/release_data"  # 5000 max rows
FRIENDS_CSV = DATA_DIR + "/friends.csv"
LIKES_CSV = DATA_DIR + "/likes.csv"
USERS_CSV = DATA_DIR + "/user_info.csv"
POSTS_CSV = DATA_DIR + "/user_tweets.csv"


def print_users_data() -> None:

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
    print("Grado 1\n:", user1_connections[0])
    print("Grado 2\n:", user1_connections[1])
    print("Grado 3\n:", user1_connections[2])

    print("\nConexiones de usuario 1:")
    print("Grado 1\n:", user2_connections[0])
    print("Grado 2\n:", user2_connections[1])
    print("Grado 3\n:", user2_connections[2])

    print("\nConexiones de usuario 1:")
    print("Grado 1\n:", user3_connections[0])
    print("Grado 2\n:", user3_connections[1])
    print("Grado 3\n:", user3_connections[2])


def print_posts_data() -> None:
    posts_index = PostsInvertedIndex(ALL_STOPWORDS)

    print("Cargando posts en indice invertido...")
    posts_index.load_data_from_csv(POSTS_CSV, LIKES_CSV)

    print(f"Tamaño de vocabulario (hashtags únicos): {len(posts_index.index):,}")


def print_hashtable_data() -> None:
    hash_table = HashTable()
    print("Cargando posts en tabla hash...")
    hash_table.load_data_from_csv(POSTS_CSV, ALL_STOPWORDS)

    top_terms = hash_table.get_top_n(10)
    print("\nTop 10 hashtags más frecuentes:")
    for i, entry in enumerate(top_terms, 1):
        print(f"{i}. {entry.hashtag}: {entry.count}")

    metrics = hash_table.get_metrics()
    print("\nMétricas de la tabla hash:")
    print(metrics)


def main() -> None:
    start_time = time.time()

    # print_users_data()
    # print_posts_data()
    print_hashtable_data()

    end_time = time.time()
    print(f"\nTiempo total de ejecución: {end_time - start_time:.2f} segundos.")


if __name__ == "__main__":
    main()
