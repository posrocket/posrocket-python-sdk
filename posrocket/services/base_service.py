class BaseServiceFactory:
    def __init__(self):
        raise NotImplemented()

    @staticmethod
    def make_list_items_response(page=1, **kwargs):
        def list_items_response(self):
            params = kwargs
            params['page'] = page
            url = self.get_service_url()
            response = self.get(url, params=params)
            result = []
            for json_location in response['data']:
                result.append(self.model_cls(**json_location))
            return result

        return list_items_response

    @staticmethod
    def make_detail_item_response():
        def detail_item_response(self, pk):
            url = self.get_service_url()
            response = self.get(f"{url}/{pk}")
            return self.model_cls(**response)

        return detail_item_response
