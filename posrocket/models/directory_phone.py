class DirectoryPhoneModel:
    id = None
    number = None
    is_primary = None
    is_verified = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.number}'
