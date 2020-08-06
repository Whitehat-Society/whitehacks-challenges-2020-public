import os

from flask import Flask

from model import Document, Flag, Lesson, Module, User, db

filepath = 'db.sqlite3'

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FLASK_SQLALCHEMY_DATABASE_URI', f"sqlite:///{filepath}")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{filepath}"
db.init_app(app)
with app.app_context():
    if os.path.isfile(filepath):
        os.remove(filepath)

    db.create_all()
    obj = [
        Flag(flag='WH2020{0Ld_5ch00l_Sql1}'),
        User(name='Bob Tan', username='temp_acc', password='48c261c89d1e8dc0e94c6a1268fa03eb8ccc77b5b9d1e81fd014277dbe8ae9dd'),  # temp_pass
        User(name='Mr. GovTech', username='govtech', password='bc2ed3d70b2521dc828ebb32db8d8fd954c6b7a9fc63580e601b1863821bc34e'),  # govtech_strong_password
        User(name='Admin', username='admin', password='d2d7122a8c5c41186b18a6c64c0e9882d73f8b7bfa3c0709aa89ed0fe1521d4b'),  # super_duper_whitehacks_strong_password
        Module(code='IS200', name='Software Foundations'),
        Module(code='IS103', name='Computational Thinking'),
        Module(code='IS101', name='Seminar on Information Systems'),
        Module(code='WRIT001', name='Academic Writing'),
        Lesson(module_code='IS200', name='Lesson 01'),
        Lesson(module_code='IS103', name='Lesson 01'),
        Lesson(module_code='IS101', name='Lesson 01'),
        Lesson(module_code='WRIT001', name='Lesson 01'),
        Document(lesson_id=1, name='Document 01', is_draft=False, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'),
        Document(lesson_id=4, name='Document Flag', is_draft=True, content='NOTFLAG{youre_almost_there_try_harder}'),
    ]

    db.session.bulk_save_objects(obj)
    db.session.commit()
