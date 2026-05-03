import csv


def write_friends_csv(
    output_path: str, user_ids: list[str], edges: set[tuple[str, str]]
) -> int:
    friends_map: dict[str, set[str]] = {user_id: set() for user_id in user_ids}
    for follower_id, followee_id in edges:
        if follower_id == followee_id:
            continue
        if (followee_id, follower_id) in edges:
            friends_map[follower_id].add(followee_id)
            friends_map[followee_id].add(follower_id)

    rows_written = 0
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["user_id", "friends"])
        for user_id in user_ids:
            friends = sorted(friends_map.get(user_id, set()))
            friends_text = ";".join(friends)
            writer.writerow([user_id, friends_text])
            rows_written += 1
    return rows_written
