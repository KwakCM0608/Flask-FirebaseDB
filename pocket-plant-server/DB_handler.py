import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

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
        }
        self.db.child("users").child(id).set(information)
        return True

    def write_post(self, writer, contents):
        pass
    def post_list(self):
        pass
    def post_detail(self, pid): # post id
        pass
    def get_user(self, uid): # user id
        pass