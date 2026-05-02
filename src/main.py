from data_structs.linked_list import LinkedList
from data_structs.structs import Post, User
from inverted_index.posts import PostsInvertedIndex
from inverted_index.users import UsersInvertedIndex


def main():
    print("Pruebas basicas de estructuras")

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
    users_index.get_friends("alice").print_list()

    users_index.get_friends("bob").print_list()

    likes_1 = LinkedList()
    likes_2 = LinkedList()
    likes_3 = LinkedList()

    post_1 = Post("p1", "alice", "Aprendiendo Python y datos", likes_1)
    post_2 = Post("p2", "bob", "Python para APIs", likes_2)
    post_3 = Post("p3", "carol", "Diseno y datos con python", likes_3)

    post_1.add_user_like("u2")
    post_1.add_user_like("u3")
    post_2.add_user_like("u1")

    stopwords = ["y", "para", "con"]
    posts_index = PostsInvertedIndex(stopwords)
    posts_index.add_post(post_1)
    posts_index.add_post(post_2)
    posts_index.add_post(post_3)

    python_posts = posts_index.index.get("python")
    if python_posts is None:
        python_posts = LinkedList()

    print('\nPosts hashtag="python":')
    python_posts.print_list()


if __name__ == "__main__":
    main()
