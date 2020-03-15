"""Business Python model

"""
from posrocket.models.timezone import TimezoneModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
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
    phone: str
    address: str
    image: str
    _timezone: TimezoneModel

    def __init__(self,
                 id=None,
                 sub_domain=None,
                 name=None,
                 type=None,
                 country=None,
                 currency=None,
                 end_of_fiscal_day=None,
                 timezone=None,
                 phone=None,
                 address=None,
                 image=None,
                 **kwargs
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
        self.phone = phone
        self.address = address
        self.image = image
        self.timezone = timezone

    @property
    def timezone(self) -> TimezoneModel:
        """
        getter for timezone
        :return: timezone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, json_timezone: dict):
        """setter for timezone

        :param json_timezone: json timezone dicts
        :return: None
        """
        if json_timezone:
            self._timezone = TimezoneModel(**json_timezone)
        else:
            self._timezone = None

    def __str__(self) -> str:
        """ String representation for the Business model

        :return: Business name
        """
        return f'{self.name}'
