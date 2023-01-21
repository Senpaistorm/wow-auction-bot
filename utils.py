from collections import defaultdict

def get_top_five_auction_map(auctions, filters):
    auction_map = defaultdict(list)
    for auction in auctions:
        item_id = auction['item']['id']
        if item_id in filters:
            auction_map[item_id].append(
                (auction['unit_price'] / 10000, auction['quantity'])
            )

    for _item_id, item_auctions in auction_map.items():
        auction_map[_item_id] = sorted(
            item_auctions,
            key=lambda x:x[0]
        )[:5]

    return auction_map
