from invoke import task

# FIX
@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

# FIX
@task
def test(ctx):
    ctx.run("pytest src", pty=True)

# FIX
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

# FIX
@task
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
