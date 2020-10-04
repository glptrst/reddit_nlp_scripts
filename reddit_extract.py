import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent)

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

def submission_extract(submission_id):
    submission = reddit.submission(id=submission_id)
    submission.comments.replace_more(limit=None)

    unpacked_comments = []

    for comment in submission.comments:
        unpacked_comments.append(comment_extract(comment))

    sub = {
        'author': submission.author.name,
        'title': submission.title,
        'text': submission.selftext,
        'comments': unpacked_comments
    }

    return sub

def get_subreddit(name):
    return reddit.subreddit(name)
