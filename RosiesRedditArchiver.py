import praw
from praw.models.reddit.submission import Submission 
from praw.models.reddit.comment import Comment

from pprint import pprint

from sys import argv

def explore(obj):
    pprint(vars(obj))

print("Connecting to reddit")
reddit = praw.Reddit('RosiesRedditArchiver')
print("Full user account access: ", not reddit.read_only)

saved_items=[]
print("Saved Items:")
for item in reddit.redditor('krlanguet').saved(
	limit=None if len(argv) <=1 else int(argv[1])
):
    print(" * ", end='')
    if isinstance(item, Submission):
        print("Post \"%s\" in %s" % (item.title, item.subreddit._path))
    elif isinstance(item, Comment):
        print('Comment by /u/%s in %s' % (item.author.name, item.subreddit._path))
    else:
        print('Unrecognized type:', item.type)
    saved_items.append(item)
