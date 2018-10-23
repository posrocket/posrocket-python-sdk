class PricingMixin:
    def get_price_for_location(self, location_id):
        for pricing in self._pricing:
            if pricing.location_id == location_id:
                return pricing.price

    @property
    def lowest_price(self):
        low = None
        for pricing in self._pricing:
            if not low or pricing.price < low:
                low = pricing.price
        return low

    @property
    def highest_price(self):
        low = None
        for pricing in self._pricing:
            if not low or pricing.price < low:
                low = pricing.price
        return low
