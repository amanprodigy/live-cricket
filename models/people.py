from .base import Base
from .address import Address, Nation


class Person(Base):
    def __init__(self, name: str, address: Address):
        super().__init__()
        self.__name = name
        self.__address = address


class Player(Base):
    def __init__(self, person: Person, nation: Nation):
        super().__init__()
        self.__person = person
        self.__nation = nation


class Admin(Base):
    def __init__(self, person: Person):
        super().__init__()
        self.__person = person

    def add_match(self, match):
        pass

    def add_team(self, team):
        pass

    def add_player(self, player):
        pass


class Commentator(Base):
    def __init__(self, person: Person):
        self.__person = person

    def assign_match(self, match):
        pass
