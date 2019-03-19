import click
import jenkins
import os

@click.group()
def cli():
    pass

@click.command()
@click.argument('keyword')
def find(keyword):
    click.echo('List all jobs with name contains a keyword: %s' %keyword)
    click.echo(list_job_by_keyword(keyword))

@click.command()
@click.argument('job_name')
def build(job_name):
    click.echo('Trigger build for job: %s' %job_name)
    build_job(job_name)

cli.add_command(find)
cli.add_command(build)

JENKINS_HOST_ADDR = "http://18.237.198.223:8080"

JENKINS_USER = os.environ['JENKINS_USER']
JENKINS_PASSWORD = os.environ['JENKINS_PASSWORD']
server = jenkins.Jenkins(JENKINS_HOST_ADDR, username=JENKINS_USER, password=JENKINS_PASSWORD)
jobs = server.get_jobs(view_name='All')

def list_job_by_keyword(keyword):
    list_jobs = []
    for job in jobs:
        job_fullname = job['fullname']
        if keyword in job_fullname:
            list_jobs.append(job_fullname)
    return list_jobs

def build_job(job_name):
    server.build_job(job_name)

if __name__ == '__main__':
    cli()

