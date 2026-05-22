import csv
import random


# Crea la tabla de likes. Por cada cada id post toma entre 0 a 3 id de usuarios como "likes".
def write_likes_csv(
    output_path: str,
    user_ids: list[str],
    post_ids: list[str],
    max_likes_per_post: int = 3,
) -> int:
    rows_written = 0
    # creamos el archivo csv "likes.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["post_id", "likes"])
        # Por cada id post toma entre 0 a 3 id de usuarios como "likes".
        for post_id in post_ids:
            if not user_ids:
                break
            likes_count = random.randint(0, max_likes_per_post)
            sample_size = min(likes_count, len(user_ids))
            if sample_size == 0:
                writer.writerow([post_id, ""])
                rows_written += 1
                continue
            # Tomamos de 0 a 3 id de usuarios
            chosen = set(random.sample(user_ids, sample_size))
            ordered_likes = [user_id for user_id in user_ids if user_id in chosen]
            # Agregamos el id del post y una lista de los id de usuarios que le dieron like separados por ";"
            writer.writerow([post_id, ";".join(ordered_likes)])
            rows_written += 1
    return rows_written
