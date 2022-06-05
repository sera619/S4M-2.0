
import json, os, sys, time, datetime
from tinydb import TinyDB, Query
from usermgmt import UserMgmt

class UIutils:
    def __init__(self):
        self.db = TinyDB('users.json')
        self.speaker_table = self.db.table('speakers')
        self.user_to_edit = None

    def is_new_user(self):
        if len(self.speaker_table) == 2:
            return True
        else:
            return False
    def get_user_number(self, name):
        speaker = Query()
        user = self.speaker_table.search(speaker.name == str(name))
        userphone =  user[0]['phone']
        return str(userphone)

    def get_gender(self,name):
        speaker = Query()
        user = self.speaker_table.search(speaker.name == str(name))
        usergender =  user[0]['gender']
        if usergender == 'Mann':
            return 1
        else:
            return 0

    def is_user_guest(self,name):
        speaker = Query()
        user = self.speaker_table.search(speaker.name == str(name))
        userpermissions =  user[0]['intents']
        if userpermissions == "[*]":
            return False
        else:
            return True

    def get_user_lang(self,name):
        speaker = Query()
        user = self.speaker_table.search(speaker.name == str(name))
        userlang =  user[0]['language']
        if userlang == "de":
            return 1
        else:
            return 0

    def get_user(self, name):
        speaker = Query()
        user = self.speaker_table.search(speaker.name == str(name))
        self.user_to_edit =user
        return user 
    
    def name_exist(self, name):
        speaker = Query()
        if self.speaker_table.contains(speaker.name == str(name)):
            return True
        else:
            return False
        
    def get_table(self):
        return self.speaker_table

    def create_user(self, name, gender, phone, voice, permissions,lang):
        self.speaker_table.insert({'name': name, 'gender':gender, 'voice': voice,'phone':phone,'intents': permissions,'language':lang})


    def get_user_list(self):
        speaker = Query
        users = []
        for user in self.speaker_table:
            users.append(user['name'])
        if len(users) == 2:
            users = []
        print(users)
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
