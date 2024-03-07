import click
from rag.service.hello_world import print_greeting

@click.command()
@click.option('--my_name', help="Your name to override the one in config.yaml")
def main(my_name):
    print_greeting(my_name)

if __name__ == '__main__':
    main()

 