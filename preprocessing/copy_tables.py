import csv
import os
from os import path
from itertools import islice


def copy_tables_with_less_rows(
    source_dir: str,
    output_subdir: str,
    max_rows: int = 200,
    user_tweets_limit: int = 200,
) -> None:
    output_dir = path.join(source_dir, output_subdir)
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        if not filename.endswith(".csv"):
            continue

        source_file_path = path.join(source_dir, filename)
        output_file_path = path.join(output_dir, filename)

        if filename == "user_tweets.csv":
            _copy_user_tweets_table(
                source_file_path,
                output_file_path,
                max_rows,
                user_tweets_limit,
            )
        else:
            _copy_normal_table(source_file_path, output_file_path, max_rows)


def _copy_normal_table(
    source_file_path: str, output_file_path: str, max_rows: int
) -> None:
    with open(source_file_path, "r", newline="", encoding="utf-8") as source:
        reader = csv.reader(source)
        header = next(reader, None)
        if header is None:
            return

        with open(output_file_path, "w", newline="", encoding="utf-8") as target:
            writer = csv.writer(target)
            writer.writerow(header)
            writer.writerows(islice(reader, max_rows))


def _copy_user_tweets_table(
    source_path: str,
    tweets_path: str,
    max_rows: int,
    user_tweets_limit: int,
) -> None:
    with open(source_path, "r", newline="", encoding="utf-8") as source:
        reader = csv.reader(source)
        header = next(reader, None)
        if header is None:
            return

        max_columns = 1 + user_tweets_limit
        header = header[:max_columns]

        with open(tweets_path, "w", newline="", encoding="utf-8") as target:
            writer = csv.writer(target)
            writer.writerow(header)
            for row in islice(reader, max_rows):
                writer.writerow(row[:max_columns])
