from gdo.base.Exceptions import GDOException
from gdo.vote.GDO_VoteTable import GDO_VoteTable


class WithVotes:

    def gdo_vote_table(self) -> GDO_VoteTable:
        raise GDOException(f"{self.__class__.__name__} does not define gdo_vote_table().")
