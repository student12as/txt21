import os

API_ID = API_ID = 10577960

API_HASH = os.environ.get("API_HASH", "80fd047285f4e94ca80311928b6bb5da")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5509916510:AAHroyKDRf7HaKq4Z79X3AhzoYXMefk6BpA")

PASS_DB = int(os.environ.get("PASS_DB", "ayush"))

OWNER = int(os.environ.get("OWNER", 1937257991))

LOG = -1001826939706

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1937257991").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
