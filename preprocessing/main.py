from os import path
import kagglehub

from friends import write_friends_csv
from io_utils import collect_posts, read_edges, read_user_ids
from likes import write_likes_csv

OUTPUT_DIR = "./data"
# columnas relevantes: follower_id, followee_id
FOLLOWERS_CSV = "edges.csv"
# columnas relevantes: id, tweet_1, tweet_2, ..., tweet_200
POSTS_CSV = "user_tweets.csv"
# columnas relevantes: id, name, description, followers_count, friends_count
USERS_CSV = "user_info.csv"
# archivos generados:
FRIENDS_CSV = "friends.csv"
LIKES_CSV = "likes.csv"


dataset_path = kagglehub.dataset_download(
    "sanketrai/twitter-mbti-dataset", output_dir=OUTPUT_DIR
)


def main() -> None:
    edges_path = path.join(dataset_path, FOLLOWERS_CSV)
    users_path = path.join(dataset_path, USERS_CSV)
    posts_path = path.join(dataset_path, POSTS_CSV)
    friends_output = path.join(dataset_path, FRIENDS_CSV)
    likes_output = path.join(dataset_path, LIKES_CSV)

    if path.exists(friends_output) and path.exists(likes_output):
        print("Archivos ya generados, no se vuelven a crear")
        return

    user_ids = read_user_ids(users_path)
    followers = read_edges(edges_path)
    post_ids = collect_posts(posts_path)
    friends_count = write_friends_csv(friends_output, user_ids, followers)
    likes_count = write_likes_csv(likes_output, user_ids, post_ids)

    print("Ruta al dataset:", dataset_path)
    print("Salida de amigos:", friends_output)
    print("Salida de likes:", likes_output)
    print("Filas de amigos escritas:", friends_count)
    print("Filas de likes escritas:", likes_count)


if __name__ == "__main__":
    main()
