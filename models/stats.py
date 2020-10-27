from datetime import datetime
from .people import Commentator


class Commentary:
    def __init__(self, text: str, commentator: Commentator):
        self.__text = text
        self.__created_at = datetime.date.today()
        self.__created_by = commentator
