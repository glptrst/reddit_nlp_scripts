import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent)
                     # log in with password and user if you need more than reading data
                     # password=config.password
                     # username=config.username)

print(reddit.read_only)

subreddit = reddit.subreddit("emacs")

for submission in subreddit.hot(limit=10):
    print('\ntitle: ' + submission.title)  # Output: the submission's title
    print('score: ' + str(submission.score))  # Output: the submission's score
    print('id: ' + submission.id)     # Output: the submission's ID
    print('url: ' + submission.url)    # Output: the URL the submission points to
                                       # or the submission's URL if it's a self post


