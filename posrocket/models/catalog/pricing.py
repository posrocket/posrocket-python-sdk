"""Catalog Pricing Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CatalogPricingModel:
    """mapper class for Catalog Pricing object from Json Dict

    """
    id: str
    location_id: str
    price: float
    cost: float
    has_inventory_cost: bool
    available: bool

    def __init__(self, id=None, location_id=None, price=None, cost=None, has_inventory_cost=None, available=None, **kwargs):
        """map a dict to Catalog Pricing object

        :param kwargs: Catalog Pricing json dict
        """
        self.id = id
        self.location_id = location_id
        self.price = price
        self.cost = cost
        self.has_inventory_cost = has_inventory_cost
        self.available = available

    def __str__(self) -> str:
        """ String representation for the Catalog Pricing model

        :return: Catalog Pricing name
        """
        return f'{self.location_id}-{self.price}'
