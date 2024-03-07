import os
import click
import yaml

@click.command()
@click.argument('script_name')
@click.option('--secret-key', default=None, help='Your name to override the one in config.yaml')
def run(script_name, secret_key):
    """
    Runs the specified script with an optional name override.
    """
    script_path = os.path.join(os.getcwd(), script_name)

    if not os.path.exists(script_path):
        click.echo(f"Error: Script '{script_name}' not found.")
        return

    if not os.path.isfile(script_path):
        click.echo(f"Error: '{script_name}' is not a file.")
        return

    if not script_name.endswith('.py'):
        click.echo("Error: Only Python scripts (.py) are supported.")
        return

    project_path = os.path.dirname(script_path)


    config_yaml_path = os.path.join(project_path, 'rag', 'config', 'config.yaml')
    if os.path.exists(config_yaml_path):
        with open(config_yaml_path, 'r') as f:
            config_data = yaml.safe_load(f)


        if secret_key is not None:
            config_data['name'] = secret_key


        name_to_use = config_data.get('name', 'default_name')
        click.echo(f"Running script '{script_name}' with name: {name_to_use}")
    else:
        click.echo(f"Error: config.yaml not found in '{project_path}'.")

if __name__ == "__main__":
    run()

