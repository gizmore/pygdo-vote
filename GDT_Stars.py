from gdo.core.GDT_Float import GDT_Float
from gdo.core.GDT_Template import GDT_Template


class GDT_Stars(GDT_Float):

    MODE_FULL = 1
    MODE_SLIM = 2
    MODE_MINI = 3

    _mode: int

    def __init__(self, name: str):
        super().__init__(name)
        self.icon('star')
        self._mode = self.MODE_FULL
        self.min(1)
        self.max(4)

    def star_mode(self, mode: int):
        self._mode = mode
        return self

    def html_star_render_mode(self) -> str:
        if self._mode == self.MODE_FULL:
            return ' full'
        elif self._mode == self.MODE_SLIM:
            return ' slim'
        elif self._mode == self.MODE_MINI:
            return ' mini'
        else:
            return ''

    def render_cell(self) -> str:
        return GDT_Template.python('vote', 'cell_stars.html', { 'field': self })

    def render_form(self) -> str:
        return GDT_Template.python('vote', 'form_stars.html', { 'field': self })
