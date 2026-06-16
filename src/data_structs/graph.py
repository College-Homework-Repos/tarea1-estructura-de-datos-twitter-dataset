from collections import deque
from data_structs.linked_list import LinkedList
from data_structs.structs import User


class GraphNode:
    def __init__(self, user: User) -> None:
        self.user: User = user
        self.connections_list: LinkedList = LinkedList()


class SocialGraph:
    def __init__(self) -> None:
        self.graph_nodes: dict[str, GraphNode] = {}

    def load_data_from_inverted_index(
        self, inverted_index: dict[str, LinkedList], users_dict: dict[str, User]
    ) -> None:
        for _, user in users_dict.items():
            self._add_node(user)

        for user_id, friends_list in inverted_index.items():
            current_node = friends_list.head
            while current_node is not None:
                friend_id = current_node.value.id
                self._add_edge(user_id, friend_id)
                current_node = current_node.next

    def validate_symmetric_relations(self) -> bool:
        for user_id, graph_node in self.graph_nodes.items():
            current_node = graph_node.connections_list.head
            while current_node is not None:
                friend_id = current_node.value
                friend_graph_node = self.graph_nodes.get(friend_id)

                if (
                    friend_graph_node is None
                    or not friend_graph_node.connections_list.contains(user_id)
                ):
                    return False
                current_node = current_node.next
        return True

    def bfs_get_connections(
        self, root_user_id: str
    ) -> tuple[LinkedList, LinkedList, LinkedList]:
        degree_1 = LinkedList()
        degree_2 = LinkedList()
        degree_3 = LinkedList()

        if root_user_id not in self.graph_nodes:
            return degree_1, degree_2, degree_3

        queue: deque[tuple[str, int]] = deque([(root_user_id, 0)])
        visited: set[str] = {root_user_id}

        while queue:
            current_id, current_degree = queue.popleft()

            current_graph_node = self.graph_nodes[current_id]
            current_user = current_graph_node.user

            match current_degree:
                case 1:
                    degree_1.add_node(value=current_user, id=current_id)
                case 2:
                    degree_2.add_node(value=current_user, id=current_id)
                case 3:
                    degree_3.add_node(value=current_user, id=current_id)
                    continue
                case degree if degree > 3:
                    break
                case _:
                    pass

            current_node = current_graph_node.connections_list.head

            while current_node is not None:
                neighbor_id = current_node.value
                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    queue.append((neighbor_id, current_degree + 1))
                current_node = current_node.next

        return degree_1, degree_2, degree_3

    def _add_node(self, user: User) -> None:
        if user.id not in self.graph_nodes:
            self.graph_nodes[user.id] = GraphNode(user)

    def _add_edge(self, user_id_a: str, user_id_b: str) -> None:
        if (
            user_id_a in self.graph_nodes
            and user_id_b in self.graph_nodes
            and user_id_a != user_id_b
        ):
            graph_node_a = self.graph_nodes[user_id_a]
            graph_node_b = self.graph_nodes[user_id_b]

            graph_node_a.connections_list.add_node(value=user_id_b, id=user_id_b)
            graph_node_b.connections_list.add_node(value=user_id_a, id=user_id_a)
