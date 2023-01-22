from dataclasses import dataclass

@dataclass
class Auction:
    item_id: int
    quantity: int
    price: int
