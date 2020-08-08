from flask import Blueprint,render_template
from models import Post
from flask_login import login_required, current_user


main=Blueprint('main', __name__)
@main.route("/")
@main.route("/home")
def home():

    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/jobs")
def jobs():

    jobs = Post.query.all()

    return render_template('jobs.html', title='Jobs', jobs=jobs,
                            quantity=len(jobs))


@main.route('/<int:id>')
def personal(id):
    jobs = Post.query.get(id)
    return render_template('job.html', job=jobs)