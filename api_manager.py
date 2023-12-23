
class ApiManager:

    @staticmethod
    def get_list_api(filename):
        with open(filename) as file:
            api_list = []
            for api_link in file:
                api_link = api_link.strip()
                if len(api_link) > 0:
                    api_list.append(api_link)
            return api_list
