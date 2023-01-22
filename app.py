from blizzard_client import get_all_auctions
from common import FAVORITES
from markets.chilled_rune import chilled_rune
from utils import get_top_five_auction_map

def refresh_favorite_auctions():
    all_auctions = get_all_auctions()
    auction_map = get_top_five_auction_map(all_auctions, FAVORITES)

if __name__ == "__main__":
    chilled_rune()