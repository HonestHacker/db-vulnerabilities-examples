import pymongo

class Database:
    def __init__(self, dbcredits: str) -> None:
        self.connection = pymongo.MongoClient(dbcredits, 27017)
        self.db = self.connection['secret_app']
        self.credits = self.db['series']
    def check_credentials(self, login: str, password: str) -> bool:
        result = self.credits.find_one({"login" : login, "password" : password})
        print(result)
        return bool(result)