from datetime import datetime

from blizzard_client import get_all_auctions
from common import FAVORITES
from utils import get_top_five_auction_map
from db import save_auctions, get_auction

def refresh_favorite_auctions():
    all_auctions = get_all_auctions()
    auction_map = get_top_five_auction_map(all_auctions, FAVORITES)
    save_auctions(auction_map)

def get_auction_price(item_id):
    updated_at, avg_price = get_auction(item_id)
    if not updated_at or (datetime.now() - updated_at).seconds > 3600:
        refresh_favorite_auctions()
        updated_at, avg_price = get_auction(item_id)

    return avg_price
