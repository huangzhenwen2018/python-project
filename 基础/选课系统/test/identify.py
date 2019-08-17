#__author: Think
#date 2019/8/9
import uuid,os,pickle

def create_uuid():
    return str(uuid.uuid1())

class Nid:
    def __init__(self,role,db_path):
        role_list = [
            'admin', 'school', 'teacher', 'course', 'course_to_teacher', 'classes', 'student'
        ]
        if role not in role_list:
            raise Exception('用户角色定义错误，选项为：%s' % ','.join(role_list))
        self.role = role
        # uuid= b515bd9e-86e5-11e6-9cf4-005056c00008
        self.uuid = create_uuid()
        self.db_path = db_path

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        for name in os.listdir(self.db_path):
            if name == self.uuid:
                return pickle.load(open(os.path.join(self.db_path,self.uuid),'rb'))



class AdminNid(Nid):
    def __init__(self,db_path):
        super(AdminNid,self).__init__('admin',db_path)
