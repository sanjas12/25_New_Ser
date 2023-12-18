import os.path
from pathlib import Path

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
# print(BASE_DIR)

LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = Path(LOGS_DIR, 'log')



# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = Path(BASE_DIR, "database")
DATABASE_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = os.path.join(DATABASE_DIR, "base_news.db")
LOCAL_BASE_FILE = Path(DATABASE_DIR, 'localbase_title.txt')
print(LOCAL_BASE_FILE)

#Logging
FORMAT = '%(asctime)s:%(levelname)s:%(message)s'

#Time
TIMEOUT = 600   # 600 -default

