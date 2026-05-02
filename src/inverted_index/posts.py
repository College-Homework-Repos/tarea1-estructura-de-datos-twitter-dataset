import re

from data_structs.linked_list import LinkedList
from data_structs.structs import Post


class PostsInvertedIndex:
    def __init__(self, stopwords: list[str]) -> None:
        self.index: dict[str, LinkedList] = {}
        self.stopwords = stopwords

    def add_post(self, post: Post) -> None:
        for hashtag in self._get_hashtags(post.text):
            if hashtag not in self.index:
                self.index[hashtag] = LinkedList()
            self.index[hashtag].add_node(post)

    def _get_hashtags(self, text: str) -> list[str]:
        words = re.findall(r"[A-Za-z0-9]+", text.lower())
        return [hashtag for hashtag in words if hashtag not in self.stopwords]
