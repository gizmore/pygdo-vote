from gdo.base.GDO import GDO
from gdo.base.Trans import t
from gdo.core.GDT_UInt import GDT_UInt

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.vote.WithVotes import WithVotes


class GDT_VoteCount(GDT_UInt):

    def __init__(self, name: str):
        super().__init__(name)
        self.not_null()
        self.initial('0')

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
