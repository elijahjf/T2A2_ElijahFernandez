from flask import Blueprint
from init import db, bcrypt
from models.florists import Florists

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
    florists = [
        Florists(
            name="Michael Scott",
            username="michaelscott.admin",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8"),
            is_senior=True
        ),
        Florists(
            name="Angela Martin",
            username="angelamartin",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8"),
            is_senior=True          
        ),
        Florists(
            name="Erin Hannon",
            username="erinhannon",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8")        
        ),
        Florists(
            name="Kevin Malone",
            username="kevinmalone",
            password=bcrypt.generate_password_hash("hunter2").decode("utf-8")          
        )
    ]

    db.session.add_all(florists)
    db.session.commit()

    print("tables seeded")