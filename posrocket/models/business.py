class BusinessModel:
    id = None
    sub_domain = None
    name = None
    type = None
    country = None
    currency = None
    end_of_fiscal_day = None
    time_offset = None
    phone = None
    address = None
    image = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
