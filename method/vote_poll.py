from gdo.base.GDT import GDT
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_Object import GDT_Object
from gdo.core.GDT_Repeat import GDT_Repeat
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.vote.GDO_Poll import GDO_Poll
from gdo.vote.GDO_PollChoice import GDO_PollChoice
from gdo.vote.GDT_PollChoice import GDT_PollChoice


class vote_poll(MethodForm):
    
    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Object('poll').not_null().table(GDO_Poll.table()),
        ]

    def get_poll_id(self):
        return self._raw_args.get_val('poll')[0]

    def get_poll(self) -> GDO_Poll:
        return GDO_Poll.table().get_by_aid(self.get_poll_id())

    def gdo_create_form(self, form: GDT_Form) -> None:
        poll = self.get_poll()
        for choice in poll.get_choices():
            form.add_field(GDT_PollChoice(f"pc{choice.get_id()}"))
        super().gdo_create_form(form)

    def form_submitted(self):
        self.clear_form()
