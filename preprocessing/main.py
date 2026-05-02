import kagglehub

# columnas relevantes: follower_id, followee_id
FOLLOWERS_CSV = "edges.csv"
# columnas relevantes: id, tweet_1, tweet_2, ..., tweet_200
POSTS_CSV = "user_tweets.csv"
# columnas relevantes: id, name, description, followers_count, friends_count
USERS_CSV = "user_info.csv"

# C:\Users\tkdgi\.cache\kagglehub\datasets\sanketrai\twitter-mbti-dataset\versions\2
dataset_path = kagglehub.dataset_download(
    "sanketrai/twitter-mbti-dataset", output_dir="./data"
)
print("Path to dataset files:", dataset_path)
