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
    id: str
    sub_domain: str
    name: str
    type: str
    country: str
    currency: str
    end_of_fiscal_day: str
    time_offset: str
    phone: str
    address: str
    image: str

    def __init__(self, **kwargs):
        """map a dict to Business object

        :param kwargs: Business json dict
        """
        self.id = None
        self.sub_domain = None
        self.name = None
        self.type = None
        self.country = None
        self.currency = None
        self.end_of_fiscal_day = None
        self.time_offset = None
        self.phone = None
        self.address = None
        self.image = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Business model

        :return: Business name
        """
        return f'{self.name}'
