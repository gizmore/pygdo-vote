from gdo.base.Exceptions import GDOException
from gdo.base.GDO import GDO

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.vote.GDO_VoteTable import GDO_VoteTable
    from gdo.vote.GDT_VoteCount import GDT_VoteCount
    from gdo.vote.GDT_VoteOutcome import GDT_VoteOutcome

class WithVotes:
    """
    Make your GDO to vote on inherit this mixin.
    add GDT_VoteCount and GDT_VoteOutcome to the gdo_columns.
    create a MethodVote
    Create a GDO inheriting GDO_VoteTable
    """
    def as_gdo(self) -> 'GDO|WithVotes':
        return self

    def gdo_votes_table(self) -> 'GDO_VoteTable':
        raise GDOException(f"{self.__class__.__name__} does not define gdo_votes_table().")

    def gdo_vote_object_table(self) -> 'GDO|WithVotes':
        raise GDOException(f"{self.__class__.__name__} does not define gdo_vote_object_table().")

    def get_vote_count_column(self) -> 'GDT_VoteCount':
        from gdo.vote.GDT_VoteCount import GDT_VoteCount
        return self.as_gdo().column_of(GDT_VoteCount)

    def get_vote_score_column(self) -> 'GDT_VoteOutcome':
        from gdo.vote.GDT_VoteOutcome import GDT_VoteOutcome
        return self.as_gdo().column_of(GDT_VoteOutcome)

    def recalculate_votes(self):
        self.get_vote_count_column().refresh()
        self.get_vote_score_column().refresh()
        return self.as_gdo().save()

    def get_votes_total(self) -> int:
        return self.get_vote_count_column().get_value()

    def get_votes_score(self) -> float:
        return round(self.get_vote_score_column().get_value(), 1)
