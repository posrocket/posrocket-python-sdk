class BaseServiceFactory:
    def __init__(self):
        raise NotImplemented()

    @staticmethod
    def list_items_response(self, **kwargs):
        params = kwargs
        url = self.get_service_url()
        response = self.get(url, params=params)
        result = []
        for json_location in response['data']:
            result.append(self.model_cls(**json_location))
        return result

    @staticmethod
    def detail_item_response(self, pk):
        url = self.get_service_url()
        response = self.get(f"{url}{pk}/")
        return self.model_cls(**response)
