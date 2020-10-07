# Extract reddit comments that mention a certain word within time
# frame using the Pushshift api (https://github.com/pushshift/api).

import urllib.request
import json

# Pushshift endpoint for searching all subreddits for the term
# 'emacs' and return comments made between 2 and 4 days ago.
#
# 25 results are returned. This value can be change using the size
# parameter (up to 500?)
pushshift_endpoint = 'https://api.pushshift.io/reddit/search/comment/?q=emacs&after=4d&before=2d&sort=asc&'

with urllib.request.urlopen(pushshift_endpoint) as response:
    response = response.read().decode('utf-8')

obj = json.loads(response)

print(len(obj['data'])) # => 25
