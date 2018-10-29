"""Directory Phone Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class DirectoryPhoneModel:
    """ mapper class for Directory Phone object from Json Dict

    """
    id: str = None
    number: str = None
    is_primary: bool = None
    is_verified: bool = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Directory Phone object

        :param kwargs: Directory Phone json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Directory Phone model

        :return: Directory Phone number
        """
        return f'{self.number}'
