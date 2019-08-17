#__author: Think
#date 2019/8/12
import sys,os

from configs import settings
from core import models


def admin_run():
    while True:
        print('\033[1;35m{}\033[0m'.format(settings.admin_user_page))
        your_input = input("\033[1;34m请输入你的选择: \033[0m").strip()
        if your_input == '1':
            admin_user_add()
        elif your_input == '2':
            print("欢迎登录管理系统！")
            u = input("\033[1;34m请输入登录管理员账号:")
            p = input("\033[1;34m请输入登录管理员密码:")
            if models.Admin.login(u,p):
                print("\033[1;31m管理员登录成功！\033[0m")
                admin_login()
            else:
                print('\033[1;31m账号密码不正确或者不存在\033[0m')
        elif your_input == '3':
            pass
        elif your_input == 'r':
            print('返回上一级！')
            print('\033[1;35m{}\033[0m'.format(settings.main_page))
            break
        elif your_input == 'q':
            print('退出系统!')
            sys.exit()
        else:
            print("\033[1;31m您的输入不正确。\033[0m")

def admin_user_add():
    user = input('请输入管理员名称：')
    pwd = input('请输入管理员密码：')
    obj = models.Admin(user, pwd)
    obj.save()
    print("管理员账号注册成功")


def admin_login():
    while True:
        print('\033[1;35m{}\033[0m'.format(settings.admin_school_page))
        admin_login_choice = input("\033[1;34m请输入你的选择： \033[0m").strip()
        if admin_login_choice == '1':
            creat_school()
        elif admin_login_choice == '2':
            manage_school()
        elif admin_login_choice == '3':
            show_school()
        elif admin_login_choice == '4':
            pass
        elif admin_login_choice == 'r':
            print('用户退出！')
            print('\033[1;35m{}\033[0m'.format(settings.admin_user_page))
            break
        else:
            print("\033[1;31m您的输入不正确。\033[0m")

def creat_school():
    school_address = input("\033[1;33m请输入学校校区地址：\033[0m")
    obj = models.School(school_address)
    obj.save()

def show_school():
    school_list = models.School.get_all_list()
    print("\033[1;33m当前学校校区列表如下： \n\033[0m")
    for obj in school_list:
        print("\033[1;33m学校名称：%s\033[0m" % obj.schoolName,"\033[1;33m学校校区：%s\033[0m" % obj.school_address)

def delete_school():
    pass

def manage_school():
    while True:
        print('\033[1;35m{}\033[0m'.format(settings.manage_school_page))
        manage_school_choice = input("\033[1;34m请输入你的选择： \033[0m").strip()
        if manage_school_choice == '1':
            add_teacher()
        elif manage_school_choice == '2':
            add_class()
        elif manage_school_choice == '3':
            add_course()
        elif manage_school_choice == '4':
            show_teacher()
        elif manage_school_choice == '5':
            show_class()
        elif manage_school_choice == '6':
            show_course()
        elif manage_school_choice == '7':
            delete_teacher()
        elif manage_school_choice == '8':
            delete_class()
        elif manage_school_choice == '9':
            delete_course()
        elif manage_school_choice == '10':
            add_course_teacher()
        elif manage_school_choice == '11':
            course_teacher_list()
        elif manage_school_choice == 'r':
            print('用户退出！')
            print('\033[1;35m{}\033[0m'.format(settings.admin_school_page))
            break
        else:
            print("\033[1;31m您的输入不正确。\033[0m")

def add_teacher():
    teacher_name = str(input("\033[1;35m请输入讲师姓名:\033[0m").strip())
    teacher_passwd = str(input("\033[1;35m请输入讲师登录密码:\033[0m").strip())
    teacher_gender = str(input("\033[1;35m请输入讲师性别:\033[0m").strip())
    teacher_age = str(input("\033[1;35m请输入讲师年龄:\033[0m").strip())
    teacher_phonenumber = str(input("\033[1;35m请输入讲师电话号码:\033[0m").strip())
    obj = models.Teacher(teacher_name,teacher_passwd,teacher_gender,teacher_age,teacher_phonenumber)
    obj.save()
    print('\033[1;35m 添加讲师成功\033[0m')

def show_teacher():
    print("\033[1;35m当前教师列表如下: \033[0m")
    teacher_list = models.Teacher.get_all_list()
    for obj in teacher_list:
        print('''\033[1;35m讲师名称：{} 讲师性别：{} 讲师年龄：{} 讲师电话号码：{}\033[0m'''.format(obj.name, obj.gender, obj.age, obj.phone))

def delete_teacher():
    pass

