#__author: Think
#date 2019/8/12

from core import models
from configs import settings

def teacher_run():
    print('教师界面'.center(60, '-'))
    teacher_name = input('请输入姓名:').strip()
    teacher_password = input('请输入登陆密码:').strip()
    teacher_list = models.Teacher.get_all_list()

    ret = []
    for obj in teacher_list:
        ret.append((obj.name, obj.password))
    if (teacher_name, teacher_password) in ret:
        teacher_main(teacher_name)
    else:
        print('用户名密码无效！')

def teacher_main(teacher_name):
    res = models.CourseToTeacher.get_all_list()
    for obj in res:
        if obj.teacher_nid.get_obj_by_uuid().name == teacher_name:
            teacher_nid = obj.teacher_nid
    while True:
        print('\n\033[1;31m欢迎您%s\033[0m\n'%teacher_nid.get_obj_by_uuid().name)
        print('\033[1;35m{}\033[0m'.format(settings.teach_view_page))
        your_input = input("\033[1;34m请输入你的选择: \033[0m").strip()
        if your_input == '1':
            print('\033[33;1m 你所负责班级信息：\033[0m')
            classes_info(teacher_nid)
        elif your_input == '2':
            pass
        elif your_input == '3':
            pass
        elif your_input == 'r':
            print('\033[1;34m退出成功！\033[0m')
            break
        else:
            print("\033[1;31m您的输入不正确。\033[0m")

def classes_info(teacher_nid):
    classes_list = []
    for obj in models.CourseToTeacher.get_all_list():
        if obj.teacher_nid.get_obj_by_uuid().name == teacher_nid.get_obj_by_uuid().name:
            obj = obj.classes_nid
            classes_list.append(obj.get_obj_by_uuid())
    for obj in classes_list:
        print('\033[33;1m 课程[%s] 班级[%s] 学费[%s]\033[0m' %(obj.course_nid.get_obj_by_uuid().courseName, obj.name, obj.tuition))
