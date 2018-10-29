"""Location Drawer Creator Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationDrawerCreatorModel:
    """ mapper class for Location Drawer Creator object from Json Dict

    """
    id: str = None
    first_name: str = None
    last_name: str = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Drawer Creator object

        :param kwargs: Location Drawer Creator json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Drawer Creator model

        :return: Directory Location Drawer Creator reference
        """
        return f'{self.first_name} {self.last_name}'
