import unittest
from unittest.mock import patch

from patch_madness.config.config import Configuration


class TestMyLib(unittest.TestCase):
    class ConfigOverride(Configuration):
        FOO = "config override"

    class OtherConfigOverride(Configuration):
        FOO = "other config override"

    def test_regular(self):
        from patch_madness.lib.my_lib import my_fun

        val = my_fun()

        self.assertEqual(val, "my foo config value")

    @patch('patch_madness.config.config.Configuration', new=ConfigOverride)
    def test_with_patched_config(self):
        from patch_madness.lib.my_lib import my_fun

        val = my_fun()

        self.assertEqual(val, "config override")

    @patch('patch_madness.config.config.Configuration', new=OtherConfigOverride)
    def test_with_other_patched_config(self):
        from patch_madness.lib.my_lib import my_fun

        val = my_fun()

        self.assertEqual(val, "other config override")
