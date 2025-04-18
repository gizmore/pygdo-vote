from gdo.base.Exceptions import GDOException
from gdo.base.GDO import GDO


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.vote.GDO_VoteTable import GDO_VoteTable


class WithVotes:

    def gdo_votes_table(self) -> 'GDO_VoteTable':
        raise GDOException(f"{self.__class__.__name__} does not define gdo_votes_table().")

    def gdo_vote_object_table(self) -> GDO:
        raise GDOException(f"{self.__class__.__name__} does not define gdo_vote_object_table().")

    def gdo_votes_total(self) -> int:
        return self.gdo_votes_table().count_where(f'vote_id={self.get_id()}')
