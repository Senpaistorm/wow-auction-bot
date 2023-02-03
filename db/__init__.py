import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="xiangli",
        password="",
        database="mydatabase"
    )
    return db

def create_db():
    db = mysql.connector.connect(
        host="localhost",
        user="xiangli",
        password="",
    )
    cur = db.cursor()
    cur.execute("CREATE DATABASE mydatabase")

db = connect_db()
if not db:
    create_db()
    db = connect_db()
cursor = db.cursor(buffered=True)
cursor.reset()

cursor.execute("CREATE TABLE IF NOT EXISTS access_token (id TINYINT, updated_at DATETIME(0), access_token VARCHAR(255), PRIMARY KEY (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS auction_price (id INT(11), updated_at DATETIME(0), avg_price FLOAT(2), PRIMARY KEY (id))")

def save_access_token(access_token):
    sql = ("""
        INSERT INTO access_token
            (id, updated_at, access_token)
            values
            (1, current_timestamp, %s)
        ON DUPLICATE KEY UPDATE
            updated_at = VALUES(updated_at), access_token = VALUES(access_token)
    """)
    cursor.execute(sql, (access_token,))
    db.commit()

def get_access_token():
    cursor.execute("""
        select * from access_token
    """)
    result = cursor.fetchone()
    return result


def save_auctions(auction_map):
    sql = ("""
        INSERT INTO auction_price
            (id, updated_at, avg_price)
            values
            (%s, current_timestamp, %s)
        ON DUPLICATE KEY UPDATE
            updated_at = VALUES(updated_at), avg_price = VALUES(avg_price)
    """)
    values = [(k, v) for k, v in auction_map.items()]
    cursor.executemany(sql, values)
    db.commit()

def get_auction(item_id):
    sql = ("""
        select updated_at, avg_price from auction_price
        where id = %s
    """)
    cursor.execute(sql, (item_id,))
    result = cursor.fetchone()
    if not result:
        return None, None
    return result
