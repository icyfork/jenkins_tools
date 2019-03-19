import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('keyword')
def find(keyword):
    click.echo('List all jobs with name contains a keyword: %s' %keyword)
    list_job_by_keyword()

@click.command()
@click.argument('job_name')
def build(job_name):
    click.echo('Trigger build for job: %s' %job_name)
    build_job()

cli.add_command(find)
cli.add_command(build)


jenkins_user = os.environ['JENKINS_USER']
jenkins_password = os.environ['JENKINS_PASSWORD']

def list_job_by_keyword():
    pass

def build_job():
    pass

if __name__ == '__main__':
    cli()

