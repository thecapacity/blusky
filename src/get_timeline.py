from atproto import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_timeline(client):
    # Get "Home" page. Use pagination (cursor + limit) to fetch all posts
    timeline = client.get_timeline(algorithm='reverse-chronological')
    for feed_view in timeline.feed:
        action = 'New Post'
        if feed_view.reason:
            action_by = feed_view.reason.by.handle
            action = f'Reposted by @{action_by}'

        post = feed_view.post.record
        author = feed_view.post.author

        yield f'[{action}] {author.display_name}: {post.text}'

if __name__ == "__main__":
    client = Client()
    client.login()
    
    print("Timeline:")

    for t in get_timeline(client):
        print(t)
