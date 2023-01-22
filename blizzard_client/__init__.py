
from datetime import datetime
import os

import requests
from common import Auction

from db import get_access_token, save_access_token


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_secret")

region = "us"
namespace = "dynamic-us"
base_url = f"https://{region}.api.blizzard.com"
commodities_endpoint = "/data/wow/auctions/commodities"

def get_refreshed_access_token():
    (_, updated_at, access_token) = get_access_token()
    print((datetime.now() - updated_at).seconds)
    # access token valid for 24 hours
    if (datetime.now() - updated_at).seconds > 60 * 60 * 23:
        # make a request to blizzard
        data = {
            'grant_type': 'client_credentials',
        }
        response = requests.post('https://oauth.battle.net/token', data=data, auth=(client_id, client_secret))
        access_token = response.json()['access_token']
        save_access_token(access_token)
    return access_token

def get_all_auctions():
    access_token = get_refreshed_access_token()
    url = f"{base_url}{commodities_endpoint}?namespace={namespace}&locale=en_US&access_token={access_token}"
    resp = requests.get(url)

    auctions = [
        Auction(
            item_id=auction['item']['id'],
            quantity=auction['quantity'],
            price=auction['unit_price']
        )
        for auction in resp.json()['auctions']
    ]
    return auctions