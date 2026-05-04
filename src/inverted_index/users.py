import csv

from data_structs.linked_list import LinkedList
from data_structs.structs import User


class UsersInvertedIndex:
    def __init__(self) -> None:
        self._index: dict[str, LinkedList] = {}

    def add_user(self, user: User) -> bool:
        if user.id not in self._index:
            self._index[user.id] = LinkedList()
            return True
        return False

    def add_friend(self, user_id: str, friend: User) -> bool:
        if user_id not in self._index:
            self._index[user_id] = LinkedList()
        return self._index[user_id].add_node(friend, friend.id)

    def get_friend(self, user_name: str):
        return self._index.get(user_name)

    def get_friends(self, user_id: str):
        friend = self._index.get(user_id)
        if friend is None:
            return LinkedList()
        return friend

    def populate_from_csv(self, users_csv: str, friends_csv: str) -> None:
        users_by_id: dict[str, User] = {}
        with open(users_csv, "r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                user_id = row.get("id")
                name = row.get("name")
                description = row.get("description") or ""
                followers_text = row.get("followers_count") or "0"
                if not user_id or not name:
                    continue
                followers_count = int(followers_text) if followers_text.isdigit() else 0
                user = User(user_id, name, description, followers_count, LinkedList())
                self.add_user(user)
                users_by_id[user_id] = user

        with open(friends_csv, "r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                user_id = row.get("user_id")
                friends_raw = row.get("friends", "")
                if not user_id:
                    continue
                user = users_by_id.get(user_id)
                if user is None:
                    continue
                friend_ids = [item for item in friends_raw.split(";") if item]
                for friend_id in friend_ids:
                    friend_user = users_by_id.get(friend_id)
                    if friend_user is not None:
                        self.add_friend(user.id, friend_user)
