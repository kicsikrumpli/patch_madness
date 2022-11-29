from patch_madness.config.config import Configuration


def function_factory(conf=Configuration):
    def _fun():
        return conf.FOO
    return _fun
