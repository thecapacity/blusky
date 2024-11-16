from atproto import Client, client_utils
import os
from dotenv import load_dotenv

def get_bsky_client():
    load_dotenv()
    client = Client()
    client.login(os.getenv('BSKY_USER'), os.getenv('BSKY_PWD'))
    return client


if __name__ == '__main__':
    client = get_bsky_client()
    print('Welcome,', client.me.display_name)
    followers = client.get_followers('vickiboykis.com')
    print(followers)