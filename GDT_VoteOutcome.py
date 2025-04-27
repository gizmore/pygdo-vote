from gdo.base.GDO import GDO
from gdo.vote.GDT_Stars import GDT_Stars

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.vote.WithVotes import WithVotes


class GDT_VoteOutcome(GDT_Stars):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo(self, gdo: GDO):
        super().gdo(gdo)
        self.min(self.gdo_with_votes().gdo_votes_table().gdo_min_vote_score())
        self.max(self.gdo_with_votes().gdo_votes_table().gdo_max_vote_score())
        return self

    def gdo_with_votes(self) -> 'GDO|WithVotes':
        return self._gdo

    def refresh(self):
        gdo = self.gdo_with_votes()
        average = float(gdo.gdo_votes_table().select('AVG(vote_score)').where(f"vote_item={gdo.get_id()}").exec(False).fetch_val())
        gdo.set_val(self.get_name(), str(round(average, 1)))
        return self
