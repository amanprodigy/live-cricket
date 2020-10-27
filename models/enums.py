from enum import Enum


class MatchType(Enum):
    ODI, T20, TEST = 1, 2, 3


class InningStatus(Enum):
    NOT_STARTED, LIVE, FINISHED = 1, 2, 3


class MatchStatus(Enum):
    NOT_STARTED, LIVE, FINISHED, DRAWN, CANCELLED = 1, 2, 3, 4, 5


class WicketType(Enum):
    BOLD, CAUGHT, STUMPED, RUN_OUT, LBW, RETIRED_HURT, HIT_WICKET = 1, 2, 3, 4, 5, 6, 7


class BallType(Enum):
    NORMAL, WIDE, WICKET, NO_BALL = 1, 2, 3, 4


class RunType(Enum):
    NORMAL, FOUR, SIX, LEG_BYE, BYE, NO_BALL, OVERTHROW = 1, 2, 3, 4, 5, 6, 7
