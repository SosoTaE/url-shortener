import string
from config import NEW_URL_SIZE, ROUTE_TIME
import time
import random

class URlShortener:
    def __init__(self):
        self.__quantity = 0
        self.__number = random.randint(100000,1000000)
        self.__data = {}
        self.__characters = string.ascii_letters + string.digits

    def get_new_short_url(self, prev_url):
        generated_route = self.__generate_route()
        self.__remove_items()
        self.__data[generated_route] = {"url": prev_url, "timestamp": time.time()}
        self.__number += 1
        self.__quantity += 1

        return generated_route

    def __generate_route(self):
        number = self.__number
        result = ""
        for i in range(NEW_URL_SIZE):
            x = number % 10
            result += self.__characters[x]
            number //= 10

        return result

    def __remove_items(self):
        for key, value in self.__data.items():
            timestamp = value.get("timestamp")
            if time.time() - timestamp >= ROUTE_TIME:
                self.__data.pop(key)

    def get(self, url):
        self.__remove_items()

        return self.__data.get(url)



url_shortener = URlShortener()