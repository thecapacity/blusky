from atproto import  CAR, CID

from loguru import logger
from collections import defaultdict
from time import sleep
from dataclasses import dataclass
from proto_client import ProtoClient



def get_car_root(client)->CID:
    """
    gets signed hash root of PDS (https://atproto.com/guides/data-repos#data-layout)
    ┌────────────────┐
    │     Commit     │  (Signed Root)
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │   Tree Nodes   │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │     Record     │
    └────────────────┘
    """
    repo = client.com.atproto.sync.get_repo({'did': client.me.did})
    car_file = CAR.from_bytes(repo)
    return car_file.root

def get_car_blocks(client)->dict:
    """
    Get all blocks from CAR file
    """
    repo = client.com.atproto.sync.get_repo({'did': client.me.did})
    car_file = CAR.from_bytes(repo)
    return car_file.blocks



if __name__=="__main__":
    profile, client = ProtoClient().get_bsky_client()

    # Get all CAR blocks
    blocks = get_car_blocks(client)

    # Get first two elements and introspect
    print(list(blocks.items())[0:2])

    
    