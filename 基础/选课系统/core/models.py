#__author: Think
#date 2019/8/9


import os,sys

'''
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
'''

import pickle
from configs import settings
from core import identifier


class BaseModel:
    def save(self):
        nid = str(self.nid)
        file_path = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_path, 'wb')) #把obj对象保存到文件里面

'''
    @staticmethod
    def get_obj_list(self):             #obj对象列表
        ret = []
        for item in os.listdir(os.path.join(self.db_path)):
            obj = pickle.load(open(os.path.join(self.db_path, item), 'rb'))
            ret.append(obj)
        return ret
'''

class Admin(BaseModel):
    db_path = settings.ADMIN_DB
    def __init__(self,name,password):
        self.nid = identifier.AdminNid(Admin.db_path)
        self.name = name
        self.password = password

    @staticmethod
    def login(user, pwd):
        for item in os.listdir(os.path.join(Admin.db_path)):
            obj = pickle.load(open(os.path.join(Admin.db_path, item),'rb'))
            if user == obj.name and pwd == obj.password:
                return obj
        return None

class School(BaseModel):
    db_path = settings.SCHOOL_DB
    def __init__(self, address):
        self.nid = identifier.SCHOOLNid(School.db_path)
        self.schoolName = 'xx'
        self.school_address = address
        self.income = 0

    def __str__(self):
        return self.schoolName

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(os.path.join(School.db_path)):
            obj = pickle.load(open(os.path.join(School.db_path, item), 'rb'))
            ret.append(obj)
        return ret

class Teacher(BaseModel):
    db_path = settings.TEACHER_DB

    def __init__(self, name, password, gender, age, phonenumber):

        self.nid = identifier.TeacherNid(Teacher.db_path)
        self.name = name
        self.password = password
        self.gender = gender
        self.age = age
        self.phone = phonenumber

    def __str__(self):
        return self.name, self.gender, self.age, self.phone

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(os.path.join(Teacher.db_path)):
            obj = pickle.load(open(os.path.join(Teacher.db_path, item), 'rb'))
            ret.append(obj)
        return ret

class Classes(BaseModel):
    db_path = settings.CLASSES_DB

    def __init__(self, name, tuition, course_nid):
        self.nid = identifier.ClassesNid(Classes.db_path)
        self.name = name
        self.tuition = tuition
        self.course_nid = course_nid

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(os.path.join(Classes.db_path)):
            obj = pickle.load(open(os.path.join(Classes.db_path, item), 'rb'))
            ret.append(obj)
        return ret

class Course(BaseModel):
    db_path = settings.COURSE_DB

    def __init__(self, name, price, period, school_nid):
        self.nid = identifier.CourseNid(Course.db_path)
        self.courseName = name
        self.coursePrice = price
        self.coursePeriod = period
        self.school_nid = school_nid

    def __str__(self):
        return "课程名：%s；课程价格：%s；课程周期：%s；所属学区：%s" % (
            self.courseName, self.coursePrice, self.coursePeriod, self.school_nid.get_obj_by_uuid().school_address)

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(os.path.join(Course.db_path)):
            obj = pickle.load(open(os.path.join(Course.db_path, item), 'rb'))
            ret.append(obj)
        return ret

class CourseToTeacher(BaseModel):
    db_path = settings.COURSE_TO_TEACHER_DB

    def __init__(self, course_nid, teacher_nid, classes_nid):
        self.nid = identifier.CourseToTeacherNid(CourseToTeacher.db_path)
        self.course_nid = course_nid
        self.teacher_nid = teacher_nid
        self.classes_nid = classes_nid

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(os.path.join(CourseToTeacher.db_path)):
            obj = pickle.load(open(os.path.join(CourseToTeacher.db_path, item), 'rb'))
            ret.append(obj)
        return ret

class Score:
    def __init__(self, student_id):
        self.studentId = student_id
        self.score_dict = {}

    def set(self, course_to_teacher_nid, number):
        self.score_dict[course_to_teacher_nid] = number

    def get(self, course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid, None)


class Student(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, name, password, age, classes_id):
        self.nid = identifier.StudentNid(Student.db_path)
        self.name = name
        self.password = password
        self.age = age
        self.classesId = classes_id
        self.score = Score(self.nid)

    @staticmethod
    def register():
        pass







