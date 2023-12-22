# Environment variables using Python
# doc: https://pypi.org/project/python-dotenv/
# Never send your .env file to a remote repo
# Always create .env-example
from dotenv import load_dotenv
import os

load_dotenv()

#print(os.environ)
print(os.getenv("DB_PASSWORD"))