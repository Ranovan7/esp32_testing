from getpass import getpass

from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from project.models import User
from project import app, socketio  # , db

# migrate = Migrate(app, db)
manager = Manager(app)

# migrations
# manager.add_command('db', MigrateCommand)


# @manager.command
# def create_admin():
#     username = input("enter username: ")
#     password = getpass("enter password: ")
#
#     user = User(
#         username=username,
#         password=password,
#         is_admin=True
#     )
#     db.session.add(user)
#     db.session.commit()
#
#
# @manager.command
# def create_db():
#     """Creates the db tables."""
#     db.create_all()
#
#
# @manager.command
# def drop_db():
#     """Drops the db tables."""
#     db.drop_all()


@manager.command
def run():
    socketio.run(app)


if __name__ == '__main__':
    # manager.run()
    socketio.run(app)
