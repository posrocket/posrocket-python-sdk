"""Directory Phone Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class DirectoryPhoneModel:
    """ mapper class for Directory Phone object from Json Dict

    """
    id: str
    number: str
    is_primary: bool
    is_verified: bool

    def __init__(self,
                 id=None,
                 number=None,
                 is_primary=None,
                 is_verified=None,
                 **kwargs
                 ):
        """ map a dict to Directory Phone object

        :param kwargs: Directory Phone json dict
        """
        self.id = id
        self.number = number
        self.is_primary = is_primary
        self.is_verified = is_verified

    def __str__(self) -> str:
        """ String representation for the Directory Phone model

        :return: Directory Phone number
        """
        return f'{self.number}'
