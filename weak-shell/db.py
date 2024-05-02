import subprocess
import os

class Database:
    def __init__(self, dbcredits: str) -> None:
        self.folder = dbcredits
    def check_credentials(self, login: str, password: str) -> bool:
        try:
            true_password = subprocess.check_output(f'more {self.folder}\\{login}.txt' if os.name == 'nt' else f'cat {self.folder}/{login}.txt', shell=True).decode().replace('\r\n', '')
            print(true_password)
            return true_password == password
        except:
            return False