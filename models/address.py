from enum import Enum


class Nation(Enum):
    INDIA = 'IND'
    AUSTRALIA = 'AUS'
    ENGLAND = 'ENG'
    NEW_ZEALAND = 'NZD'


class Address:
    def __init__(self, city: str, state: str, country: str):
        self.__city = city
        self.__state = state
        self.__country = country

    def __repr__(self):
        return f"{self.__city} {self.__state} {self.__country}"
