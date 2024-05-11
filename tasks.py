import os
from invoke import task


@task
def start(ctx):
    print("Starting Outomaatti")
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    print("Running tests")
    ctx.run("OUTOMAATTI_RESOURCES__FILE_DATABASE=outomaatti-test.db python3 src/initialize_database.py", pty=True)
    ctx.run("OUTOMAATTI_RESOURCES__FILE_DATABASE=outomaatti-test.db pytest src", pty=True)
#    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    print("Checking the test coverage")
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task
def coverage_report(ctx):
    print("Generating the test report")
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    print("Linting")
    ctx.run("pylint src", pty=True)

@task
def format(ctx):
    print("Formatting code (press CTRL-C now if there are uncommitted changes)")
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def initdb(ctx):
    print("Initializing the database")
    ctx.run("python3 src/initialize_database.py")

@task
def clean(ctx):
    print("Cleaning up")
    ctx.run("rm -rf .coverage", pty=True)
    ctx.run("rm -rf htmlcov", pty=True)
    ctx.run("rm -rf .pytest_cache", pty=True)
    ctx.run("rm -rf outomaatti-test.db", pty=True)
    ctx.run("rm -rf snapshots", pty=True)
    ctx.run("pyclean --verbose .", pty=True)
