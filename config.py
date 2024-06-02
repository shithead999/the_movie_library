from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

    OMDB_API_KEY = os.environ.get("OMDB_API_KEY") or ""

    OMDB_API_BASE = os.environ.get("OMDB_API_BASE") or "https://www.omdbapi.com/"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
