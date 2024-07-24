import configparser
import os
from utils.logger import LOGGER

class ConfigReaderUtil:
    global config

    '''
    Set the config parser and read the variables from config file
    section_name is optional parameter and default is "env" (Change is want to read from any other option)
    ini_location is optional parameter and default is "\\resources\\configuration.ini" (Change if .ini location is different)
    '''
    @staticmethod
    def set_config(section_name="env", ini_location="\\resources\\configuration.ini"):
        ConfigReaderUtil.ini_location = ini_location
        ConfigReaderUtil.section_name = section_name
        ConfigReaderUtil.config = configparser.ConfigParser()
        file_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(file_directory) + ConfigReaderUtil.ini_location
        ConfigReaderUtil.config.read(parent_directory)
        try:
            ConfigReaderUtil.config = configparser.ConfigParser()
            file_directory = os.path.dirname(os.path.abspath(__file__))
            parent_directory = os.path.dirname(file_directory) + ConfigReaderUtil.ini_location
            ConfigReaderUtil.config.read(parent_directory)
        except Exception as ex:
            print(ex)

    '''
    Returns the value for key present in configuration.ini file
    '''
    @staticmethod
    def get_env_value(key_name):
        #return ConfigReaderUtil.config[ConfigReaderUtil.section_name][key_name]
        try:
            value = ConfigReaderUtil.config[ConfigReaderUtil.section_name][key_name]
            return value
        except KeyError:
            print("Key is not present in configuration file")
        except AttributeError:
            print("Config parser is not set")
        except Exception as ex:
            print(ex)
