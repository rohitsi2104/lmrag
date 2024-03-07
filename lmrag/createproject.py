import click
import os
import shutil
import subprocess


def get_project_skeleton_path():
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    project_skeleton_path = os.path.join(script_directory, 'project_skleton')
    return project_skeleton_path

@click.command()
@click.argument('dest_path')
@click.option('--secret-key', default=None, help='Secret key to overwrite .yaml file')
def createproject(dest_path, secret_key):
    source_path = get_project_skeleton_path()

   
    dest_path = os.path.abspath(dest_path)

    try:
       
        os.makedirs(dest_path, exist_ok=True)

        
        for item in os.listdir(source_path):
            s = os.path.join(source_path, item)
            d = os.path.join(dest_path, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks=True, ignore=shutil.ignore_patterns('*.yaml'))
            else:
                shutil.copy2(s, d)

        
        if secret_key is not None:
            yaml_file_path = os.path.join(dest_path, 'rag', 'config','config.yaml')
            with open(yaml_file_path, 'w') as yaml_file:
                yaml_file.write(f'secret_key: {secret_key}')

        
        script_path_chat = os.path.join(dest_path, 'chat.py')
        subprocess.run(['streamlit', 'run', script_path_chat])

        click.echo(f"Project created successfully at '{dest_path}'.")
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    createproject()



# lmrag createproject rohit/dest/path --secret-key "abc123"