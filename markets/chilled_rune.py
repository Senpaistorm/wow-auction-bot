
from common import BUZZING_RUNE, CHILLED_RUNE, HOWLING_RUNE
from markets.auctions import get_auction_price


def fauna_rune_profit(avg_price, type):
    selling_price = (1.67 * avg_price[type[1]] + 0.64 * avg_price[type[0]]) * 0.95

    profit = selling_price - avg_price[CHILLED_RUNE[0]]
    speed = 1
    gph = round(profit / speed * 3600, 2)
    return gph

def chilled_rune():
    avg_price = {}
    for item_id in CHILLED_RUNE + HOWLING_RUNE + BUZZING_RUNE:
        avg_price[item_id] = get_auction_price(item_id)

    print("Gold per hour Howling Rune:" + str(fauna_rune_profit(avg_price, HOWLING_RUNE)))
    print("Gold per hour Buzzing Rune:" + str(fauna_rune_profit(avg_price, BUZZING_RUNE)))
