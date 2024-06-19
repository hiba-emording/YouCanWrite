#!/usr/bin/python3
"""Define API routes for posts, comments, likes, writing challange & tips"""
from flask import Blueprint, request, jsonify
from .models import Post, User, Comment, db, Tip, Challenge, ChallengeResponse
from . import bcrypt


api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to YouCanWrite API'}), 200


@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200


@api.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'],
                    content=data['content'], user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201


@api.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify(post.to_dict()), 200


@api.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted'}), 200


@api.route('/posts/<post_id>/comments', methods=['GET'])
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([comment.to_dict() for comment in comments]), 200


@api.route('/posts/<post_id>/comments', methods=['POST'])
def create_comment(post_id):
    data = request.get_json()
    new_comment = Comment(
        post_id=post_id,
        user_id=data['user_id'],
        content=data['content']
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(new_comment.to_dict()), 201


@api.route('/comments/<comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.get_json()
    comment = Comment.query.get(comment_id)
    if not comment:
        return jsonify({'message': 'Comment not found'}), 404
    comment.content = data.get('content', comment.content)
    db.session.commit()
    return jsonify(comment.to_dict()), 200


@api.route('/comments/<comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return jsonify({'message': 'Comment not found'}), 404
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted'}), 200


@api.route('/posts/<post_id>/likes', methods=['POST'])
def add_like(post_id):
    data = request.get_json()
    new_like = Like(post_id=post_id, user_id=data['user_id'])
    db.session.add(new_like)
    db.session.commit()
    return jsonify(new_like.to_dict()), 201


@api.route('/posts/<post_id>/likes', methods=['DELETE'])
def remove_like(post_id):
    data = request.get_json()
    like = Like.query.filter_by(
            post_id=post_id, user_id=data['user_id']).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return jsonify({'message': 'Like removed'}), 200
    return jsonify({'message': 'Like not found'}), 404


@api.route('/challenges', methods=['GET'])
def get_challenges():
    challenges = Challenge.query.all()
    return jsonify([challenge.to_dict() for challenge in challenges]), 200


@api.route('/challenges/daily', methods=['GET'])
def get_daily_challenge():
    try:
        challenge = Challenge.query.order_by(Challenge.created_at.desc()).first()
        if challenge:
            return jsonify(challenge.to_dict()), 200
        else:
            return jsonify({'message': 'No daily challenge available'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@api.route('/challenges/<challenge_id>/responses', methods=['GET'])
def get_challenge_responses(challenge_id):
    challenge = Challenge.query.get_or_404(challenge_id)
    return jsonify([response.to_dict() for response in challenge.responses]), 200


@api.route('/challenges/<challenge_id>/responses', methods=['POST'])
def create_challenge_response(challenge_id):
    data = request.get_json()
    new_response = ChallengeResponse(
        challenge_id=challenge_id,
        user_id=data['user_id'],
        content=data['content']
    )
    db.session.add(new_response)
    db.session.commit()
    return jsonify(new_response.to_dict()), 201


@api.route('/challenges/<challenge_id>/responses/<response_id>', methods=['PUT'])
def update_challenge_response(challenge_id, response_id):
    data = request.get_json()
    response = ChallengeResponse.query.filter_by(id=response_id, challenge_id=challenge_id).first()
    if not response:
        return jsonify({'message': 'Response not found'}), 404
    response.content = data.get('content', response.content)
    db.session.commit()
    return jsonify(response.to_dict()), 200


@api.route('/challenges/<challenge_id>/responses/<response_id>', methods=['DELETE'])
def delete_challenge_response(challenge_id, response_id):
    response = ChallengeResponse.query.filter_by(id=response_id, challenge_id=challenge_id).first()
    if not response:
        return jsonify({'message': 'Response not found'}), 404
    db.session.delete(response)
    db.session.commit()
    return jsonify({'message': 'Response deleted'}), 200


@api.route('/tips', methods=['GET'])
def get_tips():
    tips = Tip.query.all()
    return jsonify([tip.to_dict() for tip in tips]), 200


@api.route('/tips/daily', methods=['GET'])
def get_daily_tip():
    try:
        tip = Tip.query.order_by(Tip.created_at.desc()).first()
        if tip:
            return jsonify(tip.to_dict()), 200
        else:
            return jsonify({'message': 'No daily tip available'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
