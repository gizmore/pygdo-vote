from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Object import GDT_Object
from gdo.vote.WithVotes import WithVotes


class MethodVote(WithVotes, Method):

    def gdo_parameters(self) -> [GDT]:
        table = self.gdo_votes_table()
        return [
            table.column('vote_reason').copy_as('reason'),
            GDT_Object('id').not_null().table(self.gdo_vote_object_table()),
            table.column('vote_score').copy_as('score').initial(str(table.gdo_max_vote_score())),
        ]

    def get_vote_object(self) -> WithVotes|GDO:
        return self.param_value('id')

    def gdo_execute(self):
        obj = self.get_vote_object()
        self.gdo_votes_table().blank({
            'vote_item': obj.get_id(),
            'vote_score': self.param_val('score'),
            'vote_reason': self.param_val('reason'),
        }).soft_replace()
        return self.msg('msg_vote_voted', (obj.render_name(), obj.gdo_votes_total()))

