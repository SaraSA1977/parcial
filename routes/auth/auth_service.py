from db.db import SessionLocal
from db.models import User

def create_user(data):
    db = SessionLocal()

    user = User(
        email=data["email"],
        password=data["password"]
    )

    db.add(user)
    db.commit()
    db.close()

    return user


def login_user(data):
    db = SessionLocal()

    user = db.query(User).filter(User.email == data["email"]).first()

    if user and user.password == data["password"]:
        return user

    return None