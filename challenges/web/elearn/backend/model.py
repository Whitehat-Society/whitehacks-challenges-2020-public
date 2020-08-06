from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


class Module(db.Model):
    code = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Module {self.name}>"


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    module_code = db.Column(db.String(20), db.ForeignKey('module.code'), nullable=False)
    module = db.relationship('Module', backref='lesson', lazy=True)

    def __repr__(self):
        return f"<Lesson {self.name} from Module {self.module.name}>"


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text(), nullable=False)
    is_draft = db.Column(db.Boolean(), default=True, nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    lesson = db.relationship('Lesson', backref='document', lazy=True)

    def __repr__(self):
        return f"<Document {self.name} from Lesson {self.lesson.name}>"


class Flag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flag = db.Column(db.String(30), nullable=False)


class ModuleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Module


class LessonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lesson


class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
