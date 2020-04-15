"""delivery Python model

"""

from posrocket.models.driver import LocationDriverModel
from posrocket.models.driver_category import LocationDriverCategoryModel

__author__ = "Rawan Amro, Lujain Battikhi"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Rawan Amro, Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro, Lujain Battikhi"
__email__ = "Launchpad@posrocket.com"
__status__ = "Beta"


class DeliveryModel:
    """ mapper class for Delivery object from Json Dict

    """
    id: str
    ride_id: str
    status: str
    _category: LocationDriverCategoryModel
    _driver: LocationDriverModel

    def __init__(self,
                 id=None,
                 ride_id=None,
                 status=None,
                 category=None,
                 driver=None,
                 **kwargs
                 ):
        """ map a dict to delivery object

        :param kwargs: delivery json  dict
        """
        self.id = id
        self.ride_id = ride_id
        self.status = status
        self.category = category
        self.driver = driver

    @property
    def category(self) -> LocationDriverCategoryModel:
        """getter for location driver Category

        :return: Drivers Category object
        """
        return self._category

    @category.setter
    def category(self, json_category: dict):
        """setter for location driver category

        :param: json_category:json driver category
        :return: None
        """
        if json_category:
            self._category = LocationDriverCategoryModel(**json_category)
        else:
            self._category = None

    @property
    def driver(self) -> LocationDriverModel:
        """getter for location driver

        :return: list of driver
        """
        return self._driver

    @driver.setter
    def driver(self, json_driver):
        """setter for location driver

        :param json_driver:json of driver
        :return: None
        """
        if json_driver:
            self._driver = LocationDriverCategoryModel(**json_driver)
        else:
            self._driver = None
