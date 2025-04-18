from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Object import GDT_Object
from gdo.date.GDT_Created import GDT_Created
from gdo.ui.GDT_Score import GDT_Score
from gdo.vote.WithVotes import WithVotes


class GDO_VoteTable(WithVotes, GDO):

    def gdo_min_score(self) -> int:
        return 4

    def gdo_max_score(self) -> int:
        return 7

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Object('vote_item').primary().cascade_delete().table(self.gdo_vote_table()),
            GDT_Creator('vote_creator').primary(),
            GDT_Score('vote_score').min(self.gdo_min_score()).max(self.gdo_max_score()),
            GDT_Created('vote_created'),
        ]
