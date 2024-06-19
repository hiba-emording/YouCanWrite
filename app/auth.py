#!/usr/bin/python3
"""authentication and user profile routes"""
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.extensions import db
from . import bcrypt
import logging

auth = Blueprint('auth', __name__)
logging.basicConfig(level=logging.DEBUG)


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'],
                    email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Registered successfully'}), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if not user.check_password(data['password']):
        return jsonify({'message': 'Incorrect password'}), 401

    return jsonify({'message': 'Login successful'}), 200


@auth.route('/logout', methods=['GET'])
def logout():
    response = jsonify({'message': 'Logged out successfully'})
    response.set_cookie('session_token', '', expires=0)
    return response, 200


@auth.route('/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({
        'username': user.username,
        'email': user.email,
        'bio': user.bio,
        'profile_picture': user.profile_picture
    })


@auth.route('/profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    user.bio = data.get('bio', user.bio)
    user.profile_picture = data.get('profile_picture', user.profile_picture)

    db.session.commit()

    return jsonify({'message': 'Profile updated successfully'})
