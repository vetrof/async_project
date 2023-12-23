import requests
import time

start = time.time()

from api_manager import ApiManager
api_list_general = ApiManager().get_list_api('api_list_general.txt')
api_list_cat_fact = ApiManager().get_list_api('api_list_cat_fact.txt')


def get_data(list_url):
    for link in list_url:
        start_local = time.time()
        data = requests.get(link).json()
        end = time.time()
        print("запрос за:", link, round(end - start_local, 2))


get_data(api_list_general)
get_data(api_list_cat_fact)

end = time.time()
print("общее время:", round(end - start, 2))

