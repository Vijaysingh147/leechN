import os

API_ID = API_ID = 23004101

API_HASH = os.environ.get("API_HASH", "a2e157e87728053027cbb156e41a832a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6933526246:AAH4rd7MTUfhIG5lSI4BdwVt47BKG8fVyI0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5409975736))

LOG = --1002036952917

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-4165928800 -100211644569').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5409975736 5442086114").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


