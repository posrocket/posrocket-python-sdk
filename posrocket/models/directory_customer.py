"""Directory Customer Python model

"""
from datetime import date
from typing import List

from posrocket.models.directory_address import DirectoryAddressModel
from posrocket.models.directory_phone import DirectoryPhoneModel
from posrocket.models.directory_tag import DirectoryTagModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class DirectoryCustomerModel:
    """ mapper class for Directory Customer object from Json Dict

    """
    id: str
    first_name: str
    last_name: str
    email: str
    gender: str
    dob: date
    country: str
    _addresses: List[DirectoryAddressModel]
    _phone_numbers: List[DirectoryPhoneModel]
    _tags: List[DirectoryTagModel]

    def __init__(self, **kwargs: dict):
        """ map a dict to Directory Customer object

        :param kwargs: Directory Customer json dict
        """
        self.id = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.gender = None
        self.dob = None
        self.country = None
        self._addresses = None
        self._phone_numbers = None
        self._tags = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Directory Customer model

        :return: Directory Customer full name
        """
        return f'{self.get_full_name()}'

    def get_full_name(self) -> str:
        """ complains the customer first and last name and return the full name

        :return: the customer full name
        """
        return f'{self.first_name} {self.last_name}'

    @property
    def addresses(self) -> List[DirectoryAddressModel]:
        """getter for customer addresses

        :return: list of addresses for the customer
        """
        return self._addresses

    @addresses.setter
    def addresses(self, json_addresses: List[dict]):
        """setter for customer addresses

        :param json_addresses:json list of address dicts
        :return: None
        """
        self._addresses = []
        for json_address in json_addresses:
            if isinstance(json_address, DirectoryAddressModel):
                self._addresses.append(json_address)
            else:
                self._addresses.append(DirectoryAddressModel(**json_address))

    @property
    def phone_numbers(self) -> List[DirectoryPhoneModel]:
        """getter for customer phones

        :return: list of phones for the customer
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, json_phone_numbers: List[dict]):
        """setter for customer phones

        :param json_phone_numbers:json list of phone dicts
        :return: None
        """
        self._phone_numbers = []
        for json_phone_number in json_phone_numbers:
            if isinstance(json_phone_number, DirectoryPhoneModel):
                self._phone_numbers.append(json_phone_number)
            else:
                self._phone_numbers.append(DirectoryPhoneModel(**json_phone_number))

    @property
    def tags(self) -> List[DirectoryTagModel]:
        """getter for customer tags

        :return: list of tags for the customer
        """
        return self._tags

    @tags.setter
    def tags(self, json_tags: List[dict]):
        """setter for customer tags

        :param json_tags:json list of tag dicts
        :return: None
        """
        self._tags = []
        for json_tag in json_tags:
            self._tags.append(DirectoryTagModel(**json_tag))


class SaleCustomerModel:
    """ mapper class for Directory Customer object from Json Dict

    """
    id: str
    first_name: str
    last_name: str
    email: str
    gender: str
    dob: date
    country: str
    _address: DirectoryAddressModel
    _phone_number: DirectoryPhoneModel
    _tags: List[DirectoryTagModel]

    def __init__(self, **kwargs: dict):
        """ map a dict to Directory Customer object

        :param kwargs: Directory Customer json dict
        """
        self.id = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.gender = None
        self.dob = None
        self.country = None
        self._address = None
        self._phone_number = None
        self._tags = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Directory Customer model

        :return: Directory Customer full name
        """
        return f'{self.get_full_name()}'

    def get_full_name(self) -> str:
        """ complains the customer first and last name and return the full name

        :return: the customer full name
        """
        return f'{self.first_name} {self.last_name}'

    @property
    def address(self) -> DirectoryAddressModel:
        """getter for customer addresses

        :return: list of addresses for the customer
        """
        return self._address

    @address.setter
    def address(self, json_address: dict):
        """setter for customer addresses

        :param json_address:json address dicts
        :return: None
        """
        if isinstance(json_address, DirectoryAddressModel):
            self._address = json_address
        else:
            self._address = DirectoryAddressModel(**json_address)

    @property
    def phone_number(self) -> DirectoryPhoneModel:
        """getter for customer phones

        :return: list of phones for the customer
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, json_phone_number: dict):
        """setter for customer phones

        :param json_phone_number:json list of phone dicts
        :return: None
        """
        if isinstance(json_phone_number, DirectoryPhoneModel):
            self._phone_number = json_phone_number
        else:
            self._phone_number = DirectoryPhoneModel(**json_phone_number)

    @property
    def tags(self) -> List[DirectoryTagModel]:
        """getter for customer tags

        :return: list of tags for the customer
        """
        return self._tags

    @tags.setter
    def tags(self, json_tags: List[dict]):
        """setter for customer tags

        :param json_tags:json list of tag dicts
        :return: None
        """
        self._tags = []
        for json_tag in json_tags:
            self._tags.append(DirectoryTagModel(**json_tag))
