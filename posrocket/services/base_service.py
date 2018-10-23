class BaseServiceFactory:
    def __init__(self):
        raise NotImplemented()

    @staticmethod
    def make_list_items_response():
        def list_items_response(self):
            response = self.get(self.service_url)
            result = []
            for json_location in response['data']:
                result.append(self.model_cls(**json_location))
            return result

        return list_items_response

    @staticmethod
    def make_detail_item_response():
        def detail_item_response(self, pk):
            response = self.get(f"{self.service_url}/{pk}")
            return self.model_cls(**response)

        return detail_item_response
