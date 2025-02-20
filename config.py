from os import environ

API_ID = int(environ.get("API_ID", "26952240"))
API_HASH = environ.get("API_HASH", "d230e89f5a59dc7b03aa9a3f853d3397")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002295656951"))
ADMINS = int(environ.get("ADMINS", "7789729349"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://mdfahmedulislam:XAkJzWSqQ2rc6fkD@cluster0.hherf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
