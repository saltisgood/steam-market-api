from steampy.config.config import DEFAULT_COUNTRY, DEFAULT_CURRENCY, DEFAULT_LANGUAGE
from steampy.constants.currency import CURRENCY_CODE_MAP
from .response import ItemNameIdResponse, ItemOrdersHistogramResponse, ItemPricingResponse, SalesHistoryResponse

# Translates a name into an ID
class ItemNameId:
    BASE_URL = 'https://steamcommunity.com/market/listings/{appid}/{item}'

    def __init__(self, appid, item_name):
        self.appid = appid
        self.item_name = item_name
    
    def get_url(self):
        return self.BASE_URL.format(appid=self.appid, item=self.item_name)
    
    def response(self, resp):
        return ItemNameIdResponse(resp)

# Gets the current orderbook for an item
class ItemOrdersHistogram:
    BASE_URL = 'https://steamcommunity.com/market/itemordershistogram?country={country}&language={language}&currency={currency}&item_nameid={item_nameid}&two_factor=0'

    def __init__(self, item_nameid):
        self.country = DEFAULT_COUNTRY
        self.currency = CURRENCY_CODE_MAP[DEFAULT_CURRENCY]
        self.language = DEFAULT_LANGUAGE
        self.item_nameid = item_nameid

    def get_url(self):
        return self.BASE_URL.format(country=self.country, language=self.language, currency=self.currency, item_nameid=self.item_nameid)

    def response(self, resp):
        return ItemOrdersHistogramResponse(resp)

# Gets volume and price overview
class ItemPricing:
    BASE_URL = 'https://steamcommunity.com/market/priceoverview/?appid={appid}&currency={currency}&market_hash_name={item}'

    def __init__(self, appid, item_name):
        self.appid = appid
        self.currency = CURRENCY_CODE_MAP[DEFAULT_CURRENCY]
        self.item_name = item_name
    
    def get_url(self):
        return self.BASE_URL.format(appid=self.appid, currency=self.currency, item=self.item_name)
    
    def response(self, resp):
        return ItemPricingResponse(resp)

# Gets the median sales prices of an item
class SaleHistory:
    BASE_URL = 'https://steamcommunity.com/market/listings/{appid}/{item}'

    def __init__(self, appid, item_name):
        self.appid = appid
        self.item_name = item_name
    
    def get_url(self):
        return self.BASE_URL.format(appid=self.appid, item=self.item_name)
    
    def response(self, resp):
        return SalesHistoryResponse(resp)
