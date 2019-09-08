#参考に過ぎないので、修正してもらって構いません

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name
