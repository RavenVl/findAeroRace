import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")
PATH_COMMUNITY = os.environ.get("PATH_COMMUNITY")
MICROSOFT_LOCATION = os.environ.get("MICROSOFT_LOCATION")
