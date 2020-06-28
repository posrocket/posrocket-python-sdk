"""Avenue Python model

"""
__author__ = "Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Rawan Amro"
__email__ = "r.amro@posrocket.com"
__status__ = "Beta"

from typing import List

from posrocket.models import BlockModel


class AvenueModel:
    """ mapper class for Avenue object from Json Dict

    """
    id: str
    en: str
    ar: str
    _blocks: List[BlockModel]

    def __init__(self, id=None, en=None,ar=None, blocks=None, **kwargs):
        """ map a dict to Avenue object

        :param kwargs: Avenue json dict
        """
        self.id = id
        self.en = en
        self.ar = ar
        self.blocks = blocks

    def __str__(self) -> str:
        """ String representation for the Avenue model

        :return: Avenue name
        """
        return f'{self.en}'

    @property
    def blocks(self) -> List[BlockModel]:
        """
        getter for Item variations
        :return: list of variations for the item
        """
        return self._blocks

    @blocks.setter
    def blocks(self, json_blocks: List[dict]):
        """setter for item variations

        :param json_variations: json list of variation dicts
        :return: None
        """
        self._blocks = []
        for json_block in json_blocks or []:
            if json_block:
                self._blocks.append(BlockModel(**json_block))
