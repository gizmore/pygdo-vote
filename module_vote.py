from gdo.base.GDO_Module import GDO_Module
from gdo.base.Util import href
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

    def gdo_init_sidebar(self, page: 'GDT_Page'):
        page._right_bar.add_field(
            GDT_Link().href(href('vote', 'create_poll')).text('mt_vote_create_poll'),
        )
