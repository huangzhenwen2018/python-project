#__author: Think
#date 2019/8/9
import settings
import identify
import pickle,os

class BaseModel:
    def save(self):
        nid = str(self.nid)
        file_path = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_path, 'wb')) #把obj对象保存到文件里面

    def get_obj_list(self):             #obj对象列表
        ret = []
        for item in os.listdir(os.path.join(self.db_path)):
            obj = pickle.load(open(os.path.join(self.db_path, item), 'rb'))
            ret.append(obj)
        return ret



class Admin(BaseModel):
    db_path = settings.ADMIN_DB
    def __init__(self,name,password):
        self.nid = identify.AdminNid(Admin.db_path)
        self.name = name
        self.password = password


a = Admin('admin','123')
a.save()
obj = a.get_obj_list()
print(obj[0].name)














