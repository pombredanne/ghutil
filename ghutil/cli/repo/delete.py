import click
from   ghutil.local import get_remote_url
from   ghutil.types import GHRepo

@click.command()
@click.confirmation_option(prompt='Delete this repository?')
@click.argument('repo', type=GHRepo(), default=get_remote_url)
@click.pass_obj
def cli(gh, repo):
    """ Delete a repository """
    repo.delete()
