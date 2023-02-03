from common import AWAKENED_ORDER, GLOWING_TITAN_ORB, RESONANT_CRYSTAL, SOPHIC_DEVOTION, VIBRANT_SHARD
from markets.auctions import get_auction_price


_FAVORATES = (VIBRANT_SHARD, RESONANT_CRYSTAL, AWAKENED_ORDER, GLOWING_TITAN_ORB, *SOPHIC_DEVOTION)

def sophic_devotion_gph(avg_price, type):

    # 5 * vibrant shard + 4 * resonant crystal + 4 * awakened order + 4 * glowing titan orb

    # 33.6 % insp
    # 10.6 % resourcefulness
    inspiration = 0.336
    selling_price = (inspiration * avg_price[type[1]] + (1 - inspiration) * avg_price[type[0]]) * 0.95
    cost_price = (5 * avg_price[VIBRANT_SHARD] + 4 * avg_price[RESONANT_CRYSTAL] + 4 * avg_price[AWAKENED_ORDER] + 4 * avg_price[GLOWING_TITAN_ORB])
    print(selling_price, cost_price)
    profit = selling_price - cost_price
    speed = 2.7
    gph = round(profit / speed * 3600, 2)
    return gph

def sophic_devotion():
    avg_price = {}
    for item_id in _FAVORATES:
        avg_price[item_id] = get_auction_price(item_id)

    print("Gold per hour Sophic Devotion:" + str(sophic_devotion_gph(avg_price, SOPHIC_DEVOTION)))
