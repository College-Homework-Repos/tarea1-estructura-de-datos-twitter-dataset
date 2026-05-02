from data_structs.linked_list import LinkedList
from data_structs.structs import User


class UsersInvertedIndex:
    def __init__(self) -> None:
        self.index: dict[str, LinkedList] = {}

    def add_user(self, user: User) -> None:
        if user.name not in self.index:
            self.index[user.name] = LinkedList()

    def add_friend(self, user_name: str, friend: User) -> bool:
        if user_name not in self.index:
            self.index[user_name] = LinkedList()
        return self.index[user_name].add_node(friend)

    def get_friend(self, user_name: str):
        return self.index.get(user_name)

    def get_friends(self, user_name: str):
        friend = self.index.get(user_name)
        if friend is None:
            return LinkedList()
        return friend
