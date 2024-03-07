import click
from lmrag.createproject import createproject
from lmrag.runscript import run

@click.group()
def cli():
    pass

cli.add_command(createproject)
cli.add_command(run)

if __name__ == '__main__':
    cli()
