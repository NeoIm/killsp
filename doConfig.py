# -*- coding:utf-8 -*-

import configparser
import os

class ConfigProcessor:

    configFileName = 'config.ini'
    sectionLang = 'Language'
    optionLang = 'language'

    valueEn = 'en'
    valueZh = 'zh'

    def __init__(self):
        self.config = configparser.ConfigParser()

        # 判断是否存在配置文件，不存在则创建
        if(not os.path.isfile(self.configFileName)):
            self.config[self.sectionLang] = {self.optionLang: self.valueZh}

            try:
                with open(self.configFileName, 'w') as configFile:
                    self.config.write(configFile)
            except Exception as e:
                print(e)

        self.config.read(self.configFileName)

    # 将值设置到配置文件
    def setCongfig(self, value, section=sectionLang, option=optionLang):
        self.config.set(section, option, value)
        try:
            self.config.write(open(self.configFileName, 'w'))
        except Exception as e:
            print(e)

    # 读取配置文件的值
    def readConfig(self, section=sectionLang, option=optionLang):
        lang = None
        try:
            lang = self.config.get(section, option)
        except Exception as e:
            print(e)

        return lang


if __name__ == "__main__":
    processor = ConfigProcessor()
    result = processor.readConfig("Language", "language")
    print(result)

    processor.setCongfig("Language", "language", "en")
    result = processor.readConfig("Language", "language")

    print(result)