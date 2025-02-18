import os
from atproto import Client, client_utils
from dotenv import load_dotenv

load_dotenv()

def main():
    client = Client()
    profile = client.login(os.getenv('BSKY_USER'), os.getenv('BSKY_PWD'))
    print('Welcome,', profile.display_name)
    
if __name__ == '__main__':
    client = main()
