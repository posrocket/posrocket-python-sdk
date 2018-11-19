"""Location Tab Creator Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabCreatorModel:
    """ mapper class for Location Tab Creator object from Json Dict

    """
    id: str
    name: str
    email: str

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Tab creator object

        :param kwargs: Location Tab json creator dict
        """
        self.id = None
        self.name = None
        self.email = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Tab creator model

        :return: Location Tab creator name
        """
        return f'{self.name}'
