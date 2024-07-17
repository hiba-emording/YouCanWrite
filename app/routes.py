#!/usr/bin/python3
"""Define API routes"""
from flask import Flask, flash, Blueprint, request, jsonify, render_template, redirect, url_for, session, current_app
from .models import db, Post, User, Comment, Like, Tip, Challenge
from sqlalchemy.orm import joinedload
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from .email_verify import send_confirmation_email, confirm_token
import logging

api = Blueprint('api', __name__, template_folder='templates')
logging.basicConfig(level=logging.DEBUG)


@api.route('/')
def index():
    """Render the pre-log page"""
    return render_template('index.html')


@api.route('/register', methods=['GET', 'POST'])
def show_register_form():
    """"Handle user registration and Render the registr form"""
    if request.method == 'POST':
        data = request.form
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            flash('Username already taken. Please choose a different one.', 'error')
            return redirect(url_for('api.show_register_form'))

        existing_email = User.query.filter_by(email=data['email']).first()
        if existing_email:
            flash('Email already registered. Please use a different email.', 'error')
            return redirect(url_for('api.show_register_form'))

        new_user = User(username=data['username'], email=data['email'], password=data['password'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        send_confirmation_email(new_user.email)
        flash('A confirmation email has been sent via email. Please check your inbox and spam folder.', 'info')
        return redirect(url_for('api.show_login_form'))
    return render_template('register.html')

@api.route('/confirm/<token>')
def confirm_email(token):
    """Confirm user's email using the token"""
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('api.show_login_form'))

    user = User.query.filter_by(email=email).first_or_404()
    if user.email_confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.email_confirmed = True
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('api.show_login_form'))


@api.route('/login', methods=['GET', 'POST'])
def show_login_form():
    """Render the login form"""
    if current_user.is_authenticated:
        return redirect(url_for('api.home'))
    
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(email=data['email']).first()
        if user and user.verify_password(data['password']):
            if not user.email_confirmed:
                flash('Please confirm your email to login.', 'error')
                return redirect(url_for('api.show_login_form'))
            
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('api.home'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('login.html')


@api.route('/logout')
@login_required
def logout():
    """Logout the user"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('api.show_login_form'))


@api.route('/home')
@login_required
def home():
    """Render the post-log:home page with posts and daily tip"""
    daily_tip = Tip.query.order_by(Tip.created_at.desc()).first()
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    posts_with_likes = Post.query.options(joinedload(Post.likes)).all()
    sorted_posts = sorted(posts_with_likes, key=lambda post: post.count_likes(), reverse=True)
    popular_posts = sorted_posts[:5]
    all_posts = Post.query.order_by(Post.created_at.desc()).all()
    
    return render_template('home.html', 
                           daily_tip=daily_tip,
                           recent_posts=recent_posts,
                           popular_posts=popular_posts,
                           all_posts=all_posts)


@api.route('/allposts')
@login_required
def all_posts():
    """Render the all-posts page"""
    all_posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('all_posts.html', posts=all_posts)


@api.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Render the user profile page"""
    user = User.query.get(current_user.id)
    if request.method == 'POST':
        data = request.form
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.bio = data.get('bio', user.bio)
        user.profile_picture = data.get('profile_picture', user.profile_picture)
        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('api.profile'))
    return render_template('profile.html', user=user)


@api.route('/user/<username>')
@login_required
def view_user_profile(username):
    """Handles view of users profile through herf"""
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user, view_only=True)


@api.route('/writing_zone', methods=['GET'])
@login_required
def dashboard():
    """Render the writingzone page with user posts and daily challenge"""
    user_posts = Post.query.filter_by(user_id=current_user.id).all()
    posts_data = [{'id': post.id, 'title': post.title, 'image_url': post.image_url} for post in user_posts]
    daily_challenge = Challenge.query.order_by(Challenge.created_at.desc()).first()

    return render_template('dashboard.html', posts_data=posts_data, daily_challenge=daily_challenge)


@api.route('/posts/<int:post_id>', methods=['GET'])
@login_required
def get_post(post_id):
    """Render the post page to view post with certain id"""
    post = Post.query.options(joinedload(Post.author)).get_or_404(post_id)
    return render_template('post.html', post=post)


