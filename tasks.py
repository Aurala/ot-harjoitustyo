from invoke import task

# FIX: Descriptions for each task

@task
def start(c):
    print("Starting Outomaatti")
    c.run("python3 src/index.py", pty=True)

@task
def test(c):
    print("Running tests")
    c.run("pytest src", pty=True)

@task
def coverage(c):
    print("Checking the test coverage")
    c.run("coverage run --branch -m pytest src", pty=True)

@task
def coverage_report(c):
    print("Generating the test report")
    c.run("coverage html", pty=True)

@task
def lint(c):
    print("Linting")
    c.run("pylint src", pty=True)

@task
def format(c):
    print("Formatting code (press CTRL-C now if there are uncommitted changes)")
    c.run("autopep8 --in-place --recursive src", pty=True)

@task
def initdb(c):
    print("Initializing the database")
    c.run("python3 src/initialize_database.py")

@task
def clean(c):
    print("Cleaning up")
    c.run("rm -rf .coverage", pty=True)
    c.run("rm -rf htmlcov", pty=True)
    c.run("rm -rf .pytest_cache", pty=True)
    c.run("rm -rf *.db", pty=True)
    c.run("pyclean --verbose .")
