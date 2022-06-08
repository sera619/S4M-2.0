from loguru import logger
import json, os, sys, time, datetime
from tinydb import TinyDB, Query, where
from tinydb.operations import set as tset
from usermgmt import UserMgmt


class UIutils:
    def __init__(self):
        self.db = TinyDB('users.json')
        self.speaker_table = self.db.table('speakers')

    def delete_user(self, user):
        speaker = Query()
        self.speaker_table.remove(speaker.name == user)
        logger.debug('\nUser: ' +str(user)+ ' deleted!')

    def edit_name(self,user,name):
        speaker = Query()
        edit_user = self.speaker_table.get(speaker.name == str(user))
        edit_user['name'] = name
        self.speaker_table.update(edit_user,speaker.name == str(user))
        logger.debug('\nnew username set : ', name)

    def edit_number(self, user, number):
        speaker = Query()
        edit_user = self.speaker_table.get(speaker.name == str(user))
        edit_user['phone'] = number
        self.speaker_table.update(edit_user,speaker.name == str(user))
        logger.debug('\nnew number set at '+user+ ' : '+str(number))

    def edit_lang(self, user, lang):
        speaker = Query()
        edit_user = self.speaker_table.get(speaker.name == str(user))
        edit_user['language'] = lang
        self.speaker_table.update(edit_user,speaker.name == str(user))

    def edit_permissions(self, user, permissions = False):
        speaker = Query()
        edit_user = self.speaker_table.get(speaker.name == str(user))
        if permissions:
            edit_user['intents'] = "[*]"
            self.speaker_table.update(edit_user,speaker.name == str(user))
            logger.debug('\nUser '+user+' is not a guest anymore')

        else:
            edit_user['intents'] = "['animalsounds','gettime']"
            self.speaker_table.update(edit_user,speaker.name == str(user))
            logger.debug('\nUser '+user+' is now a guest')

    def edit_gender(self, user, gender):
        speaker = Query()
        edit_user =self.speaker_table.get(speaker.name ==str(user))
        edit_user['gender'] = gender
        logger.debug('\nnew gender set at '+ user + ' : ' + str(gender))

    def edit_mail(self, user, mail):
        speaker = Query()
        edit_user = self.speaker_table.get(speaker.name == str(user))
        edit_user['mail'] = mail
        logger.debug('\nnew mail set at '+user+ ' : '+str(mail))

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

    def get_user_mail(self, name):
        speaker = Query()
        user = self.speaker_table.search(speaker.name == str(name))
        usermail =  user[0]['mail']
        return str(usermail)

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

    def create_user(self, name, gender, phone, voice, permissions, lang, mail):
        self.speaker_table.insert({'name': name, 'gender':gender, 'voice': voice,'phone':phone,'intents': permissions,'language':lang,'mail':mail})


    def get_user_list(self):
        speaker = Query
        users = []
        for user in self.speaker_table:
            users.append(user['name'])
        if len(users) == 2:
            users = []
        logger.debug(users)
        return users


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
