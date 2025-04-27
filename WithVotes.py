from gdo.base.Exceptions import GDOException
from gdo.base.GDO import GDO


from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from gdo.vote.GDO_VoteTable import GDO_VoteTable


class WithVotes:
    """
    Make your GDO to vote on inherit this mixin.
    add GDT_VoteCount and GDT_VoteOutcome to the gdo_columns.
    create a MethodVote
    Create a GDO inheriting GDO_VoteTable
    """

    def gdo_votes_table(self) -> 'GDO_VoteTable':
        raise GDOException(f"{self.__class__.__name__} does not define gdo_votes_table().")

    def gdo_vote_object_table(self) -> GDO:
        raise GDOException(f"{self.__class__.__name__} does not define gdo_vote_object_table().")

    def as_gdo(self) -> 'GDO|WithVotes':
        return self

    def recalculate_votes(self):
        from gdo.vote.GDT_VoteCount import GDT_VoteCount
        from gdo.vote.GDT_VoteOutcome import GDT_VoteOutcome
        self.as_gdo().column_of(GDT_VoteCount).refresh()
        self.as_gdo().column_of(GDT_VoteOutcome).refresh()
        self.as_gdo().save()

    def query_votes_total(self) -> int:
        return self.gdo_votes_table().count_where(f'vote_id={self.get_id()}')
