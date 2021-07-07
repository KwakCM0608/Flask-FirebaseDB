import pyrebase
import json
import uuid

class DBModule:

    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

        def noquote(s):
            return s

        pyrebase.pyrebase.quote = noquote

    def login(self, uid, pwd):
        users=self.db.child("users").get().val()
        try:
            userinfo = users[uid]
            if userinfo["pwd"] == pwd:
                return True
            else:
                return False
        except:
            return False

    def signin(self, id, pwd, name, email):
        
        information = {
            "pwd" : pwd,
            "uname" : name,
            "email" : email
            #"plant_list" : {},
        }
        self.db.child("users").child(id).set(information)
        return True

    def plant_list(self, id):
        #plants = self.db.child("plants").get().val()
        query = self.db.child('plants').order_by_child('owner_id').equal_to(id)
        plantinfo = query.get().val()
        if len(list(plantinfo)) > 0:
            plantlist = {}
            for plantid in list(plantinfo):
                print(plantinfo[plantid])
                plantlist[plantid] = plantinfo[plantid]
            return plantlist
        else:
            return {} # Should be return other else

    def create_plant(self, id, plantname, plantkind):
        pid = str(uuid.uuid4())[:10]     # plantid
        print("Create plant id : " + pid)
        information = {
            "owner_id" : id,
            "name" : plantname,
            "kind" : plantkind,
            "grow_rate" : 0,
            "age" : 0,
            "life_rate" : 100,       # 100 %
            "max_height" : 0,
        }
        information['max_height'] = 30
        self.db.child("plants").child(pid).set(information)
        return True

    def write_post(self, writer, contents):
        pass

    def post_list(self):
        pass
    
    def post_detail(self, pid): # post id
        pass
    
    def get_user(self, uid): # user id
        pass