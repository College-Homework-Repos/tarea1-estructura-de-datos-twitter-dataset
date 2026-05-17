import csv
import re

from data_structs.linked_list import LinkedList
from data_structs.structs import Post


class PostsInvertedIndex:
    def __init__(self, stopwords: list[str]) -> None:
        self._index: dict[str, LinkedList] = {}
        self._stopwords = stopwords

    def add_post(self, post: Post) -> None:
        for hashtag in self._get_hashtags_from_post(post.text):
            if hashtag not in self._index:
                self._index[hashtag] = LinkedList()
            self._index[hashtag].add_node(post, post.id)

    def search_hashtags(self, hashtags: list[str]) -> LinkedList:
        if not hashtags:
            return LinkedList()

        result = self._index.get(hashtags[0])
        if result is None:
            return LinkedList()

        current = result
        for term in hashtags[1:]:
            next_list = self._index.get(term)
            if next_list is None:
                return LinkedList()
            current = self._intersect_posts(current, next_list)
        return current

    def _get_hashtags_from_post(self, text: str) -> list[str]:
        words = re.findall(r"[A-Za-z0-9]+", text.lower())
        return [hashtag for hashtag in words if hashtag not in self._stopwords]

    def _intersect_posts(self, left: LinkedList, right: LinkedList) -> LinkedList:
        intersection = LinkedList()
        current = left.head
        while current is not None:
            post = current.value
            if right.contains(post.id):
                intersection.add_node(post, post.id)
            current = current.next
        return intersection

    def populate_from_csv(self, posts_csv: str, likes_csv: str) -> None:
        likes_map: dict[str, LinkedList] = {}

        with open(likes_csv, "r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                user_id = row.get("user_id")
                post_id = row.get("post_id")
                if not user_id or not post_id:
                    continue
                likes_list = likes_map.get(post_id)
                if likes_list is None:
                    likes_list = LinkedList()
                    likes_map[post_id] = likes_list
                likes_list.add_node(user_id, user_id)

        with open(posts_csv, "r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                user_id = row.get("id")
                if not user_id:
                    continue
                for key, value in row.items():
                    if key.startswith("tweet_") and value:
                        post_id = f"{user_id}_{key}"
                        likes = likes_map.get(post_id)
                        if likes is None:
                            likes = LinkedList()
                        post = Post(post_id, user_id, value, likes)
                        self.add_post(post)
