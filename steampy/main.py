from .constants.apps import CSGO
from .engine.engine import Engine
from .market.request import ItemNameId, ItemOrdersHistogram, ItemPricing, SaleHistory

def _main():
    e = Engine()
    #print(e.request(ItemPricing(CSGO, 'Clutch Case')))
    #print(e.request(ItemNameId(CSGO, 'Clutch Case')))
    #print(e.request(ItemOrdersHistogram(176241017)))
    print(e.request(SaleHistory(CSGO, 'Clutch Case')))

if __name__ == "__main__":
    _main()