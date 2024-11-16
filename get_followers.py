from atproto import Client
import os
from dotenv import load_dotenv
from loguru import logger
from collections import defaultdict
from time import sleep
from dataclasses import dataclass
import typing
import pprint

# Meta Config
pp = pprint.PrettyPrinter(indent=4)
BSKY_USER = os.getenv("BSKY_USER")
BSKY_PWD = os.getenv("BSKY_PWD")


@dataclass
class PaginationConfig:
    """Configure for pagination results"""

    batch_size: int = 100
    rate_limit_delay: float = 0.5
    max_items: int = 1


def get_bsky_client(user: str, pwd: str):
    """
    set your env variables in your .env file (your bsky login)
    """
    load_dotenv()
    client = Client()
    profile = client.login(user, pwd)
    return profile, client


def bsky_get_follows_simple(client):
    """
    Simple method to get follows at pagination limit
    """
    follows = client.get_follows(BSKY_USER)
    follow_list = follows.follows

    for follow in follow_list:
        print(follow.did, follow.handle, follow.created_at)


def bsky_get_follows_paginated(client: Client, config=None) -> dict[str, str]:
    """
    Gets all the accounts you've followed from data via your PDS
    """
    if config is None:
        config = PaginationConfig()

    items_from_api = 0
    cursor = None
    follow_dict = defaultdict(str)

    while True:
        if items_from_api >= config.max_items:
            break

        remaining = config.max_items - items_from_api
        batch_limit = min(config.batch_size, remaining)

        # Fetch the current page
        response = client.get_follows(actor=BSKY_USER, cursor=cursor, limit=batch_limit)

        for follow in response.follows:
            follow_dict[follow.did] = {
                "handle": follow.handle,
                "created_at": follow.created_at,
            }

            items_from_api += 1

            if items_from_api >= config.max_items:
                return follow_dict

        cursor = response.cursor
        if not cursor:
            break

        sleep(config.rate_limit_delay)

    return follow_dict


def bsky_get_followers_paginated(client: Client, config=None) -> dict[str, str]:
    """
    Gets all the accounts that have followed you
    """
    if config is None:
        config = PaginationConfig()

    items_from_api = 0
    cursor = None
    follower_dict = defaultdict(str)

    while True:
        if items_from_api >= config.max_items:
            break

        remaining = config.max_items - items_from_api
        batch_limit = min(config.batch_size, remaining)

        # Fetch the current page
        response = client.get_followers(
            actor=BSKY_USER, cursor=cursor, limit=batch_limit
        )

        for follower in response.followers:
            follower_dict[follower.did] = {
                "handle": follower.handle,
                "created_at": follower.created_at,
            }

            items_from_api += 1

            if items_from_api >= config.max_items:
                return follower_dict

        cursor = response.cursor
        if not cursor:
            break

        sleep(config.rate_limit_delay)

    return follower_dict


if __name__ == "__main__":
    # login
    profile, client = get_bsky_client(BSKY_USER, BSKY_PWD)
    # confirm connection
    logger.info(f"Welcome {profile.display_name}")

    # get 100 follows, if limit=None will get all
    pp.pprint(
        bsky_get_follows_paginated(client, config=PaginationConfig(max_items=100))
    )

    # get 100 followers, if limit=None will get all
    pp.pprint(
        bsky_get_followers_paginated(client, config=PaginationConfig(max_items=100))
    )
