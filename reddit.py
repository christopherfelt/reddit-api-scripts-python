import praw
import os

from dotenv import load_dotenv
load_dotenv()

REDDIT_CLIENT = os.getenv("REDDIT_CLIENT")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")


reddit = praw.Reddit(client_id=REDDIT_CLIENT,
                     client_secret=REDDIT_SECRET,
                     user_agent=USER_AGENT)

subreddit = reddit.subreddit("metalcore")

# for post in listen_to_this:
#     print(post.url)

for submission in subreddit.hot(limit=25):
    if ("youtube" in submission.url or "youtu.be" in submission.url):
        if ("youtube" in submission.url):
            pass
            yt_split1 = submission.url.split("/")
            yt_id = yt_split1[-1].split("=")[-1]
            print(f"yt_id={yt_id}, name={submission.title}, created={submission.created}, score= {submission.score}, upvote_ratio= {submission.upvote_ratio}")
        else:
            yt_split2 = submission.url.split("/")
            yt_id = yt_split2[-1]
            print(f"yt_id={yt_id}, name={submission.title}, created={submission.created}, score= {submission.score}, upvote_ratio= {submission.upvote_ratio}")

