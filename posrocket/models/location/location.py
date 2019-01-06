"""Location Python model

"""
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationModel:
    """ mapper class for Location object from Json Dict

    """
    id: str
    name: str
    tax_number: str
    phone: str
    address: str

    def __init__(self,
                 id=None,
                 name=None,
                 tax_number=None,
                 phone=None,
                 address=None,
                 **kwargs
                 ):
        """ map a dict to Location object

        :param kwargs: Location json dict
        """
        self.id = id
        self.name = name
        self.tax_number = tax_number
        self.phone = phone
        self.address = address

    def __str__(self) -> str:
        """ String representation for the Location model

        :return: Location name
        """
        return f'{self.name}'
