"""delivery Python model

"""

from posrocket.models.driver import DriverModel
from posrocket.models.driver_category import DriverCategoryModel

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
    status: int
    _category: DriverCategoryModel
    _driver: DriverModel

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
    def category(self) -> DriverCategoryModel:
        """getter for  Driver Category

        :return: Drivers Category object
        """
        return self._category

    @category.setter
    def category(self, category):
        """setter for  driver category

        :param: category:json driver category
        :return: None
        """

    @property
    def driver(self) -> DriverModel:
        """getter for Driver

        :return: list of driver
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """setter for driver

        :param driver:json of driver
        :return: None
        """
