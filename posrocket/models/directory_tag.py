from uuid import UUID


class DirectoryTagModel:
    id: UUID = None
    name: str = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
