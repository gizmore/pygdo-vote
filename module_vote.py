from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.ui.GDT_Page import GDT_Page
from gdo.ui.GDT_Score import GDT_Score


class module_vote(GDO_Module):

    def gdo_classes(self):
        return [
        ]

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_Score('vote_min_score').initial('1'),
            GDT_Score('vote_max_score').initial('5'),
            GDT_UInt('vote_total_votes').initial('0').writable(False),
        ]

    def cfg_min_score(self) -> int:
        return self.get_config_value('vote_min_score')

    def cfg_max_score(self) -> int:
        return self.get_config_value('vote_max_score')

    def cfg_total_votes(self) -> int:
        return self.get_config_value('vote_total_votes')

    def gdo_load_scripts(self, page: 'GDT_Page'):
        self.add_js('js/gdo8-vote.js')
        self.add_css('css/gdo8-vote.css')
