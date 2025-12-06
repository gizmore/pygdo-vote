from gdo.base.GDO import GDO
from gdo.base.Trans import t
from gdo.core.GDT_UInt import GDT_UInt

from typing import TYPE_CHECKING

from gdo.vote.GDO_VoteTable import GDO_VoteTable

if TYPE_CHECKING:
    from gdo.vote.WithVotes import WithVotes


class GDT_VoteCount(GDT_UInt):

    _table: GDO_VoteTable|None

    def __init__(self, name: str):
        super().__init__(name)
        self._table = None
        self.not_null()
        self.initial('0')

    def table(self, table: GDO_VoteTable):
        self._table = table
        return self

    def gdo_with_votes(self) -> 'GDO|WithVotes':
        return self._gdo

    def refresh(self):
        gdo = self.gdo_with_votes()
        count = gdo.gdo_votes_table().count_where(f"vote_item={gdo.get_id()}")
        gdo.set_val(self.get_name(), str(count))

    ##########
    # Render #
    ##########

    def render_txt(self) -> str:
        return t('txt_vote_count', (self.get_val()))
