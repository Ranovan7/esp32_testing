# import datetime
#
# from project import app, db, bcrypt, login
# from sqlalchemy.orm import relationship
#
# types = {
#     '1': 'auth',
#     '2': 'refresh'
# }
#
#
# class User(db.Model):
#     """ User Model for storing user related details """
#     __tablename__ = "users"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.Text, unique=True, nullable=False)
#     password = db.Column(db.Text, nullable=False)
#     is_admin = db.Column(db.Boolean, default=False)
#     last_activity = db.Column(db.DateTime, nullable=True)
#     email = db.Column(db.Text, nullable=True)
#
#     roles = relationship('UserRole', back_populates='user')
#
#     def __init__(self, username, password, role_ids=[]):
#         self.username = username
#         self.set_password(password)
#         self.registered_on = datetime.datetime.now()
#         self.is_active = True
#         self.add_roles(role_ids)
#
#     def set_password(self, password):
#         self.password = bcrypt.generate_password_hash(
#             password, app.config.get('BCRYPT_LOG_ROUNDS')
#         ).decode()
#
#     def check_password(self, password):
#         """
#         Check User password
#         """
#         return bcrypt.check_password_hash(
#             self.password, password
#         )
#
#
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
