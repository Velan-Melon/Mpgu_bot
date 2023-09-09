import os

from dotenv import load_dotenv

#Это присвоение токена
load_dotenv()
TOKEN = str(os.getenv("TOKEN"))

#здесь мы прописываем айди всех админов, которым будут приходить персональные сообщения
ADMIN_ID = [
    1141053973
]


ip = os.getenv("HOST")
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv("DATABASE"))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'