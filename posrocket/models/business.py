"""Business Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class BusinessModel:
    """mapper class for Business object from Json Dict

    """
    id: str = None
    sub_domain: str = None
    name: str = None
    type: str = None
    country: str = None
    currency: str = None
    end_of_fiscal_day: str = None
    time_offset: str = None
    phone: str = None
    address: str = None
    image: str = None

    def __init__(self, **kwargs):
        """map a dict to Business object

        :param kwargs: Business json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Business model

        :return: Business name
        """
        return f'{self.name}'
