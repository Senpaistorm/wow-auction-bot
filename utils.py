from collections import defaultdict

def get_top_five_auction_map(auctions, filters):
    auction_map = defaultdict(list)
    for auction in auctions:
        item_id = auction.item_id
        if item_id in filters:
            auction_map[item_id].append(
                (auction.price / 10000, auction.quantity)
            )

    for _item_id, item_auctions in auction_map.items():
        auction_map[_item_id] = sorted(
            item_auctions,
            key=lambda x:x[0]
        )[:5]

    avg_price = {}
    for item_id, prices in auction_map.items():
        sum = 0
        total_quantity = 0
        for price, quantity in prices:
            sum += price * quantity
            total_quantity += quantity
        avg_price[item_id] = sum / total_quantity

    print(avg_price)

    return avg_price

