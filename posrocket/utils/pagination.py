class Pagination:
    def __init__(self, response, model_cls):
        self.model_cls = model_cls
        self.records = []
        self.has_next = True if response['next'] else False
        self.next = response['next']
        self.has_previous = True if response['previous'] else False
        self.previous = response['previous']

        for json_location in response['data']:
            self.records.append(self.model_cls(**json_location))

    def __iter__(self):
        return iter(self.records)

    def next(self):
        return next(self.records)
