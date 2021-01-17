"""Location Discount Days Python model

"""

__author__ = "Mohammad Hashim"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Mohammad Hashim"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Mohammad Hashim"
__email__ = "m.hashim@posrocket.com"
__status__ = "Beta"


class LocationDiscountDaysTimeModel:

    start: str
    end: str

    def __init__(self,
                 start=None,
                 end=None,
                 **kwargs
                 ):
        self.start =start
        self.end =end


class LocationDiscountDaysModel:

    id: str
    day: str
    _time: LocationDiscountDaysTimeModel

    def __init__(self,
                 id=None,
                 day=None,
                 time=None,
                 **kwargs
                 ):
        self.id = id
        self.day = day
        self.time = time

    def __str__(self) -> str:

        return f'{self.day}'


    @property
    def time(self) -> LocationDiscountDaysTimeModel:
        return self._time
