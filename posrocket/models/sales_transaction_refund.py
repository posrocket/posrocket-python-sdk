from posrocket.models.directory_customer import DirectoryCustomerModel
from posrocket.models.sales_transaction_extra_charges import SalesTransactionExtraChargeModel
from posrocket.models.sales_transaction_itemization import SalesTransactionItemizationModel
from posrocket.models.sales_transaction_refund_creator import SalesTransactionRefundCreatorModel
from posrocket.models.sales_transaction_tender import SalesTransactionTenderModel


class SalesTransactionRefundModel:
    id = None
    transaction_id = None
    type = None
    reason = None
    notes = None
    serial_number = None
    creation_time = None
    _customer = None
    _tender = None
    _creator = None
    _extra_charges = None
    _itemization = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.id}'

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer_dict):
        self._customer = DirectoryCustomerModel(**customer_dict)

    @property
    def tender(self):
        return self._tender

    @tender.setter
    def tender(self, tender_dict):
        self._tender = SalesTransactionTenderModel(**tender_dict)

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, creator_dict):
        self._creator = SalesTransactionRefundCreatorModel(**creator_dict)

    @property
    def extra_charges(self):
        return self._extra_charges

    @extra_charges.setter
    def extra_charges(self, extra_charges_list):
        self._extra_charges = []
        for extra_charge in extra_charges_list:
            self._extra_charges.append(SalesTransactionExtraChargeModel(**extra_charge))

    @property
    def itemization(self):
        return self._itemization

    @itemization.setter
    def itemization(self, itemization_list):
        self._itemization = []
        for itemization in itemization_list:
            self._itemization.append(SalesTransactionItemizationModel(**itemization))
