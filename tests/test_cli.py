import unittest
from contexts import cli


class TestCli(unittest.TestCase):

    def test_cli_entry(self):
        c = cli.Cli()
