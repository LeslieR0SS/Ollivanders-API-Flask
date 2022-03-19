from mongoengine import *
from flask.cli import with_appcontext
from flask import g
import click
from repository.db_uri import DB, HOST
from repository.items import items

from repository.schema import Ollivanders


def get_bd(db_name, host_url):
    """
    Se conecta a una base de datos y la devuelve al objeto grlobal g de Flask
    """
    if "db" not in g:
        g.db = connect(
            db=db_name,
            host=host_url,
        )
        g.Ollivanders = Ollivanders
    return g.db


def close_db(e=None):
    g.pop("db", None)
    connection = g.pop("connection", None)

    if connection is not None:
        connection.close()


def init_db(db_name, host_url):
    db = get_bd(db_name, host_url)
    for item in items:
        print(item)
        Ollivanders(
            name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
        ).save()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db(DB, HOST)
    click.echo("Data Base initialized")


def init_app(app, db_name, host_url):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
