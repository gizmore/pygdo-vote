from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Object import GDT_Object
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Created import GDT_Created
from gdo.ui.GDT_Score import GDT_Score
from gdo.vote.module_vote import module_vote

from gdo.vote.WithVotes import WithVotes


class GDO_VoteTable(WithVotes, GDO):
    """
    Inherit from this table to enable votes
    """

    def gdo_min_vote_score(self) -> int:
        return module_vote.instance().cfg_min_score()

    def gdo_max_vote_score(self) -> int:
        return module_vote.instance().cfg_max_score()

    def gdo_cached(self) -> bool:
        return False

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Object('vote_item').primary().table(self.gdo_vote_object_table()).cascade_delete(),
            GDT_Creator('vote_creator').primary().cascade_delete(),
            GDT_String('vote_reason').maxlen(96),
            GDT_Score('vote_score').bytes(1).min(self.gdo_min_vote_score()).max(self.gdo_max_vote_score()),
            GDT_Created('vote_created'),
        ]
