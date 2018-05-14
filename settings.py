from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

CLIENT_ACCESS_TOKEN = os.getenv('CLIENT_ACCESS_TOKEN')
