"""Location Driver Python model

"""
from typing import List

from posrocket.models.location.driver_category import LocationDriverCategoryModel

__author__ = "Rawan Amro, Lujain Battikhi"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Rawan Amro, Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro, Lujain Battikhi"
__email__ = "Launchpad@posrocket.com"
__status__ = "Beta"


class LocationDriverModel:
    """mapper class for location driver object from Json Dict

    """

    id: str
    name: str
    _driver_categories: List[LocationDriverCategoryModel]

    def __init__(self,
                 id=None,
                 name=None,
                 driver_categories=None,
                 **kwargs
                 ):
        """map a dict to location driver object

        :param kwargs: location driver json dict
        """
        self.id = id
        self.name = name
        self.driver_categories = driver_categories

    @property
    def driver_categories(self) -> List[LocationDriverCategoryModel]:
        """
        getter for location driver categories
        :return: list of location driver categories
        """
        return self._driver_categories

    @driver_categories.setter
    def driver_categories(self, json_driver_categories: List[dict]):
        """setter for location driver categories

        :param json_driver_categories: json list of location driver categories dicts
        :return: None
        """
        self._driver_categories = []
        for json_driver_category in json_driver_categories or []:
            self._driver_categories.append(LocationDriverCategoryModel(**json_driver_category))
