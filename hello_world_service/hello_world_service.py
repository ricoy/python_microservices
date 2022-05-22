import os
from app import app
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    if os.getenv("ENVIRONMENT") == "prod":
        app.run()
    else:
        app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)
