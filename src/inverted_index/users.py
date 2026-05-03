from data_structs.linked_list import LinkedList
from data_structs.structs import User


class UsersInvertedIndex:
    def __init__(self) -> None:
        self._index: dict[str, LinkedList] = {}

    def add_user(self, user: User) -> bool:
        if user.name not in self._index:
            self._index[user.name] = LinkedList()
            return True
        return False

    def add_friend(self, user_name: str, friend: User) -> bool:
        if user_name not in self._index:
            self._index[user_name] = LinkedList()
        return self._index[user_name].add_node(friend, friend.id)

    def get_friend(self, user_name: str):
        return self._index.get(user_name)

    def get_friends(self, user_name: str):
        friend = self._index.get(user_name)
        if friend is None:
            return LinkedList()
        return friend
