
import json, os, sys, time, datetime
from tinydb import TinyDB, Query
from usermgmt import UserMgmt

class UIutils:
    def __init__(self):
        self.db = TinyDB('users.json')
        self.speaker_table = self.db.table('speakers')

    def is_new_user(self):
        if len(self.speaker_table) == 2:
            return True
        else:
            return False
    
    def name_exist(self, name):
        speaker = Query()
        if self.speaker_table.contains(speaker.name == name):
            return True
        else:
            return False
    def get_table(self):
        return self.speaker_table

    def create_user(self, name, gender, phone, voice, permissions):
        self.speaker_table.insert({'name': name, 'gender':gender, 'voice': voice,'phone':phone,'intents': permissions})


    def get_user_list(self):
        speaker = Query
        users = []
        for user in self.speaker_table:
            users.append(user['name'])
        return users



class Styles:
    def applyButtonStyle():
    
        was =    """    QPushButton{
        border-radius:20px;
        border-color: rgb(0, 255, 255);
        }
        QPushButton:hover{
            border-color: rgb(0, 255, 255);
            color: black;
            background-color: rgb(170, 255, 255);
        }
        QPushButton:pressed {
            border-color: rgb(0, 255, 255);
            color: black;	
            background-color: rgb(0, 255, 255);
        }
        """
	















def main():
    utils = UIutils()

    choice = int(input("\n1. Create new user\n2. Get user list\n3. Exit\n"))
    if choice == 1:
        print('not now')
    elif choice == 2:
        utils.get_user_list()
    elif choice == 3:
        sys.exit(0)
    else:
        print('this option is not available')
        return main()

























if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramm wurde durch Benutzer beendet!")
        sys.exit(0)
    except Exception as e:
        print('Error: {}',e)
        exit(1)
    finally:
        sys.exit(0)
