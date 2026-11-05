from datetime import UTC, datetime

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True, index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, index=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped["Post"] = so.relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"<User {self.username}>"


class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(
        sa.Integer, sa.ForeignKey(User.id), index=True
    )
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime, index=True, default=lambda: datetime.now(UTC)
    )
    author: so.Mapped[User] = so.relationship(back_populates="posts")

    def __repr__(self):
        return f"<Post {self.body}>"


class Bookmark(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(
        sa.Integer, sa.ForeignKey(User.id), index=True)
    post_id: so.Mapped[int] = so.mapped_column(
        sa.Integer, sa.ForeignKey(Post.id), index=True)
    timestamp: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime, index=True, default=lambda: datetime.now(UTC)
    )
    post: so.Mapped[Post] = so.relationship()