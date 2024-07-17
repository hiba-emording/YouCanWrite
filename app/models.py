#!/usr/bin/python3
"""Define DB models: User, Post, Comment, Like, Challenge, Tip"""
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship, backref
from .extensions import db


class User(db.Model, UserMixin):
    """User model to store user-related information"""
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    email_confirmed = Column(db.Boolean, default=False) 
    bio = Column(Text, nullable=True)
    profile_picture = Column(String(1024), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship('Post', back_populates='author', lazy=True)
    liked_posts = relationship('Like', back_populates='user', lazy=True)
    comments = relationship('Comment', back_populates='user', lazy=True)


    def to_dict(self):
        """Convert the User object to a dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'bio': self.bio,
            'profile_picture': self.profile_picture,
            'created_at': self.created_at.isoformat()
        }


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)


    def set_password(self, password):
        """Hash the password and store it in the password_hash field"""
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')


    def verify_password(self, password):
        """Verify the provided password against the stored password hash"""
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    """Post model to store post-related information"""
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String(120), nullable=False)
    image_url = Column(String(1024), nullable=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post', lazy=True, cascade='all, delete-orphan')
    likes = relationship('Like', back_populates='post', lazy=True, cascade='all, delete-orphan')


    def to_dict(self):
        """Convert the Post object to a dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'image_url': self.image_url,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'comments': [comment.to_dict() for comment in self.comments],
            'likes': [like.to_dict() for like in self.likes],
            'likes_count': self.count_likes()
        }


    def count_likes(self):
        """Count the number of likes for the post"""
        return len(self.likes)


class Comment(db.Model):
    """Comment model to store comment-related information"""
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')


    def to_dict(self):
        """Convert the Comment object to a dictionary"""
        return {
            'id': self.id,
            'post_id': self.post_id,
            'user_id': self.user_id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'user': self.user.to_dict()
        }


class Like(db.Model):
    """Like model to store like-related information"""
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='liked_posts')
    post = relationship('Post', back_populates='likes')


    def to_dict(self):
        """Convert the Like object to a dictionary"""
        return {
            'id': self.id,
            'post_id': self.post_id,
            'user_id': self.user_id,
            'user': self.user.to_dict(),
            'created_at': self.created_at.isoformat()
        }


class Challenge(db.Model):
    """Challenge model to store writing challenge-related information"""
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


    def to_dict(self):
        """Convert the Challenge object to a dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
        }


class Tip(db.Model):
    """Tip model to store writing tips-related information"""
    id = Column(Integer, primary_key=True)
    tip = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


    def to_dict(self):
        """Convert the Tip object to a dictionary"""
        return {
            'id': self.id,
            'tip': self.tip,
            'created_at': self.created_at.isoformat()
        }
