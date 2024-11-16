from atproto import Client, client_utils
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    USER = os.getenv('BSKY_USER')
    PWD = os.getenv('BSKY_PWD')
    
    client = Client()
    profile = client.login(USER,PWD)
    print('Welcome,', profile.display_name)

    followers = client.get_followers('vickiboykis.com')
    print(followers)


if __name__ == '__main__':
    main()