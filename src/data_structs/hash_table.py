import csv
import re
from .linked_list import LinkedList, Node

# N = 721093 (cantidad de hashtags)
# X = 1.5 * N = 1081639.5
# M >= X
# M = 1081657

M_PRIME: int = 1_081_657


class HashtagEntry:
    def __init__(self, hashtag: str) -> None:
        self.hashtag: str = hashtag
        self.count: int = 1


class HashTable:
    def __init__(self) -> None:
        self.size: int = M_PRIME
        self.table: list[LinkedList] = [LinkedList() for _ in range(self.size)]
        self.elements_count: int = 0

    def get_top_n(self, n: int) -> list[HashtagEntry]:
        all_hashtags: list[HashtagEntry] = []
        for i in range(self.size):
            collisions = self.table[i]
            current_node = collisions.head
            while current_node is not None:
                all_hashtags.append(current_node.value)
                current_node = current_node.next

        all_hashtags.sort(key=(lambda entry: entry.count), reverse=True)
        return all_hashtags[:n]

    def get_metrics(self) -> dict[str, int | float]:
        total_collisions: int = 0
        max_list_len: int = 0
        occupied_slots: int = 0
        average_list_len: float = 0.0

        for i in range(self.size):
            collisions = self.table[i]
            c_len: int = collisions.size
            if c_len > 0:
                occupied_slots += 1
                total_collisions += c_len - 1
                if c_len > max_list_len:
                    max_list_len = c_len

        if occupied_slots > 0:
            average_list_len = self.elements_count / occupied_slots

        return {
            "total_collisions": total_collisions,
            "max_list_length": max_list_len,
            "average_list_length": average_list_len,
        }

    def load_data_from_csv(self, posts_csv: str, stopwords: set[str]) -> None:
        with open(posts_csv, "r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                for key, value in row.items():
                    if not (key.startswith("tweet_") and value):
                        continue

                    words: list[str] = re.findall(r"[^\W_]+", value.lower())
                    for word in words:
                        if word in stopwords:
                            continue

                        self._insert(word)

    def _get_djb2_hash(self, key: str) -> int:
        hash_value: int = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)

        hash_value &= 0xFFFFFFFF
        return hash_value % self.size

    def _insert(self, hashtag: str) -> None:
        index: int = self._get_djb2_hash(hashtag)
        current_node: Node | None = self.table[index].head
        found: bool = False

        while current_node is not None:
            current_entry: HashtagEntry = current_node.value
            if current_entry.hashtag == hashtag:
                current_entry.count += 1
                found = True
                break
            current_node = current_node.next

        if not found:
            entry: HashtagEntry = HashtagEntry(hashtag)
            self.table[index].add_node(entry, hashtag)
            self.elements_count += 1
