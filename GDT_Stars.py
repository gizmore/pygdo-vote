from gdo.core.GDT_Template import GDT_Template
from gdo.core.GDT_UInt import GDT_UInt


class GDT_Stars(GDT_UInt):

    MODE_FULL = 1
    MODE_COMPACT = 2
    MODE_MINI = 3

    _mode: int

    def __init__(self, name: str):
        super().__init__(name)
        self.icon('star')
        self._mode = self.MODE_FULL
        self.bytes(1)
        self.min(0)
        self.max(5)

    def star_mode(self, mode: int):
        self._mode = mode
        return self

    def render_cell(self) -> str:
        if self._mode == self.MODE_FULL:
            return GDT_Template.python('vote', 'cell_stars_full.html', {'field': self})
        elif self._mode == self.MODE_COMPACT:
            return GDT_Template.python('vote', 'cell_stars_compact.html', {'field': self})
        elif self._mode == self.MODE_MINI:
            return GDT_Template.python('vote', 'cell_stars_mini.html', {'field': self})
        else:
            return super().render_cell()

    def render_form(self) -> str:
        return GDT_Template.python('vote', 'form_stars.html', { 'field': self })