from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
        }

class Post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] =  mapped_column(ForeignKey("user.id"))
    title: Mapped[str] = mapped_column(String(140))
    content: Mapped[str] = mapped_column(String(500))

    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "content": self.content
        }


class Followers(db.Model):
    __tablename__ = "followers"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return{
            "id": self.id,
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }


class Comment(db.Model):
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(300))
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }
        
