from topsdk.ability338.ability338 import Ability338
from topsdk.ability338.request.aliexpress_ds_product_get_request import *

from topsdk.client import TopApiClient, TopException


class AliexpressDsProductGetRequest:
    pass


if __name__ == '__main__':
    # create Client
    client = TopApiClient(appkey='34173206', app_sercet='a0d5286213b1b65b06c3c2ec2f30681c', top_gateway_url='http://api.taobao.com/router/rest',verify_ssl=False)
    ability = Ability338(client=client)

    # create domain

    # create request
    request = AliexpressDsProductGetRequest()
    request.ship_to_country = 'US'
    request.product_id = 32982857990
    request.target_currency = 'USD'
    request.target_language = 'EN'
    try:
        response = ability.aliexpress_ds_product_get(request, '<user session>')
        print(response)
    except TopException as e:
        print(e)