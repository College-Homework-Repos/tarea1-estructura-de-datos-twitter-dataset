import kagglehub

FOLLOWERS_CSV = "edges.csv"  # follower_id, followee_id
POSTS_CSV = "user_tweets.csv"  # id, tweet_1, tweet_2, ..., tweet_
USERS_CSV = "user_info.csv"  # id, name, description, followers_count, friends_count


dataset_path = kagglehub.dataset_download("sanketrai/twitter-mbti-dataset")
print("Path to dataset files:", dataset_path)
