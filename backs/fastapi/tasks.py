# This is a workaround because pipenv does not support chained scripts,
# use invoke to do that
# https://github.com/pypa/pipenv/issues/2283
# type: ignore
from invoke import task


@task
def format(c):
    c.run("pipenv run format-black", env={"PIPENV_DONT_LOAD_ENV": "1"})
    c.run("pipenv run format-autoflake", env={"PIPENV_DONT_LOAD_ENV": "1"})
    c.run("pipenv run format-isort", env={"PIPENV_DONT_LOAD_ENV": "1"})


@task
def lint(c):
    c.run("pipenv run lint-black", env={"PIPENV_DONT_LOAD_ENV": "1"})
    c.run("pipenv run lint-isort", env={"PIPENV_DONT_LOAD_ENV": "1"})
    c.run("pipenv run lint-flake8", env={"PIPENV_DONT_LOAD_ENV": "1"})
    c.run("pipenv run lint-mypy", env={"PIPENV_DONT_LOAD_ENV": "1"})
