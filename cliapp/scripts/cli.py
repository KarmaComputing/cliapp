import click


@click.group()
def cli():
    pass

@cli.command()
def install():
    """Install the program"""
    click.echo('Installing...')

@cli.command()
def run():
    """Run the program"""
    click.echo('Running...')

@cli.command()
@click.argument('platform', required=True) 
def deploy():
    """Deploy the program"""
    click.echo('Deploying...')
