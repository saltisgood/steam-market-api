from steampy.config.config import DEFAULT_CURRENCY

from decimal import Decimal, ROUND_DOWN

STEAM_PREFIXES = {
    'A$ ': 'AUD',
}

CURRENCY_PREFIX = {
    'AUD': 'A$',
    'USD': '$'
}

class Price:
    @staticmethod
    def parse(price):
        for pfx in STEAM_PREFIXES:
            if price.startswith(pfx):
                return Price(price[len(pfx):], STEAM_PREFIXES[pfx])
        raise NotImplementedError()

    def __init__(self, value, currency=None):
        self._value = Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        if currency:
            self._currency = currency
        else:
            self._currency = DEFAULT_CURRENCY
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
    
    @property
    def currency(self):
        return self._currency
    
    def __str__(self):
        pfx = CURRENCY_PREFIX[self.currency]
        return '{}{}'.format(pfx, self.value)