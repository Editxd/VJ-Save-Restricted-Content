import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "12380656"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority")
