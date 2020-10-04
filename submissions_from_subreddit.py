import json
from reddit_extract import comment_extract
from reddit_extract import submission_extract
from reddit_extract import get_subreddit

emacs_subreddit = get_subreddit('emacs')

submissions = []

# Get 50 hot emacs submissions
for sub in emacs_subreddit.hot(limit=50):
    submissions.append(submission_extract(sub.id))

with open('./hot_emacs_submissions.json', 'w') as f:
    json.dump(submissions, f, indent=4)
    
# TODO:
# - how to get ALL emacs' (or any other subreddit) submissions?
# - how to get ALL emacs' submissions within a time interval?
