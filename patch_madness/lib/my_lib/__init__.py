__all__ = ["my_fun"]

from patch_madness.config.config import Configuration
from patch_madness.lib.lib_thing import function_factory

my_fun = function_factory(conf=Configuration)
