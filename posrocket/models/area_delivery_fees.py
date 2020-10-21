"""Block Python model

"""
__author__ = "Yazan Alhorani"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Yazan Alhorani"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yazan Alhorani"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"


class AreaDeliveryFeesModel:
    """ mapper class for Block object from Json Dict

    """
    id: str
    area_id: str
    cost: float
    created_at: str
    updated_at: str

    def __init__(self, id=None, area_id=None, cost=None, created_at=None, updated_at=None, **kwargs):
        """ map a dict to Block object

        :param kwargs: Block json dict
        """
        self.id = id
        self.area_id = area_id
        self.cost = cost
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self) -> str:
        """ String representation for the Block model

        :return: Block name
        """
        return f'{self.area_id} {self.cost}'
