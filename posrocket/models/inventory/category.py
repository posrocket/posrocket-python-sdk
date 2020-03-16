"""Inventory Category Python model

"""

__author__ = "Lujain Battiki, Rawan Amro"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Lujain Battiki, Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lujain Battiki, Rawan Amro"
__email__ = "Lanuchpad@posrocket.com"
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
