import csv


# Crea la tabla de amigos, a partir de la tabla de seguidores "edges.csv" tomando como "amigos" a aquellos usuarios que se siguen mutuamente.
def write_friends_csv(
    output_path: str, user_ids: list[str], followers: set[tuple[str, str]]
) -> int:

    friends_dict: dict[str, set[str]] = {user_id: set() for user_id in user_ids}
    for follower_id, followee_id in followers:
        if follower_id == followee_id:
            continue
        if (followee_id, follower_id) in followers:
            friends_dict[follower_id].add(followee_id)
            friends_dict[followee_id].add(follower_id)

    rows_written = 0
    # creamos el archivo csv "friends.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["user_id", "friends"])
        for user_id in user_ids:
            friends = friends_dict.get(user_id, set())
            friends_text = ";".join(friends)
            # Agregamos el id usuario y una lista de los id de sus amigos separados por ";"
            writer.writerow([user_id, friends_text])
            rows_written += 1
    return rows_written
