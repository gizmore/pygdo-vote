import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import module_enabled
from gdo.vote.module_vote import module_vote
from gdotest.TestUtil import reinstall_module, text_plug, GDOTestCase, cli_plug, cli_gizmore


class VoteTestCase(GDOTestCase):
    """
    Nothing to test as this is a module that eases developing of other modules.
    Vote Tests are in pygdo-quote.
    """

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        reinstall_module('vote')
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        Application.init_cli()
        loader.init_cli()

    def test_01_cli_vote(self):
        reinstall_module('vote')
        reinstall_module('vote')
        self.assertTrue(module_vote.instance().gdo_value('module_enabled'), 'vote is not enabled via db.')
        self.assertTrue(module_enabled('vote'), 'vote is not enabled via loader.')
