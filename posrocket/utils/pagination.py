class Pagination:
    def __init__(self, response, model_cls):
        self.model_cls = model_cls
        self.records = []
        self.has_next = True if 'next' in response and response['next'] else False
        self.next = response['next'] if 'next' in response else None
        self.has_previous = True if 'previous' in response and response['previous'] else False
        self.previous = response['previous'] if 'previous' in response else None

        try:
            for json_location in response['data']:
                self.records.append(self.model_cls(**json_location))
        except Exception as e:
            for item in response:
                self.records.append(self.model_cls(**item))

    def __iter__(self):
        return iter(self.records)

    def next(self):
        return next(self.records)
