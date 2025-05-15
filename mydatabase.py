import json

class Database:
    def File_Register(self, Name, Email, Password):
        with open(r"D:\NLPApp\database.json", "r") as F1:
            data= json.load(F1)
        if Email in data:
            return False
        else:
            data[Email]=[Name, Password]
            with open(r"D:\NLPApp\database.json", "w") as F1:
                json.dump(data, F1)
            return True

    def Check_Credentials(self, email, password):
        with open(r"D:\NLPApp\database.json", "r") as F1:
            data=json.load(F1)
        if email in data and data[email][1]==password:
            return True
        else:
            return False
