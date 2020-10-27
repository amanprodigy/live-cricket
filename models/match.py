from .base import Base, TimeTracker
from .enums import BallType, WicketType, InningStatus, MatchStatus
from .people import Player
from .teams import Team
from .address import Address
from ._errors import TeamAlreadyAddedException


class Ball(TimeTracker):
    def __init__(
            self,
            ball_number: int,
            bowled_by: Player,
            batted_by: Player,
            ball_type: BallType = BallType.NORMAL,  # By default normal ball
            wicket: WicketType = None,  # By default no wicket
            runs: int = 0,  # By default no run
            commentary: str = ''):  # By default no commentary
        self.__ball_number = ball_number
        self.__balled_by = bowled_by
        self.__played_by = batted_by
        self.__ball_type = ball_type
        self.__wicket = wicket
        self.__runs = runs
        self.__commentary = commentary

    def __repr__(self):
        return f"Ball#{self.__ball_number} Batted by {self.__batted_by} Bowled by {self.__bowled_by}"


class Over(Base):
    def __init__(self, number: int):
        self.__number = number
        self.__balls = []

    def add_ball(self, ball: Ball) -> None:
        self.__balls.append(ball)


class Wicket(TimeTracker):
    def __init__(
            self,
            wicket_type: WicketType,
            player_out: Player,
            caught_by: Player = None,  # By default no-one
            runout_by: Player = None,  # By default no-one
            stumped_by: Player = None):  # By default no-one
        self.__wicket_type = wicket_type
        self.__player_out = player_out
        self.__caught_by = caught_by
        self.__runout_by = runout_by
        self.__stumped_by = stumped_by


class Inning(Base):
    def __init__(
            self,
            number: 1 | 2,  # 1 or 2
            status: InningStatus = InningStatus.NOT_STARTED):
        self.__number = number
        self.__status = status
        self.__overs = []

    def add_over(self, over: Over) -> None:
        self.__overs.append(over)


class Stadium(Base):
    def __init__(self, name, address: Address):
        self.name = name


class Match(Base):
    __first_team: Team
    __second_team: Team
    __first_inning: Inning
    __second_inning: Inning
    __stadium: Stadium

    def __init__(self, number: int):
        self.__number = number
        self.__status = MatchStatus.LIVE
        self.__match_status = MatchStatus.NOT_STARTED

    def assign_stadium(self, stadium: Stadium) -> None:
        self.__stadium = stadium

    def add_team(self, team: Team) -> None:
        if self.__first_team and self.__second_team:
            raise TeamAlreadyAddedException()
        elif self.__first_team:
            self.__second_team = team
        else:
            self.__first_team = team

    def start_match(self) -> None:
        self.__match_status = MatchStatus.LIVE

    # Set first and second innings
    def start_first_inning(self, team: Team):
        if team == self.__first_team:
            self.__first_inning = Inning()
