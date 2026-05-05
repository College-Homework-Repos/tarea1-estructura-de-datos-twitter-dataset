from .linked_list import LinkedList


class User:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        followers_count: int,
        friends: LinkedList,
    ) -> None:
        self.id: str = id
        self.name: str = name
        self.description: str = description
        self.followers_count: int = followers_count
        self.friends: LinkedList = friends

    def add_friend(self, friend: "User") -> bool:
        added = self.friends.add_node(friend.id, friend.id)
        return added

    def __str__(self) -> str:
        return f'User(id="{self.id:.5}", name="{self.name:.10}")'


class Post:
    def __init__(
        self,
        id: str,
        author: str,
        text: str,
        likes: LinkedList,
    ) -> None:
        self.id: str = id
        self.author: str = author
        self.text: str = text
        self.likes: LinkedList = likes

    def add_user_like(self, user_id: str) -> bool:
        return self.likes.add_node(user_id, user_id)

    def __str__(self) -> str:
        return (
            f'Post(id="{self.id}", author="{self.author}", text="{self.text:.10}...")'
        )
