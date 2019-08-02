import configparser
import sys

class ConfigReader(configparser.SafeConfigParser):

    def __init__(self):
        configparser.SafeConfigParser.__init__(self)
        self.load_config()

    @classmethod
    def get_config_file(cls):
        config_files = []
        default_config = '/Users/amardip.kumar/Documents/AuctionAPI/src/service/config.cfg'
        config_files.append(default_config)
        return config_files

    def load_config(self):
        config_files = self.get_config_file()
        self.read(config_files)
    
    def read_config(self, arg, section):
        value = self.get(section, arg)
        return value


class _FakeModule(object):
    
    def get_reader(self):
        return ConfigReader()

    def read(self, section, arg):
        return self.get_reader().get(section, arg)
sys.modules[__name__] = _FakeModule()
    
    

    

        
