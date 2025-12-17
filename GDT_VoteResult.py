from gdo.core.GDT_Decimal import GDT_Decimal
from gdo.vote.GDO_VoteTable import GDO_VoteTable


class GDT_VoteResult(GDT_Decimal):

    _table: GDO_VoteTable

    def __init__(self, name: str):
        super().__init__(name)
        self.digits(2, 3)

    def table(self, table: GDO_VoteTable):
        self._table = table
        return self
