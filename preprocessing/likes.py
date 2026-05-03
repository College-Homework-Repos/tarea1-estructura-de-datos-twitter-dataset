import csv
import random


def write_likes_csv(output_path: str, user_ids: list[str], post_ids: list[str]) -> int:
    rows_written = 0
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["user_id", "post_id"])
        for post_id in post_ids:
            if not user_ids:
                break
            likes_count = random.randint(0, 40)
            sample_size = min(likes_count, len(user_ids))
            if sample_size == 0:
                continue
            for user_id in random.sample(user_ids, sample_size):
                writer.writerow([user_id, post_id])
                rows_written += 1
    return rows_written
