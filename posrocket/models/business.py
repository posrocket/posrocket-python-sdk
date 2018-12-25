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

    def __init__(self,
                 id=None,
                 sub_domain=None,
                 name=None,
                 type=None,
                 country=None,
                 currency=None,
                 end_of_fiscal_day=None,
                 time_offset=None,
                 phone=None,
                 address=None,
                 image=None
                 ):
        """map a dict to Business object

        :param kwargs: Business json dict
        """
        self.id = id
        self.sub_domain = sub_domain
        self.name = name
        self.type = type
        self.country = country
        self.currency = currency
        self.end_of_fiscal_day = end_of_fiscal_day
        self.time_offset = time_offset
        self.phone = phone
        self.address = address
        self.image = image

    def __str__(self) -> str:
        """ String representation for the Business model

        :return: Business name
        """
        return f'{self.name}'
