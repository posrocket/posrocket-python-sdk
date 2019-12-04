"""Position Python model

"""

__author__ = "Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Rawan Amro"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Rawan Amro"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class PositionModel:
    """mapper class for Position object from Json Dict

    """
    longitude: str
    latitude: str

    def __init__(self, longitude=None, latitude=None, **kwargs):
        """map a dict to Position object

        :param kwargs: Payment Method json dict
        """
        self.longitude = longitude
        self.latitude = latitude