import praw
from praw.models.reddit.submission import Submission 
from praw.models.reddit.comment import Comment 
from pprint import pprint as prnt

reddit = praw.Reddit('RosiesRedditArchiver')
print("Full user account access: ", not reddit.read_only)

print("Saved Items:")
for item in reddit.redditor('krlanguet').saved(limit=20):
    print(" * ", end='')
    if isinstance(item, Submission):
        print("Post title:", item.title)
    elif isinstance(item, Comment):
        print('Comment by:', item.author.name)
    else:
        print('Unrecognized type:', item.type)
