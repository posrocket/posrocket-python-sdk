"""Location Driver Category Python model

"""
from typing import List

from posrocket.models.location.driver import LocationDriverModel

__author__ = "Rawan Amro, Lujain Battikhi"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Rawan Amro, Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro, Lujain Battikhi"
__email__ = "Launchpad@posrocket.com"
__status__ = "Beta"


class LocationDriverCategoryModel:
    """mapper class for location driver category object from Json Dict

    """

    id: str
    name: str
    _drivers: List[LocationDriverModel]

    def __init__(self,
                 id=None,
                 name=None,
                 drivers=None,
                 **kwargs
                 ):
        """map a dict to location driver category object

        :param kwargs: location driver category json dict
        """
        self.id = id
        self.name = name
        self.drivers = drivers

    @property
    def drivers(self) -> List[LocationDriverModel]:
        """
        getter for location drivers
        :return: list of location drivers
        """
        return self._drivers

    @drivers.setter
    def drivers(self, json_drivers: List[dict]):
        """setter for location driver

        :param json_drivers: json list of location driver dicts
        :return: None
        """
        self._drivers = []
        for json_driver in json_drivers or []:
            self._drivers.append(LocationDriverModel(**json_driver))
