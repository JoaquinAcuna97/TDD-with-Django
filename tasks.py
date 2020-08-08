from invoke import task
import time
from urllib.request import urlopen


@task
def create(ctx, docs=False, bytecode=False, extra=""):
    ctx.run("python -m django --version")
    ctx.run("django-admin startproject djangotest .")
    ctx.run("python manage.py migrate")
    # Start application.
    time.sleep(1)
    ctx.run("python manage.py runserver")
    time.sleep(1)
    # Test if the site works well.
    with urlopen("http://127.0.0.1:8000/ ") as response:
        if not response.getcode() == 200:
            sys.exit("CRITICAL: The site respond CODE " + response.getcode())
    # Success!
    print("App created succeeded.")


@task
def deploy(ctx):
    ctx.run("git fetch")
    ctx.run("git pull")
    ctx.run("pip install -r requirements.txt")
    ctx.run("python manage.py makemigrations")
    ctx.run("python manage.py migrate")
    # Start application.
    ctx.run("python manage.py runserver")
    time.sleep(1)
    # Test if the site works well.
    with urlopen("http://localhost:8000") as response:
        if not response.getcode() == 200:
            sys.exit("CRITICAL: The site respond CODE " + response.getcode())
    # Success!
    print("Deploy succeeded.")