def add_course():
    school_list = models.School.get_all_list()
    for k, obj in enumerate(school_list):
        print('\033[1;35m校区编号; %d \033[0m' % k, '\033[1;35m校区: %s \033[0m' % obj.school_address)
    sid = int(input('\033[1;35m请选择创建课程的校区编号: \033[0m'))
    school_obj = school_list[sid]
    print("\033[1;33m所选择校区为：\033[0m", school_obj.school_address)

    name = input('\033[1;35m请输入课程名: \033[0m').strip()
    price = input('\033[1;35m请输入课程价格: \033[0m').strip()
    period = input('\033[1;35m请输入课程周期: \033[0m').strip()

    course_name_list = []
    for obj in models.Course.get_all_list():
        course_name_list.append((obj.courseName, obj.school_nid.uuid))
    if (name, school_obj.nid.uuid) in course_name_list:
        print('课程已经存在！')
    else:
        obj = models.Course(name, price, period, school_obj.nid)
        obj.save()
        print('\033[33;1m[%s]课程 创建成功\033[0m' % obj.courseName)

def show_course():
    course_obj_list = models.Course.get_all_list()
    for obj in course_obj_list:
        print('\033[33;1m[%s] [%s] [%s]课程 价格[%s] 周期[%s]\033[0m' \
              % (obj.school_nid.get_obj_by_uuid().schoolName, obj.school_nid.get_obj_by_uuid().school_address, \
                 obj.courseName, obj.coursePrice, obj.coursePeriod))

def delete_course():
    school_adress = input('\033[1;35m输入需删除的课程校区: \033[0m').strip()
    course_name = input('\033[1;35m输入需删除的课程名: \033[0m').strip()
    course_obj_list = models.Course.get_all_list()
    course_name_list = []
    for obj in course_obj_list:
        if school_adress == obj.school_nid.get_obj_by_uuid().school_address and course_name == obj.courseName:
            os.remove(os.path.join(settings.COURSE_DB,obj.nid.uuid))
            print('删除成功')

def add_course_teacher():
    # get course list
    course_list = models.Course.get_all_list()
    for k, obj in enumerate(course_list):
        print(k, obj.courseName)
    cid = int(input('请输入课程：'))
    course_obj = course_list[cid]

    # get teacher list
    teacher_list = models.Teacher.get_all_list()
    for k, obj in enumerate(teacher_list):
        print(k, obj.name)
    tid = int(input('请选择关联老师：'))
    teacher_obj = teacher_list[tid]

    # get classes list
    classes_list = models.Classes.get_all_list()
    for k, obj in enumerate(classes_list):
        print(k, obj.name)
    sid = int(input('请选择负责的班级：'))
    classes_obj = classes_list[sid]

    obj = models.CourseToTeacher(course_obj.nid, teacher_obj.nid, classes_obj.nid)
    obj.save()
    print('\033[33;1m课程[%s] 班级[%s] 导师[%s] 分配成功\033[0m' % (course_obj.courseName, classes_obj.name, teacher_obj.name))

def course_teacher_list():
    print("\033[33;1m 课程讲师列表信息：\033[0m")
    for obj in models.CourseToTeacher.get_all_list():
        print('\033[33;1m 课程[%s] 班级[%s] 导师[%s]\033[0m' % (obj.course_nid.get_obj_by_uuid().courseName, \
                                                         obj.classes_nid.get_obj_by_uuid().name, \
                                                         obj.teacher_nid.get_obj_by_uuid().name))

def add_class():
    try:
        print('创建班级'.center(60, '-'))
        course_list = models.Course.get_all_list()
        for k, obj in enumerate(course_list):
            print(k, obj.courseName)
        cid = int(input('请选择课程：'))
        course_obj = course_list[cid]
        name = input('请输入班级名:').strip()
        tuition = input('请输入学费:').strip()

        #class_list_name = models.Classes.get_all_list()
        class_list_name = [obj.name for obj in models.Classes.get_all_list()]
        if name in class_list_name:
            raise Exception('\033[43;1m班级[%s] 已存在，不可重复创建\033[0m' % name)
        obj = models.Classes(name, tuition, course_obj.nid)
        obj.save()
        print('课程创建成功！')
        status = True
        error = ''
        data = '\033[33;1m班级[%s] 学费[%s] 创建成功\033[0m' % (obj.name, obj.tuition)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_class():
    for obj in models.Classes.get_all_list():
        print("\033[33;1m 班级列表信息：\033[0m")
        print('\033[33;1m 课程：[%s] 班级：[%s] 学费：[%s]\033[0m' \
              % (obj.course_nid.get_obj_by_uuid().courseName, obj.name, obj.tuition))

def delete_class():
    pass