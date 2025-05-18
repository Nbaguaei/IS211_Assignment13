from flask import Flask, render_template, redirect, url_for, request, session, flash
from models import db, User, Post
from forms import LoginForm, PostForm
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

with app.app_context():
    db.create_all()

# Helper
def current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

@app.route('/')
def index():
    posts = Post.query.filter_by(published=True).order_by(Post.published_date.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if not current_user():
        return redirect(url_for('login'))
    posts = Post.query.filter_by(user_id=current_user().id).all()
    return render_template('dashboard.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if not current_user():
        return redirect(url_for('login'))
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            published=form.published.data,
            user_id=current_user().id
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('new_post.html', form=form)

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    if not current_user():
        return redirect(url_for('login'))
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user().id:
        return redirect(url_for('dashboard'))

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.published = form.published.data
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_post.html', form=form)

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    if not current_user():
        return redirect(url_for('login'))
    post = Post.query.get_or_404(post_id)
    if post.user_id == current_user().id:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/unpublish/<int:post_id>')
def unpublish_post(post_id):
    if not current_user():
        return redirect(url_for('login'))
    post = Post.query.get_or_404(post_id)
    if post.user_id == current_user().id:
        post.published = False
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    if not post.published:
        return "This post is not published", 404
    return render_template('view_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
