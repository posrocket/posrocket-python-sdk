from posrocket.models.directory_address import DirectoryAddressModel
from posrocket.models.directory_phone import DirectoryPhoneModel
from posrocket.models.directory_tag import DirectoryTagModel


class DirectoryCustomerModel:
    id = None
    first_name = None
    last_name = None
    email = None
    gender = None
    dob = None
    country = None
    _addresses = None
    _phone_numbers = None
    _tags = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, json_addresses):
        self._addresses = []
        for json_address in json_addresses:
            self._addresses.append(DirectoryAddressModel(**json_address))

    @property
    def phone_numbers(self):
        return self._addresses

    @phone_numbers.setter
    def phone_numbers(self, json_phone_numbers):
        self._phone_numbers = []
        for json_phone_number in json_phone_numbers:
            self._phone_numbers.append(DirectoryPhoneModel(**json_phone_number))

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, json_tags):
        self._tags = []
        for json_tag in json_tags:
            self._tags.append(DirectoryTagModel(**json_tag))
