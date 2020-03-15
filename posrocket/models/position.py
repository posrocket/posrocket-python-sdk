"""Position Python model

"""

__author__ = "Rawan Amro, Lujain Battikhi"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Rawan Amro", "Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Rawan Amro, Lujain Battikhi"
__email__ ="Launchpad@posrocket.com"
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
