"""Directory Address Python model

"""
from posrocket.models.position import PositionModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

from posrocket.models.area import AreaModel
from posrocket.models.city import CityModel
from posrocket.models.avenue_info import AvenueInfoModel
from posrocket.models.block_info import BlockInfoModel


class DirectoryAddressModel:
    """ mapper class for Directory Address object from Json Dict

    """
    id: str
    label: str
    residence: str
    street: str
    building: str
    floor: str
    apartment: str
    extras: str
    is_primary: bool
    is_verified: bool
    _city: CityModel
    _area: AreaModel
    _avenue: AvenueInfoModel
    _block: BlockInfoModel
    _position: PositionModel

    def __init__(self,
                 id=None,
                 label=None,
                 residence=None,
                 street=None,
                 building=None,
                 floor=None,
                 apartment=None,
                 extras=None,
                 is_primary=None,
                 is_verified=None,
                 city=None,
                 area=None,
                 avenue=None,
                 block=None,
                 position=None,
                 **kwargs
                 ):
        """ map a dict to Directory Address object

        :param kwargs: Directory Address json dict
        """
        self.id = id
        self.label = label
        self.residence = residence
        self.street = street
        self.building = building
        self.floor = floor
        self.apartment = apartment
        self.extras = extras
        self.is_primary = is_primary
        self.is_verified = is_verified
        self.city = city
        self.area = area
        self.avenue = avenue
        self.block = block
        self.position = position

    def __str__(self) -> str:
        """ String representation for the Directory Address model

        :return: Directory Address label
        """
        return f'{self.label}'

    @property
    def city(self) -> CityModel:
        """
        getter for Address City
        :return: Address City object
        """
        return self._city

    @city.setter
    def city(self, json_city: dict):
        """setter for Address City

        :param json_city: json dict for City
        :return: None
        """
        if not json_city:
            self._city = None
        elif isinstance(json_city, CityModel):
            self._city = json_city
        else:
            self._city = CityModel(**json_city)

    @property
    def area(self) -> AreaModel:
        """
        getter for Address Area
        :return: Address Area object
        """
        return self._area

    @area.setter
    def area(self, json_area: dict):
        """setter for Address Area

        :param json_city: json dict for Area
        :return: None
        """
        if not json_area:
            self._area = None
        elif isinstance(json_area, AreaModel):
            self._area = json_area
        else:
            self._area = AreaModel(**json_area)

    @property
    def avenue(self) -> AvenueInfoModel:
        """
        getter for Address City Area Avenue
        :return: Address City Area Avenue object
        """
        return self._avenue

    @avenue.setter
    def avenue(self, json_avenue: dict):
        """setter for Address City Area Avenue

        :param json_avenue: json dict for City Area Avenue
        :return: None
        """
        if not json_avenue:
            self._avenue = None
        elif isinstance(json_avenue, AvenueInfoModel):
            self.avenue = json_avenue
        else:
            self._avenue = AvenueInfoModel(**json_avenue)

    @property
    def block(self) -> BlockInfoModel:
        """
        getter for Address City Area Avenue
        :return: Address City Area Avenue object
        """
        return self._block

    @block.setter
    def block(self, json_block: dict):
        """setter for Address City Area Avenue Block

        :param json_block: json dict for City Area Avenue Block
        :return: None
        """
        if not json_block:
            self._block = None
        elif isinstance(json_block, BlockInfoModel):
            self.block = json_block
        else:
            self._block = BlockInfoModel(**json_block)


    @property
    def position(self) -> PositionModel:
        """
        getter for Customer Address Position
        :return: Customer Address Position object
        """
        return self._position

    @position.setter
    def position(self, json_position: dict):
        """setter for Customer Address Position

        :param json_position: json dict for Customer Address Position
        :return: None
        """
        if json_position:
            self._position = PositionModel(**json_position)
        else:
            self._position = None

