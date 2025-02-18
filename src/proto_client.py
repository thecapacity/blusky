from atproto import Client
import os
from dotenv import load_dotenv

class ProtoClient():

    """
    Authenticates to Bluesky using your logins from .env as env var
    """

    def __init__(self):
        load_dotenv()
        self.client = None
        self.profile = None
        
    def get_bsky_client(self):
        """
        set your env variables in your .env file (your bsky login)
        """
        client = Client()
        profile = client.login(os.getenv("BSKY_USER"), os.getenv("BSKY_PWD"))
        return profile, client