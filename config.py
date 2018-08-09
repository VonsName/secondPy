# __author:  Administrator
# __date:  2018/8/9/009

import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'ServerAliveInterval': 45}
config['tes.org'] = {'User': 'lisi'}


with open('example.ini', 'w') as configfile:
    config.write(configfile)
