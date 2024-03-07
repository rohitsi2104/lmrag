
import os
import yaml

def print_greeting(secret_key=None):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_yaml_path = os.path.join(script_directory, '..', 'config', 'config.yaml')

    if os.path.exists(config_yaml_path):
        with open(config_yaml_path, 'r') as f:
            config_data = yaml.safe_load(f)
            default_name = config_data.get('secret_key', 'Default_Name')
    else:
        default_name = 'Default_Name'

    name_to_print = secret_key or default_name
    print(f"Hello {name_to_print}!")
