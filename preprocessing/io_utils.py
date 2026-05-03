import csv


def read_user_ids(users_path: str) -> list[str]:
    user_ids: list[str] = []
    with open(users_path, "r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            user_id = row.get("id")
            if user_id:
                user_ids.append(user_id)
    return user_ids


def read_edges(edges_path: str) -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()
    with open(edges_path, "r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            follower_id = row.get("follower_id")
            followee_id = row.get("followee_id")
            if follower_id and followee_id:
                edges.add((follower_id, followee_id))
    return edges


def collect_posts(posts_path: str) -> list[str]:
    post_ids: list[str] = []
    with open(posts_path, "r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            user_id = row.get("id")
            if not user_id:
                continue
            for key, value in row.items():
                if key.startswith("tweet_") and value:
                    post_ids.append(f"{user_id}_{key}")
    return post_ids
