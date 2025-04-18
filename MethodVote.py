from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Object import GDT_Object
from gdo.vote.WithVotes import WithVotes


class MethodVote(WithVotes, Method):

    def gdo_parameters(self) -> [GDT]:
        table = self.gdo_vote_table()
        return [
            table.column('vote_reason').copy_as('reason'),
            GDT_Object('id').not_null().table(table),
            table.column('vote_score').copy_as('score').initial(str(table.gdo_max_vote_score())),
        ]
