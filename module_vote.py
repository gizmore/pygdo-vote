from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.base.Util import href
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.Time import Time
from gdo.date.GDT_Duration import GDT_Duration
from gdo.ui.GDT_Link import GDT_Link
from gdo.ui.GDT_Page import GDT_Page
from gdo.vote.GDO_Poll import GDO_Poll
from gdo.vote.GDO_PollChoice import GDO_PollChoice
from gdo.vote.GDO_PollVote import GDO_PollVote


class module_vote(GDO_Module):

    def gdo_classes(self):
        return [
            GDO_Poll,
            GDO_PollChoice,
            GDO_PollVote,
        ]

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_UInt('max_side_polls').not_null().initial('3'),
            GDT_Duration('max_age_side_polls').not_null().initial('1w'),
        ]

    def cfg_max_side_polls(self) -> int:
        return self.get_config_value('max_side_polls')

    def cfg_max_age_side_polls(self) -> int:
        return self.get_config_value('max_age_side_polls')

    def gdo_init_sidebar(self, page: 'GDT_Page'):
        page._right_bar.add_field(
            GDT_Link().href(href('vote', 'create_poll')).text('mt_vote_create_poll'),
        )
        self.add_sidebar_polls(page)

    def add_sidebar_polls(self, page):
        cut = Time.get_date(Application.TIME - self.cfg_max_age_side_polls())
        result = (GDO_Poll.table().select().order('poll_created DESC').
                  select('(SELECT COUNT(*) FROM gdo_pollvote LEFT JOIN gdo_pollchoice ON pv_choice=pc_id WHERE pc_poll=poll_id) AS pc').
                  limit(self.cfg_max_side_polls()).where(f"poll_created >= '{cut}'").nocache().exec())
        for poll in result:
            page._right_bar.add_field(GDT_Link().href(href('vote', 'show_poll', f"&poll={poll.get_id()}")).text('poll_sidebar', (poll.gdo_value('poll_title'), poll._vals['pc'])))
