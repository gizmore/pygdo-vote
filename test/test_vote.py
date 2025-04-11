import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Render import Render, Mode
from gdo.core.Connector import Connector
from gdo.core.GDO_Server import GDO_Server
from gdotest.TestUtil import reinstall_module, text_plug, GDOTestCase, cli_plug, cli_gizmore


class TelegramTestCase(GDOTestCase):

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        reinstall_module('vote')
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        loader.init_cli()

    def test_01_cli_poll(self):
        giz = cli_gizmore()
        out = cli_plug(giz, '$poll "Who is major?" "" ')
        self.assertIn('created', out, "Poll was not created.")

    def test_02_render_telegram(self):
        out = text_plug(Mode.TELEGRAM, '$help')
        self.assertIn('Core', out, 'Telegram does not render help nicely.')
        self.assertNotIn('[0m', out, 'Telegram does render as CLI.')

    def test_03_channel_creation(self):
        server = GDO_Server.get_by_connector('Telegram')
        channel1 = server.get_or_create_channel(str(-4139465915), 'WeChall')
        channel2 = server.get_or_create_channel(str(-4139465915), 'WeChall')
        self.assertEqual(channel1, channel2, 'Channel cannot be gotten from memory.')
