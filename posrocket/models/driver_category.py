"""Driver Category Python model

"""
from typing import List

from posrocket.models.driver import DriverModel

__author__ = "Rawan Amro, Lujain Battikhi"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Rawan Amro, Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro, Lujain Battikhi"
__email__ = "Launchpad@posrocket.com"
__status__ = "Beta"


class DriverCategoryModel:
    """mapper class for Driver Category object from Json Dict

    """

    id: str
    name: str
    _drivers: List[DriverModel]

    def __init__(self,
                 id=None,
                 name=None,
                 drivers=None,
                 **kwargs
                 ):
        """map a dict to Driver Category object

        :param kwargs: Driver categories json dict
        """
        self.id = id
        self.name = name
        self.drivers = drivers
