from flask import Flask, render_template

from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")


def main():
    session = db_session.create_session()

    surname_list = ['Scott', 'Smith', 'Johnson', 'Williams', 'Jones']
    name_list = ['Ridley', 'Liam', 'William', 'Benjamin', 'Mason']
    age_list = [21, 34, 44, 29, 22]
    position_list = ['captain', 'navigator', 'medic', 'shooter', 'motor mechanic']
    speciality_list = ['research engineer', 'scout', 'medic', 'defender', 'engineer']
    email_list = ['scott_chief@mars.org', 'smith@mars.org', 'johnson@mars.org',
                  'williams@mars.org', 'jones@mars.org']

    for i in range(len(surname_list)):
        user = User()
        user.id = i + 1
        user.surname = surname_list[i]
        user.name = name_list[i]
        user.age = age_list[i]
        user.position = position_list[i]
        user.speciality = speciality_list[i]
        user.address = f"module_1"
        user.email = email_list[i]
        session.add(user)
        session.commit()

    job_list = ['deployment of residential modules 1 and 2', 'scout the nearby area',
                'study the composition of the soil', 'repair of the 4-th engine']
    work_size = [15, 15, 10, 20]
    user_id_list = [1, 2, 3, 5]
    collaborators_list = ['1, 4', '2', '3', '1, 5']
    is_finished_list = [True, True, False, False]

    for i in range(len(job_list)):
        user = session.get(User, user_id_list[i])
        job = Jobs()
        job.team_leader = f"{user.surname} {user.name}"
        job.job = job_list[i]
        job.work_size = work_size[i]
        job.collaborators = collaborators_list[i]
        job.is_finished = is_finished_list[i]
        job.user_id = user_id_list[i]
        session.add(job)
        session.commit()
    app.run()

@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs)
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    main()
