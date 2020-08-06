from flask_restful import Api, Resource

from flask_jwt import current_identity, jwt_required

from .model import (Document, DocumentSchema, Lesson, LessonSchema, Module,
                    ModuleSchema, db)


class ModulesResource(Resource):
    modules_schema = ModuleSchema(many=True)

    @jwt_required()
    def get(self):
        modules = Module.query.all()
        if 'admin' in current_identity.name.lower():
            flag = Module()
            flag.code = 'Flag'
            flag.name = 'WH2020{wh0_s@y5_5ing13_p@g3_@PP_i5nt_w3@k_t0_01d_vu1n5}'
            modules.insert(0, flag)
        return self.modules_schema.dump(modules)


class SearchResource(Resource):
    @jwt_required()
    def get(self, search):
        result = db.session.execute(f"SELECT * FROM module WHERE code LIKE '%{search}%' OR name LIKE '%{search}%'")
        return [dict(r) for r in result]


class ModuleResource(Resource):
    module_schema = ModuleSchema()

    @jwt_required()
    def get(self, code):
        module = Module.query.filter(Module.code == code).first()
        return self.module_schema.dump(module)


class LessonsResource(Resource):
    lessons_schema = LessonSchema(many=True)

    @jwt_required()
    def get(self, code):
        lessons = Lesson.query.filter(Lesson.module_code == code).all()
        return self.lessons_schema.dump(lessons)


class LessonResource(Resource):
    lesson_schema = LessonSchema()

    @jwt_required()
    def get(self, code, lesson_name):
        lesson = Lesson.query.filter(Lesson.module_code == code and Lesson.name == lesson_name).first()
        return self.lesson_schema.dump(lesson)


class DocumentsResource(Resource):
    documents_schema = DocumentSchema(many=True)

    @jwt_required()
    def get(self, code, lesson_name):
        documents = Document.query.join(Lesson) \
            .filter(Lesson.module_code == code) \
            .filter(Lesson.name == lesson_name)
        if current_identity.username != 'admin':
            documents = documents.filter(Document.is_draft == False)
        documents = documents.all()
        return self.documents_schema.dump(documents)


class DocumentResource(Resource):
    document_schema = DocumentSchema()

    @jwt_required()
    def get(self, code, lesson_name, document_name):
        document = Document.query.join(Lesson) \
            .filter(Lesson.module_code == code) \
            .filter(Lesson.name == lesson_name) \
            .filter(Document.name == document_name).first()
        return self.document_schema.dump(document)

    @jwt_required()
    def put(self, code, lesson_name, document_name):
        if current_identity.username != 'admin':
            return None, 401

        document = Document.query.join(Lesson) \
            .filter(Lesson.module_code == code) \
            .filter(Lesson.name == lesson_name) \
            .filter(Document.name == document_name).first()

        if not document.is_draft:
            return None, 405

        return {'flag': 'WH2020{@cc35S_15_gr@nt3d_t0_th3_ch0sEn}'}


api = Api(prefix='/api')
api.add_resource(ModulesResource, '/modules')
api.add_resource(SearchResource, '/modules/search/<string:search>')
api.add_resource(ModuleResource, '/modules/<string:code>')
api.add_resource(LessonsResource, '/modules/<string:code>/lessons')
api.add_resource(LessonResource, '/modules/<string:code>/lessons/<string:lesson_name>')
api.add_resource(DocumentsResource, '/modules/<string:code>/lessons/<string:lesson_name>/documents')
api.add_resource(DocumentResource, '/modules/<string:code>/lessons/<string:lesson_name>/documents/<string:document_name>')
