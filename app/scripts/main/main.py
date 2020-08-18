from datetime import time
from flask import Blueprint, render_template, send_file, Response
from models import User, Post, Level, Category, Jobs_skills, Users_skills, Skills
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


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
    levels = Level.query.all()
    category = Category.query.all()
    # STEXARENQ
    return render_template('jobs.html', title='Jobs', jobs=jobs, levels=levels
                           )


@main.route('/<int:id>')
def personal(id):
    job = Post.query.get(id)
    print('aaaaaaa')
    jobs_skills = Jobs_skills.query.filter(Jobs_skills.job_id == str(id))
    a = [x.skill_id for x in jobs_skills]
    skills = [Skills.query.get(x).title for x in a]
    if current_user.is_authenticated:
        u_id = current_user.get_id()
        user_skills = Users_skills.query.filter(Users_skills.user_id == str(u_id))
        b = [x.skill_id for x in user_skills]
        b.append(379)
        # Model.query.filter(Model.columnName.contains('sub_string'))
        matching = round(len(set(a) & set(b)) / (float(len(set(a)))) * 100)
    else:
        matching=0
    return render_template('job.html', job=job, matching=matching, skills=skills)
