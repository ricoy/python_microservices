import os
from app import app
from dotenv import load_dotenv

load_dotenv()

app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