@api.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    """Render the create new post page"""
    if request.method == 'POST':
        data = request.form
        new_post = Post(title=data['title'], content=data['content'], image_url=data['image_url'], user_id=current_user.id)
        try:
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('api.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating post: {str(e)}', 'error')
            return redirect(url_for('api.create_post'))

    return render_template('createpost.html')


@api.route('/update_post/<int:post_id>', methods=['POST'])
@login_required
def update_post(post_id):
    """Render the edit-post page"""
    data = request.form
    post = Post.query.get(post_id)
    if not post:
        flash('Post not found.', 'error')
        return redirect(url_for('api.dashboard'))

    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    post.image_url = data.get('image_url', post.image_url)
    db.session.commit()
    flash('Post updated successfully.', 'success')
    return redirect(url_for('api.get_post', post_id=post_id))


@api.route('/posts/<int:post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    """Handle delete post"""
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully.', 'success')
    return jsonify({'message': 'Post deleted'}), 200


@api.route('/posts/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    """Handle like/unlike feature"""
    post = Post.query.get_or_404(post_id)
    user_id = current_user.id
    like = Like.query.filter_by(post_id=post_id, user_id=user_id).first()
    
    if like:
        db.session.delete(like)
        db.session.commit()
        liked = False
    else:
        new_like = Like(post_id=post_id, user_id=user_id)
        db.session.add(new_like)
        db.session.commit()
        liked = True

    likes = Like.query.filter_by(post_id=post_id).all()
    liked_users = [{'username': like.user.username} for like in likes]

    return jsonify({'liked': liked, 'likes_count': post.count_likes(), 'liked_users': liked_users})


@api.route('/posts/<post_id>/comments', methods=['GET'])
def get_comments(post_id):
    """Display comments for post"""
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([comment.to_dict() for comment in comments]), 200


@api.route('/posts/<int:post_id>/comments', methods=['POST'])
@login_required
def create_comment(post_id):
    """Handle creation of a new comment"""
    data = request.json
    current_app.logger.debug(f'Received data: {data}')
    content = data.get('content')
    if not content:
        return jsonify({'message': 'Comment content is required.'}), 400

    user_id = current_user.id

    comment = Comment(content=content, user_id=user_id, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    flash('Comment updated successfully.', 'success')

    user = User.query.get(user_id)

    return jsonify({'id': comment.id, 'content': comment.content, 'user': {'username': user.username}}), 201


@api.route('/comments/<int:comment_id>', methods=['PUT'])
@login_required
def update_comment(comment_id):
    """Handle comment edit"""
    data = request.json
    content = data.get('content')

    comment = Comment.query.get(comment_id)
    if comment:
        comment.content = content
        db.session.commit()
        flash('Commment updated successfully.', 'success')
        return jsonify({'success': True, 'content': comment.content})
    else:
        return jsonify({'success': False, 'message': 'Comment not found'}), 404


@api.route('/comments/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    """Handle comment deletion"""
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    post_id = comment.post_id
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully.', 'success')
    return jsonify({'message': 'Comment deleted successfully', 'post_id': post_id})


@api.route('/challenges', methods=['GET'])
def get_challenges():
    """Render all-challenges page"""
    challenges = Challenge.query.all()
    return render_template('challenge.html', challenges=challenges)


@api.route('/challenges/daily', methods=['GET'])
def get_daily_challenge():
    """Handle daily challenge"""
    try:
        daily_challenge = Challenge.query.order_by(Challenge.created_at.desc()).first()
        if daily_challenge:
            return jsonify(daily_challenge.to_dict()), 200
        else:
            return jsonify({'message': 'No daily challenge available'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@api.route('/tips', methods=['GET'])
def get_tips():
    """Render all-tips page"""
    tips = Tip.query.all()
    return render_template('tips.html', tips=tips)


@api.route('/tips/daily', methods=['GET'])
def get_daily_tip():
    """Handle daily tip"""
    try:
        tip = Tip.query.order_by(Tip.created_at.desc()).first()
        if tip:
            return jsonify(tip.to_dict()), 200
        else:
            return jsonify({'message': 'No daily tip available'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
