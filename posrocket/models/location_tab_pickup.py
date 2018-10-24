class LocationTabPickupModel:
    id = None
    eta = None
    company = None
    driver_name = None
    driver_phone = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.driver_name}'
