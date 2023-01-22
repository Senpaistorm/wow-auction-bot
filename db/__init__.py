import sqlite3
from common import Auction
con = sqlite3.connect("auctions.db")

cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master").fetchone()
if 'auctions' not in res:
    cur.execute("CREATE TABLE auctions(id, quantity, price, updated_at)")

cur.execute("""
    INSERT INTO auctions VALUES
        (1, 'test name', 8.2)
    """
)

res = cur.execute("SELECT * FROM auctions").fetchall()
print(res)

def get_last_updated_at():
    pass

def save_auctions(auctions):
    data = [
        (auction.item_id, auction.quantity, auction.price)
        for auction in auctions
    ]
    cur.executemany("INSERT INTO auctions VALUES(?, ?, ?, current_timestamp)", data)
    con.commit()  # Remember to commit the transaction after executing INSERT.