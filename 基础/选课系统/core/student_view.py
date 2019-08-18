#__author: Think
#date 2019/8/12
from configs import settings
from core import models


def student_run():
    while True:
        print('\033[1;35m{}\033[0m'.format(settings.student_user_page))
        admin_login_choice = input("\033[1;34m请输入你的选择： \033[0m").strip()
        if admin_login_choice == '1':
            student_add()
        elif admin_login_choice == '2':
            student_login()
        elif admin_login_choice == '3':
            pass
        elif admin_login_choice == 'r':
            print('用户退出！')
            print('\033[1;35m{}\033[0m'.format(settings.student_user_page))
            break
        else:
            print("\033[1;31m您的输入不正确。\033[0m")

def student_add():
    print("\033[1;31m欢迎注册本校为学员。\033[0m")
    name = input('请输入学员名称：')
    pwd = input('请输入学员密码：')
    age = input('请输入学员年龄：')
    phone = input('请输入学员电话：')

    course_class_teacher_list = models.CourseToTeacher.get_all_list()
    for k, obj in enumerate(course_class_teacher_list):
        print(k, '\033[33;1m 课程[%s] 班级[%s] 导师[%s]\033[0m' % (obj.course_nid.get_obj_by_uuid().courseName, \
                                                         obj.classes_nid.get_obj_by_uuid().name, \
                                                         obj.teacher_nid.get_obj_by_uuid().name))

    cid = int(input('请选择对应课程班级导师：'))
    course_class_teacher_obj = course_class_teacher_list[cid]

    obj = models.Student(name, pwd, age, phone, course_class_teacher_obj.nid)
    obj.save()
    print("学员账号注册成功")

def student_login():
    print("欢迎登录学员系统！")
    u = input("\033[1;34m请输入登录学员账号:")
    p = input("\033[1;34m请输入登录学员密码:")
    if models.Student.login(u, p):
        print("\033[1;34m学员登录成功！\033[0m")
        student_system(u)

def student_system(u):
    while True:
        print('\033[1;35m{}\033[0m'.format(settings.student_info_page))
        student_system_choice = input("\033[1;34m请输入你的选择： \033[0m").strip()
        if student_system_choice == '1':
            show_coure_class_teacher(u)
        elif student_system_choice == '2':
            pass
        elif student_system_choice == 'r':
            print('用户退出！')
            print('\033[1;35m{}\033[0m'.format(settings.admin_user_page))
            break
        else:
            print("\033[1;31m您的输入不正确。\033[0m")

def show_coure_class_teacher(u):
    print("\033[1;35m所选课程为: \033[0m")
    for obj in models.Student.get_all_list():
        if obj.name == u:
            print('\033[33;1m 课程[%s] 班级[%s] 导师[%s]\033[0m' % (obj.course_to_teacher_nid.get_obj_by_uuid().course_nid.get_obj_by_uuid().courseName, \
                                                         obj.course_to_teacher_nid.get_obj_by_uuid().classes_nid.get_obj_by_uuid().name, \
                                                         obj.course_to_teacher_nid.get_obj_by_uuid().teacher_nid.get_obj_by_uuid().name))

