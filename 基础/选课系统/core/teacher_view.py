#__author: Think
#date 2019/8/12

from core import models
from configs import settings

def teacher_run():
    print('\033[1;35m欢迎进入教师系统！\033[0m')
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
            print('\033[33;1m你所负责班级信息：\033[0m')
            classes_info(teacher_nid)
        elif your_input == '2':
            print('\033[33;1m你所负责学生信息：\033[0m')
            s_list = student_info(teacher_nid)
            for obj in s_list:
                print("\033[33;1m学员: %s 年龄: %s 电话: %s 课程：%s 班级：%s\033[0m" % (obj.name, obj.age, obj.phone, \
                                                                             obj.course_to_teacher_nid.get_obj_by_uuid().course_nid.get_obj_by_uuid().courseName, \
                                                                             obj.course_to_teacher_nid.get_obj_by_uuid().classes_nid.get_obj_by_uuid().name))
        elif your_input == '3':
            print('\033[33;1m学生成绩评级：\033[0m')
            set_student_score(teacher_nid)
        elif your_input == '4':
            print('\033[33;1m查看学生成绩：\033[0m')
            show_student_score(teacher_nid)
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
    return classes_list

def student_info(teacher_nid):
    c_c_t_list = []
    s_list = []
    for obj in models.CourseToTeacher.get_all_list():
        if obj.teacher_nid.get_obj_by_uuid().name == teacher_nid.get_obj_by_uuid().name:
            c_c_t_list.append(obj.nid.uuid)

    for obj in models.Student.get_all_list():
        if obj.course_to_teacher_nid.uuid in c_c_t_list:
            s_list.append(obj)
    return s_list

def set_student_score(teacher_nid):
    s_list = student_info(teacher_nid)
    for k, obj in enumerate(s_list):
        print(k, "\033[33;1m学员: %s \033[0m" %obj.name)
    sid = int(input('\033[1;34m请选择需评级学生:\033[0m').strip())
    student_obj = s_list[sid]

    level = input("\033[1;34m请输入课程评分等级:\033[0m".strip())
    obj = models.Score(student_obj.nid)
    obj.set(student_obj.course_to_teacher_nid, level)
    obj.save_score_dict()
    print("\033[1;31m该学员评级成功！。\033[0m")

def show_student_score(teacher_nid):
    #s_list = student_info(teacher_nid)
    #for obj in s_list:
    #    print(obj.score.get(obj.course_to_teacher_nid))
    #obj_list = models.Score.get_all_list()
    pass





