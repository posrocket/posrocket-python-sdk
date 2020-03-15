"""Summary Details Python model

"""
__author__ = "Lujain Battiki, Rawan Amro"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Lujain Battiki, Rawan Amro"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Lujain Battiki, Rawan Amro"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"

class SummaryDetailsModel:
    """mapper class for Summary Details object from Json Dict

    """

    discounts: float
    modifiers: float
    tip: float
    additive_tax: float
    inclusive_tax: float
    tax: float
    net_sales: float
    gross_sales: float
    extra_charges: float
    total_collected: float
    cash: float
    credit_card: float
    other: float

    def __init__(self,
                 discounts=None,
                 modifiers=None,
                 tip=None,
                 additive_tax=None,
                 inclusive_tax=None,
                 tax=None,
                 net_sales=None,
                 gross_sales=None,
                 extra_charges=None,
                 total_collected=None,
                 cash=None,
                 credit_card=None,
                 other=None,
                 **kwargs
                 ):
        """map a dict to Summary Details object

        :param kwargs: Summary Details json dict
        """
        self.discounts = discounts
        self.modifiers = modifiers
        self.tip = tip
        self.additive_tax = additive_tax
        self.inclusive_tax = inclusive_tax
        self.tax = tax
        self.net_sales = net_sales
        self.gross_sales = gross_sales
        self.extra_charges = extra_charges
        self.total_collected = total_collected
        self.cash = cash
        self.credit_card = credit_card
        self.other = other
