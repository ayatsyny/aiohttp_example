from os.path import isfile
from envparse import env


if isfile('.env'):
    env.read_envfile('.env')


MYSQL_HOST = env.str('MYSQL_HOST')
MYSQL_DATABASE = env.str('MYSQL_DATABASE')
MYSQL_USER = env.str('MYSQL_USER')
MYSQL_PASSWORD = env.str('MYSQL_PASSWORD')
