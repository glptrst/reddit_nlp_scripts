#
# Extract comments from submission
#

import json
from reddit_extract import comment_extract
from reddit_extract import submission_extract

submission_id = 'j4aykc'

submission_unpacked = submission_extract(submission_id)

# Save submission in json format
with open('./unpacked.json', 'w') as f:
    json.dump(submission_unpacked, f, indent=4)

