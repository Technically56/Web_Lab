"""Adds the sample users and posts to the database.

Run from the project folder, after `flask db upgrade`:

    python populate_db.py

It is safe to run more than once: records that already exist are skipped.
Passwords are stored as ready-made scrypt hashes, created with
werkzeug.security.generate_password_hash.
"""

import sys

import sqlalchemy as sa

from app import app, db
from app.models import Post, User

USERS = [
    {
        "username": "Ahmet",
        "email": "ahmet@mail.com",
        "password_hash": "scrypt:32768:8:1$ekmVsTd9HK4rWX4U$74dbac1b0e8bb198b2f256a82cc9a4339361a231292b43c7ee4c8b2a141e65db80972888c68f025463dcac9f9beabeaf923187e3c5c8fee3585582b41d7e5470",
    },
    {
        "username": "Kağan",
        "email": "kagan@mail.com",
        "password_hash": "scrypt:32768:8:1$pd7xmgXI5LN2mE0D$abc5d0b9ecba42924ecf5bbc6b5a3823277f6e232118fce5291ce9f0b0d16829cb875579be7b48828f4c96b4e6f0298bfcd0ac0e747b24d2ceb1ff66fd190690",
    },
]

POSTS = [
    {"author": "Ahmet", "body": "my first post!"},
]


def create_users():
    for data in USERS:
        query = sa.select(User).where(User.username == data["username"])
        if db.session.scalar(query) is None:
            db.session.add(User(**data))
    db.session.commit()


def create_posts():
    for data in POSTS:
        author = db.session.scalar(
            sa.select(User).where(User.username == data["author"])
        )
        query = author.posts.select().where(Post.body == data["body"])
        if db.session.scalar(query) is None:
            db.session.add(Post(body=data["body"], author=author))
    db.session.commit()


if __name__ == "__main__":
    # Windows may not be able to print Turkish characters such as 'ğ' otherwise.
    sys.stdout.reconfigure(encoding="utf-8")

    with app.app_context():
        create_users()
        create_posts()
        print("Users:", db.session.scalars(sa.select(User)).all())
        print("Posts:", db.session.scalars(sa.select(Post)).all())
