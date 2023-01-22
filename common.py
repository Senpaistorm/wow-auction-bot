from dataclasses import dataclass

CHILLED_RUNE = (194767, 194768)
HOWLING_RUNE = (194819, 194820)
BUZZING_RUNE = (194822, 194823)

FAVORITES = CHILLED_RUNE + HOWLING_RUNE + BUZZING_RUNE

@dataclass
class Auction:
    item_id: int
    quantity: int
    price: int
