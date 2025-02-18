from atproto import Client
import os
from dotenv import load_dotenv

class ProtoClient():

    """
    Authenticates to Bluesky using your logins from .env as env var
    """

    def __init__(self):


    def get_bsky_client(self):
        """
        set your env variables in your .env file (your bsky login)
        """
        load_dotenv()
        client = Client()
        profile = client.login(self.user, self.pwd)
        return profile, client