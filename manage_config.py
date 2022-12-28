import json

CONFIG_FILE = 'config.json'

def write_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def read_config():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)