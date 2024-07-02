import datetime
from dataclasses import dataclass

@dataclass
class Match:
    MatchID: int
    TeamHomeID: int
    TeamAwayID: int
    TeamHomeFormation: int
    TeamAwayFormation: int
    ResultOfTeamHome: int
    Date: datetime.date

    def __hash__(self):
        return hash(self.MatchID)
