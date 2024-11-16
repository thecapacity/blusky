from atproto import Client
import os
from dotenv import load_dotenv
from loguru import logger

BSKY_USER = os.getenv("BSKY_USER")
BSKY_PWD = os.getenv("BSKY_PWD")


def get_bsky_client(user: str, pwd: str):
    load_dotenv()
    client = Client()
    profile = client.login(user, pwd)
    return profile, client


if __name__ == "__main__":
    # Login, get client session and profile
    profile, client = get_bsky_client(BSKY_USER, BSKY_PWD)
    logger.info(f"Welcome {profile.display_name}")

    # Get all followers + metadata
    followers = client.get_followers(os.getenv("BSKY_USER"))
    logger.info(followers)

    # Get all follow actions
    follows = client.get_follows(BSKY_USER)
