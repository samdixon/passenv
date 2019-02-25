import click
from . import api
from .config import Config


c = Config("1password")


@click.group()
def Cli():
    pass


# Create new key or project command
@Cli.command()
@click.option("--name")
@click.option("--key")
@click.option("--project")
def create(name, key, project):
    api.Create(name, project, key, c.password_manager)


# List key or project or all
@Cli.command()
@click.option(
    "--force-remote-update", "-update", help="Force remote update of projects/keys"
)
@click.option("--active-only")
def list(force_remote_update, active_only):
    api.List(force_remote_update, active_only)


@Cli.command()
def delete():
    print("delete")
