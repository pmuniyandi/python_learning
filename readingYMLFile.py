import yaml

ymlname="/Users/munperum/PycharmProjects/training/data/data.yml"


with open(ymlname) as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)

print(dataMap)