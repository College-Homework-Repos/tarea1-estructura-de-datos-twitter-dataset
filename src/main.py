from data_structs.linked_list import LinkedList
from data_structs.structs import Post, User
from inverted_index.posts import PostsInvertedIndex
from inverted_index.users import UsersInvertedIndex
from stopwords import ALL_STOPWORDS


def main() -> None:
    print("Pruebas basicas de estructuras")

    sample_list = LinkedList()
    print("Lista vacia:", sample_list.is_empty())
    sample_list.add_node("n1", "n1")
    sample_list.add_node("n2", "n2")
    print("Lista con nodos:", sample_list)
    print("Contiene n1:", sample_list.contains("n1"))
    print("Contiene n3:", sample_list.contains("n3"))

    alice_friends = LinkedList()
    bob_friends = LinkedList()
    carol_friends = LinkedList()

    alice = User("u1", "alice", "Ama los datos", 10, alice_friends)
    bob = User("u2", "bob", "Programador curioso", 5, bob_friends)
    carol = User("u3", "carol", "Disena apps", 8, carol_friends)

    users_index = UsersInvertedIndex()
    users_index.add_user(alice)
    users_index.add_user(bob)
    users_index.add_user(carol)

    users_index.add_friend("alice", bob)
    users_index.add_friend("alice", carol)
    users_index.add_friend("bob", carol)

    print("\nUsuarios indice invertido:")
    print(users_index.get_friends("alice"))

    print(users_index.get_friends("bob"))

    likes_1 = LinkedList()
    likes_2 = LinkedList()
    likes_3 = LinkedList()

    post_1 = Post("p1", "alice", "Aprendiendo Python y datos", likes_1)
    post_2 = Post("p2", "bob", "Python para APIs", likes_2)
    post_3 = Post("p3", "carol", "Diseno y datos con python", likes_3)

    post_1.add_user_like("u2")
    post_1.add_user_like("u3")
    post_2.add_user_like("u1")

    print("\nLikes del post p1:", post_1.likes)

    posts_index = PostsInvertedIndex(ALL_STOPWORDS)
    posts_index.add_post(post_1)
    posts_index.add_post(post_2)
    posts_index.add_post(post_3)

    posts_list = LinkedList()
    posts_list.add_node(post_1, post_1.id)
    posts_list.add_node(post_2, post_2.id)
    posts_list.add_node(post_3, post_3.id)
    posts_index.add_posts(posts_list)

    python_posts = posts_index.search_hashtags(["python"])
    print("\nBusqueda con un hashtag [python]:")
    print(python_posts)

    print("\nBusqueda con varios hashtag [python, datos]:")
    python_multi_search = posts_index.search_hashtags(["python", "datos"])
    print(python_multi_search)


if __name__ == "__main__":
    main()
