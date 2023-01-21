import requests
from utils import get_top_five_auction_map

access_token = "USmsgQH1KknMiHHTzjzrl9X5mqoGDN26zq" # valid for 24 hours
region = "us"
namespace = "dynamic-us"
base_url = f"https://{region}.api.blizzard.com"
commodities_endpoint = "/data/wow/auctions/commodities"


def get_all_auctions():
    url = f"{base_url}{commodities_endpoint}?namespace={namespace}&locale=en_US&access_token={access_token}"
    resp = requests.get(url)
    return resp.json()['auctions']

ALL_AUCTIONS = get_all_auctions()

CHILLED_RUNE = (194767, 194768)
HOWLING_RUNE = (194819, 194820)
BUZZING_RUNE = (194822, 194823)

def fauna_rune_profit(avg_price, type):
    selling_price = (1.67 * avg_price[type[1]] + 0.64 * avg_price[type[0]]) * 0.95

    profit = selling_price - avg_price[CHILLED_RUNE[0]]
    speed = 1
    gph = round(profit / speed * 3600, 2)
    return gph

def chilled_rune():
    auction_map = get_top_five_auction_map(
        ALL_AUCTIONS, 
        CHILLED_RUNE + HOWLING_RUNE + BUZZING_RUNE
    )

    avg_price = {}
    for item_id, prices in auction_map.items():
        sum = 0
        total_quantity = 0
        for price, quantity in prices:
            sum += price * quantity
            total_quantity += quantity
        avg_price[item_id] = sum / total_quantity

    print(avg_price)

    print("Gold per hour Howling Rune:" + str(fauna_rune_profit(avg_price, HOWLING_RUNE)))
    print("Gold per hour Buzzing Rune:" + str(fauna_rune_profit(avg_price, BUZZING_RUNE)))


if __name__ == "__main__":
    chilled_rune()
