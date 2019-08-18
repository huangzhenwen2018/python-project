#__author: Think
#date 2019/8/9
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB = os.path.join(BASEDIR,'db','admin')
SCHOOL_DB = os.path.join(BASEDIR,'db','school')
COURSE_DB = os.path.join(BASEDIR,'db','course')
COURSE_TO_TEACHER_DB = os.path.join(BASEDIR, 'db', 'course_to_teacher')
CLASSES_DB = os.path.join(BASEDIR, 'db', 'class')
STUDENT_DB = os.path.join(BASEDIR, 'db', 'student')
TEACHER_DB = os.path.join(BASEDIR, 'db', 'teacher')

main_page = '''
           欢迎进入xx大学选课系统!

            1.学员视图
            2.讲师视图
            3.管理视图
            q.系统退出
            '''

admin_user_page = '''
            欢迎进入管理员账号管理!

            1:账号注册
            2:账号登录
            3:账号销账
            r:返回上一级
            q:系统退出 
            '''

admin_school_page = '''
            欢迎进入学校系统!

            1:添加校区
            2:管理学校
            3:校区列表
            4.删除校区
            r:用户退出           
            '''

manage_school_page = '''
                欢迎进入学校管理!
                
                1:添加讲师
                2:添加班级
                3:添加课程
                4:查看讲师列表
                5:查看班级列表
                6:查看学校开设课程列表
                7:删除讲师
                8:删除班级
                9:删除课程
                10:关联讲师课程班级信息
                11:查看讲师课程班级列表
                r:返回上级
                '''

teach_view_page = '''
            欢迎进入教师管理系统!

            1:查看负责班级信息
            2:查看负责学生信息
            3:学生成绩评级
            4.查看学生成绩
            r:退出           
            '''

student_user_page = '''
            欢迎进入学生账号管理系统!

            1:账号注册
            2:账号登录
            3:账号销账
            r:返回上一级
            q:系统退出 
            '''
student_info_page = '''
            欢迎进入学生系统!

            1:查看所选课程
            2:交学费
            3:查成绩
            r:返回上一级
            q:系统退出 
            '''