"""Catalog Pricing Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CatalogPricingModel:
    """mapper class for Catalog Pricing object from Json Dict

    """
    id: str = None
    location_id: str = None
    price: float = None
    has_inventory_cost: bool = None
    available: bool = None

    def __init__(self, **kwargs):
        """map a dict to Catalog Pricing object

        :param kwargs: Catalog Pricing json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Catalog Pricing model

        :return: Catalog Pricing name
        """
        return f'{self.location_id}-{self.price}'
