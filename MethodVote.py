from gdo.base.Application import Application
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.IPC import IPC
from gdo.base.Method import Method
from gdo.core.GDT_Object import GDT_Object
from gdo.vote.WithVotes import WithVotes


class MethodVote(WithVotes, Method):

    def gdo_parameters(self) -> list[GDT]:
        table = self.gdo_votes_table()
        return [
            table.column('vote_reason').copy_as('reason'),
            table.column('vote_score').copy_as('score').initial(str(table.gdo_max_vote_score())),
            GDT_Object('id').not_null().table(self.gdo_vote_object_table()),
        ]

    def get_vote_object(self) -> GDO|WithVotes:
        return self.param_value('id')

    async def gdo_execute(self):
        obj = self.get_vote_object()
        klass = self.gdo_votes_table()
        vote = klass.blank({
            'vote_item': obj.get_id(),
            'vote_score': self.param_val('score'),
            'vote_reason': self.param_val('reason'),
        }).soft_replace()
        obj.recalculate_votes()
        await Application.EVENTS.publish('vote_casted', obj, vote)
        return self.msg('msg_vote_voted', (obj.render_name(), obj.get_votes_total(), obj.get_votes_score(), klass.table().gdo_max_vote_score()))

