"""Inventory Category Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class InventoryCategoryModel:
    """mapper class for Inventory Category object from Json Dict

    """
    id: str
    name: str
    trackables_count: float

    def __init__(self, id=None, name=None, trackables_count=None, **kwargs):
        """map a dict to Inventory Category object

        :param kwargs: Inventory Category json dict
        """
        self.id = id
        self.name = name
        self.trackables_count = trackables_count

    def __str__(self) -> str:
        """ String representation for the Inventory Category model

        :return: Inventory Category name
        """
        return f'{self.name}'
