import os

API_ID = API_ID = 10577960

API_HASH = os.environ.get("API_HASH", "80fd047285f4e94ca80311928b6bb5da")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6057552780:AAFaoMpd88jH8cHlRR4kNeoku4Rl46en4MA")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 5917311887))

LOG = -1001911414728

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5917311887").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
