import sys

import sqlalchemy as sa

from app import app, db
from app.models import Post, User, Bookmark

USERS = [
    {
        "id": 1,
        "username": "Ahmet",
        "email": "ahmet@mail.com",
        "password_hash": "scrypt:32768:8:1$ekmVsTd9HK4rWX4U$74dbac1b0e8bb198b2f256a82cc9a4339361a231292b43c7ee4c8b2a141e65db80972888c68f025463dcac9f9beabeaf923187e3c5c8fee3585582b41d7e5470",
    },
    {
        "id": 2,
        "username": "Kağan",
        "email": "kagan@mail.com",
        "password_hash": "scrypt:32768:8:1$pd7xmgXI5LN2mE0D$abc5d0b9ecba42924ecf5bbc6b5a3823277f6e232118fce5291ce9f0b0d16829cb875579be7b48828f4c96b4e6f0298bfcd0ac0e747b24d2ceb1ff66fd190690",
    },
    {

        "id": 3,
        "username": "Mehmet",
        "email": "mehmet@mail.com",
        "password_hash": "scrypt:32768:8:1$pd7xmgXI5LN2mE0D$abc5d0b9ecba42924ecf5bbc6b5a3823277f6e232118fce5291ce9f0b0d16829cb875579be7b48828f4c96b4e6f0298bfcd0ac0e747b24d2ceb1ff66fd190690",
    }
]

POSTS = [
    {"id": 1, "author": "Ahmet", "body": "my first post!"},
    {"id": 2, "author": "Ahmet", "body": "my second post!"},
    {"id": 3, "author": "Kağan", "body": "my first post!"},
    {"id": 4, "author": "Kağan", "body": "my second post!"},
    {"id": 5, "author": "Mehmet", "body": "my first post!"},
    {"id": 6, "author": "Mehmet", "body": "my second post!"},
]


BOOKMARKS = [
    {"user_id": 2, "post_id": 1},  # Kağan -> Ahmet's first post
    {"user_id": 2, "post_id": 2},  # Kağan -> Ahmet's second post
    {"user_id": 1, "post_id": 3},  # Ahmet -> Kağan's first post
    {"user_id": 1, "post_id": 4},  # Ahmet -> Kağan's second post
    {"user_id": 3, "post_id": 1},  # Mehmet -> Ahmet's first post
    {"user_id": 3, "post_id": 2},  # Mehmet -> Ahmet's second post
    {"user_id": 3, "post_id": 3},  # Mehmet -> Kağan's first post
    {"user_id": 3, "post_id": 4},  # Mehmet -> Kağan's second post
]

def create_users():
    for data in USERS:
        if db.session.get(User, data["id"]) is None:
            db.session.add(User(**data))
    db.session.commit()


def create_posts():
    for data in POSTS:
        author = db.session.scalar(
            sa.select(User).where(User.username == data["author"])
        )
        if db.session.get(Post, data["id"]) is None:
            db.session.add(Post(id=data["id"], body=data["body"], author=author))
    db.session.commit()


def create_bookmarks():
    """LEGACY: quick implementation written under time pressure. Not used.

    Not sustainable, so create_dummy_bookmarks() replaced it. It derives the
    bookmarks from the data instead of declaring them: for each post it picks
    an arbitrary other user (first match, so ambiguous with 3+ users) and
    bookmarks it only if that user has a post with the same body. That only
    works because the sample posts happen to share identical text. Kept for
    reference; use create_dummy_bookmarks() and edit BOOKMARKS instead.
    """
    posts =db.session.scalars(sa.select(Post)).all()

    for post in posts:
        author = db.session.scalar(
            sa.select(User).where(User.username != post.author.username)
        )
        query = author.posts.select().where(Post.body == post.body)
        if db.session.scalar(query) is not None:
            exists = db.session.scalar(
                sa.select(Bookmark).where(
                    Bookmark.user_id == author.id, Bookmark.post_id == post.id
                )
            )
            if exists is None:
                db.session.add(Bookmark(user_id=author.id, post_id=post.id))
    db.session.commit()


def create_dummy_bookmarks():
    """Create the bookmarks listed in BOOKMARKS, skipping ones that exist."""
    for data in BOOKMARKS:
        exists = db.session.scalar(
            sa.select(Bookmark).where(
                Bookmark.user_id == data["user_id"],
                Bookmark.post_id == data["post_id"],
            )
        )
        if exists is None:
            db.session.add(Bookmark(**data))
    db.session.commit()


def wipe():
    """Delete all rows but keep the tables, so alembic_version stays valid.

    Children are deleted before parents because of the foreign keys.
    """
    for model in (Bookmark, Post, User):
        db.session.execute(sa.delete(model))
    db.session.commit()


def print_table(title, headers, rows):
    """Print rows as an aligned text table under a title with a row count."""
    rows = [[str(cell) for cell in row] for row in rows]
    widths = [
        max(len(h), *(len(row[i]) for row in rows)) if rows else len(h)
        for i, h in enumerate(headers)
    ]
    print(f"\n{title} ({len(rows)})")
    print("  ".join(h.ljust(w) for h, w in zip(headers, widths)))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print("  ".join(cell.ljust(w) for cell, w in zip(row, widths)))


def show():
    """Print users, posts and bookmarks as readable tables."""
    users = db.session.scalars(sa.select(User).order_by(User.id)).all()
    print_table(
        "Users", ["id", "username", "email"],
        [(u.id, u.username, u.email) for u in users],
    )

    posts = db.session.scalars(sa.select(Post).order_by(Post.id)).all()
    print_table(
        "Posts", ["id", "author", "body", "timestamp"],
        [(p.id, p.author.username, p.body, p.timestamp) for p in posts],
    )

    bookmarks = db.session.scalars(sa.select(Bookmark).order_by(Bookmark.id)).all()
    users_by_id = {u.id: u.username for u in users}
    print_table(
        "Bookmarks", ["id", "user", "post", "post author", "post body", "timestamp"],
        [
            (
                b.id,
                f"{b.user_id} {users_by_id.get(b.user_id, '?')}",
                b.post_id,
                b.post.author.username,
                b.post.body,
                b.timestamp,
            )
            for b in bookmarks
        ],
    )


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1:] == ["wipe"]:
        with app.app_context():
            uri = app.config["SQLALCHEMY_DATABASE_URI"]
            if input(f"Delete ALL users, posts and bookmarks in {uri}? [y/N] ").lower() == "y":
                wipe()
                print("Wiped.")
            else:
                print("Cancelled.")
    elif sys.argv[1:] == ["show"]:
        with app.app_context():
            show()
    else:
        with app.app_context():
            create_users()
            create_posts()
            create_dummy_bookmarks()



       