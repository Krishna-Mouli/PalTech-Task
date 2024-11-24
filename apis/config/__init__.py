import yaml
import os

def load_config(environment):
    config_file = f"{os.path.dirname(__file__)}/{environment}config.yml"
    
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    
    return config
