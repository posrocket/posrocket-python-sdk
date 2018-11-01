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
    id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    gender: str = None
    dob: date = None
    country: str = None
    _addresses: List[DirectoryAddressModel] = None
    _phone_numbers: List[DirectoryPhoneModel] = None
    _tags: List[DirectoryTagModel] = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Directory Customer object

        :param kwargs: Directory Customer json dict
        """
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
