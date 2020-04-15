"""Driver Python model

"""
from typing import List

from posrocket.models.driver_category import DriverCategoryModel

__author__ = "Rawan Amro, Lujain Battikhi"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Rawan Amro, Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro, Lujain Battikhi"
__email__ = "Launchpad@posrocket.com"
__status__ = "Beta"


class DriverModel:
    """mapper class for Driver object from Json Dict

    """

    id: str
    name: str
    _driver_categories: List[DriverCategoryModel]

    def __init__(self,
                 id=None,
                 name=None,
                 driver_categories=None,
                 **kwargs
                 ):
        """map a dict to Driver object

        :param kwargs: Driver json dict
        """
        self.id = id
        self.name = name
        self.driver_categories = driver_categories
