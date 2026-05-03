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

    def add_posts(self, posts: LinkedList) -> None:
        current = posts.head
        while current is not None:
            self.add_post(current.value)
            current = current.next

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
