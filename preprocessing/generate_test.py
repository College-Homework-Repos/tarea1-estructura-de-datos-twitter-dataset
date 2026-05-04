import csv
import os
from os import path


def generate_test_tables(
    source_dir: str, output_subdir: str, max_rows: int = 200
) -> None:
    output_dir = path.join(source_dir, output_subdir)
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        if not filename.endswith(".csv"):
            continue

        source_path = path.join(source_dir, filename)
        target_path = path.join(output_dir, filename)

        with open(source_path, "r", newline="", encoding="utf-8") as source:
            reader = csv.reader(source)
            header = next(reader, None)
            if header is None:
                continue

            with open(target_path, "w", newline="", encoding="utf-8") as target:
                writer = csv.writer(target)
                writer.writerow(header)
                rows_written = 0
                for row in reader:
                    writer.writerow(row)
                    rows_written += 1
                    if rows_written >= max_rows:
                        break
