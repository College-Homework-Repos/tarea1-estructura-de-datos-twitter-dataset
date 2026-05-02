from typing import Any

from .linked_list import LinkedList


class User:
    def __init__(
        self,
        user_id: str,
        name: str,
        description: str,
        followers_count: int,
        friends: LinkedList,
    ) -> None:
        self.user_id = user_id
        self.name = name
        self.description = description
        self.followers_count = followers_count
        self.friends = friends

    def add_friend(self, friend: Any) -> bool:
        added = self.friends.add_node(friend)
        return added

    def __str__(self) -> str:
        return f'User(id="{self.user_id:.5}", name="{self.name:.10}")'


class Post:
    def __init__(
        self,
        post_id: str,
        author: str,
        text: str,
        likes: LinkedList,
    ) -> None:
        self.post_id = post_id
        self.author = author
        self.text = text
        self.likes = likes

    def add_user_like(self, user_id: str) -> bool:
        return self.likes.add_node(user_id)

    def __str__(self) -> str:
        return f'Post(id="{self.post_id:.5}", author="{self.author:.10}", text="{self.text:.10}...")'
