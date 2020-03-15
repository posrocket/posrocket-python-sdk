"""Location Drawer Creator Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationDrawerCreatorModel:
    """ mapper class for Location Drawer Creator object from Json Dict

    """
    id: str
    first_name: str
    last_name: str

    def __init__(self, id=None, first_name=None, last_name=None, **kwargs):
        """ map a dict to Location Drawer Creator object

        :param kwargs: Location Drawer Creator json dict
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """ String representation for the Location Drawer Creator model

        :return: Directory Location Drawer Creator reference
        """
        return f'{self.first_name} {self.last_name}'
