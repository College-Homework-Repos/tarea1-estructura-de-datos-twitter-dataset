from data_structs.linked_list import LinkedList

from inverted_index.posts import PostsInvertedIndex
from inverted_index.users import UsersInvertedIndex

from stopwords import ALL_STOPWORDS

DATA_DIR = "./data/test_data"
FRIENDS_CSV = DATA_DIR + "/friends.csv"
LIKES_CSV = DATA_DIR + "/likes.csv"
USERS_CSV = DATA_DIR + "/user_info.csv"
POSTS_CSV = DATA_DIR + "/user_tweets.csv"


def main() -> None:
    users_index = UsersInvertedIndex()
    posts_index = PostsInvertedIndex(ALL_STOPWORDS)

    print("Cargando usuarios en indice invertido...")
    users_index.populate_from_csv(USERS_CSV, FRIENDS_CSV)
    print("Cargando posts en indice invertido...")
    posts_index.populate_from_csv(POSTS_CSV, LIKES_CSV)

    print("Indices invertidos cargados.")
    print("Cargando consultas...")

    user1_friends: LinkedList = users_index.get_friends("160881623")
    user2_friends: LinkedList = users_index.get_friends("907848145")
    user3_friends: LinkedList = users_index.get_friends("89903824")

    print("\nIndice invertido de usuarios:")
    print("\nAmigos de usuario 1:")
    print(user1_friends)
    print("\nAmigos de usuario 2:")
    print(user2_friends)
    print("\nAmigos de usuario 3:")
    print(user3_friends)

    posts_with_python: LinkedList = posts_index.search_hashtags(["books"])
    posts_with_animals: LinkedList = posts_index.search_hashtags(["dog"])

    print("\nIndice invertido de posts:")
    print("\nBusqueda con hashtag [python]:")
    print(posts_with_python)
    print("\nBusqueda con hashtag [dog, cat]:")
    print(posts_with_animals)


if __name__ == "__main__":
    main()
