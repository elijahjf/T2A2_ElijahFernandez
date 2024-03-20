from flask import Blueprint
from init import db, bcrypt
from models.users import Users

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        Users(
            name="Michael Scott",
            username="michaelscott.admin",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8"),
            is_admin=True
        ),
        Users(
            name="Angela Martin",
            username="angelamartin",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8")           
        ),
        Users(
            name="Erin Hannon",
            username="erinhannon",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8")        
        ),
        Users(
            name="Kevin Malone",
            username="kevinmalone",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8")          
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    print("tables seeded")