# -*- coding: utf-8 -*-
"""Basic for load save and add item for toml config file

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from tomlconfig import TomlConfig

class Config(TomlConfig):
    """Config parser for program"""
    defaultfile = os.path.join(os.path.dirname(__file__), "config.toml")
    _current = None
    def __init__(self, cfgfile=None):
        super().__init__()
        if cfgfile is None:
            cfgfile = Config.defaultfile
        self.file = cfgfile
        if os.path.exists(cfgfile):
            if self.read(cfgfile):
                print('config file "{}" load successed!'.format(cfgfile))
                return
            else:
                print('config file "{}" load failed!'.format(cfgfile))

        s = """[general]

        [editor]

        """
        self.readString(s)

    @classmethod
    def current(cls):
        if isinstance(Config._current, Config):
            return Config._current
        else:
            Config._current = Config()
            return Config._current

    def saveDefault(self):
        if self.save(self.file):
            print("config file saved.")
        else:
            print("config file save failed.")
