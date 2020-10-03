#
# Extract comments from submission in json format.
#

import json
import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent)

url = 'https://www.reddit.com/r/emacs/comments/j333eb/how_to_have_helmlike_quick_help_persistent_action/'
submission = reddit.submission(url=url)

submission.comments.replace_more(limit=None)

def comment_extract(comment):
    """Take a comment praw object.  Return dictionary representing comment
    recursively unpacked (with replies, replies to replies, etc.).

    Only author, body, and replies are preserved.

    """
    if comment.replies:
        c = {
            'author': comment.author.name if comment.author else 'none?',
            'body': comment.body,
            'replies': []
        }
        for r in comment.replies:
            c['replies'].append(comment_extract(r))
        return c
    else:
        return {
            'author': comment.author.name,
            'body': comment.body,
            'replies': []
        }

unpacked_comments = []
for comment in submission.comments:
    unpacked_comments.append(comment_extract(comment))

# Save submission in json format
sub = {
    'author': submission.author.name,
    'title': submission.title,
    'text': submission.selftext,
    'comments': unpacked_comments
}

with open('./unpacked.json', 'w') as f:
    json.dump(sub, f, indent=4)
