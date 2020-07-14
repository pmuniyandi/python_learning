
#loading lib
from configparser import ConfigParser
#object/mapping function
config = ConfigParser()
#giving my config fle location
configname="/Users/munperum/PycharmProjects/training/data/config.properties"
#using file handle/object reading content from file
config.read(configname)
#Reading specific values from file
value1 = (config.get('DEV','path1'))
value2 = (config.get('SIT','path1'))

#print(listfile(value1))
#displying data
print(value1)
print(value2)