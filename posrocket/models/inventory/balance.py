"""Inventory Balance Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class InventoryBalanceModel:
    """mapper class for Inventory Balance object from Json Dict

    """
    id: str
    location_id: str
    quantity: float
    cost_per_unit: float
    cost: float
    threshold: float
    tracking: bool

    def __init__(self, id=None, location_id=None, quantity=None, cost_per_unit=None, cost=None, threshold=None,
                 tracking=None, **kwargs):
        """map a dict to Inventory Balance object

        :param kwargs: Inventory Balance json dict
        """
        self.id = id
        self.location_id = location_id
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit
        self.cost = cost
        self.threshold = threshold
        self.tracking = tracking

    def __str__(self) -> str:
        """ String representation for the Inventory Balance model

        :return: Inventory Balance name
        """
        return f'{self.location_id}'
