"""Inventory Trackable Python model

"""

__author__ = "Lujain Battiki, Rawan Amro"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Lujain Battiki, Rawan Amro"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Lujain Battiki, Rawan Amro"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"


class InventoryTrackableModel:
    """mapper class for Inventory Trackable object from Json Dict

    """
    id: str
    name: str
    type: str
    unit: str
    cost_per_unit: str

    def __init__(self, id=None, name=None, type=None, unit=None, cost_per_unit=None,
                 **kwargs):
        """map a dict to Inventory Trackable object

        :param kwargs: Inventory Trackable json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.unit = unit
        self.cost_per_unit = cost_per_unit

    def __str__(self) -> str:
        """ String representation for the Inventory Trackable model

        :return: Inventory Trackable name
        """
        return f'{self.name}'
