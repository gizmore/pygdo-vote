from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.ui.GDT_Score import GDT_Score


class module_vote(GDO_Module):

    def gdo_classes(self):
        return [
        ]

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_Score('vote_min_score').initial('0'),
            GDT_Score('vote_max_score').initial('5'),
        ]

    def cfg_min_score(self) -> int:
        return self.get_config_value('vote_min_score')

    def cfg_max_score(self) -> int:
        return self.get_config_value('vote_max_score')
