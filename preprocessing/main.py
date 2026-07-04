from os import path
import kagglehub

from generate_friends import write_friends_csv
from io_utils import get_posts_ids, get_both_followers_ids, get_user_ids
from generate_likes import write_likes_csv
from copy_tables import copy_tables_with_less_rows

OUTPUT_DIR = "./data"
# columnas relevantes: follower_id, followee_id
FOLLOWERS_CSV = OUTPUT_DIR + "/edges.csv"
# columnas relevantes: id, tweet_1, tweet_2, ..., tweet_200
POSTS_CSV = OUTPUT_DIR + "/user_tweets.csv"
# columnas relevantes: id, name, description, followers_count, friends_count
USERS_CSV = OUTPUT_DIR + "/user_info.csv"
# archivos generados:
FRIENDS_CSV = OUTPUT_DIR + "/friends.csv"
LIKES_CSV = OUTPUT_DIR + "/likes.csv"


dataset_path = kagglehub.dataset_download(
    "sanketrai/twitter-mbti-dataset", output_dir=OUTPUT_DIR
)


def main() -> None:
    if path.exists(FRIENDS_CSV) and path.exists(LIKES_CSV):
        print("Archivos ya generados, no se vuelven a crear")
        return None

    user_ids = get_user_ids(USERS_CSV)
    both_followers_ids = get_both_followers_ids(FOLLOWERS_CSV)
    post_ids = get_posts_ids(POSTS_CSV)

    friends_count = write_friends_csv(FRIENDS_CSV, user_ids, both_followers_ids)
    likes_count = write_likes_csv(LIKES_CSV, user_ids, post_ids)

    print("Ruta al dataset:", dataset_path)
    print("Salida de amigos:", FRIENDS_CSV)
    print("Salida de likes:", LIKES_CSV)
    print("Filas de amigos escritas:", friends_count)
    print("Filas de likes escritas:", likes_count)

    copy_tables_with_less_rows(
        source_dir=dataset_path,
        output_subdir="less_data",
        max_rows=1500,
        user_tweets_limit=50,
    )
    copy_tables_with_less_rows(
        source_dir=dataset_path,
        output_subdir="release_data",
        max_rows=5000,
        user_tweets_limit=100,
    )


if __name__ == "__main__":
    main()
