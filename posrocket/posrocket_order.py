"""
POS Rocket Order Module
"""
import json
from posrocket.utils import Singleton


class POSRocketOrder(object):
    __metaclass__ = Singleton

    """
    Order Object Class to change json data into python object
    """

    def __init__(self, tab_id=None, location_id=None, issuer_id=None, sequence_number=None, name=None,
                 ticket_number=None, creation_time=None, status=None,
                 acknowledged=None, total_amount=None, order_option=None, items=None, customer=None, pickup=None,
                 creator=None):
        """
        :param tab_id: POSRocket tab_id for order
        :type tab_id: UUID
        :param location_id: Location id for order
        :type location_id: UUID
        :param issuer_id: Issuer id for order
        :type issuer_id: UUID
        :param sequence_number: Sequence number for order
        :type sequence_number: int
        :param name: Name of the Order/Tab
        :type name: str
        :param ticket_number: Ticket number for order
        :type ticket_number: int
        :param creation_time: Date and time of the creation of the order
        :type creation_time: date str
        :param status: Order Status (current state)
        :type status: str
        :param total_amount: Total amount to be paid by the customer
        :type total_amount: int
        :param acknowledged: Status of the order if it is acknowledged by the restaurant
        :type acknowledged: bool
        :param order_option: Order Options for the order
        :type order_option: dict
        :param items: Items in the order
        :type items: dict
        :param customer: Customer Details
        :type customer: dict
        :param pickup: Pickup(delivery) details of the order
        :type pickup: dict
        :param creator: Order Creator details
        :type creator: dict
        """
        self.tab_id = tab_id
        self.location_id = location_id
        self.issuer_id = issuer_id
        self.sequence_number = sequence_number
        self.name = name
        self.ticket_number = ticket_number
        self.creation_time = creation_time
        self.status = status
        self.issuer_id = issuer_id
        self.acknowledged = acknowledged
        self.total_amount = total_amount
        self.order_option = order_option
        self.items = items
        self.customer = customer
        self.pickup = pickup
        self.creator = creator

    def to_json(self):
        """Returns Order Object as a json object
        """
        return json.dumps(self.__dict__)