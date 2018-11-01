"""Location Tab Pickup Python model

"""
from datetime import date

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabPickupModel:
    """ mapper class for Location Tab Pickup object from Json Dict

    """
    id: str = None
    eta: date = None
    company: str = None
    driver_name: str = None
    driver_phone: int = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Tab Pickup object

        :param kwargs: Location Tab Pickup json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Pickup model

        :return: Directory Location Tab Pickup name
        """
        return f'{self.driver_name}'
