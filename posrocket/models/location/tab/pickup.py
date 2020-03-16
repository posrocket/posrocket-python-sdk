"""Location Tab Pickup Python model

"""
from datetime import date

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabPickupModel:
    """ mapper class for Location Tab Pickup object from Json Dict

    """
    id: str
    eta: date
    company: str
    driver_name: str
    driver_phone: int

    def __init__(self,
                 id=None,
                 eta=None,
                 company=None,
                 driver_name=None,
                 driver_phone=None,
                 **kwargs
                 ):
        """ map a dict to Location Tab Pickup object

        :param kwargs: Location Tab Pickup json dict
        """
        self.id = id
        self.eta = eta
        self.company = company
        self.driver_name = driver_name
        self.driver_phone = driver_phone

    def __str__(self) -> str:
        """ String representation for the Location Pickup model

        :return: Directory Location Tab Pickup name
        """
        return f'{self.driver_name}'
