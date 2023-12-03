from pathlib import Path

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")

LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = Path(LOGS_DIR, 'log.log')

OUT_DIR = Path(BASE_DIR, "Base")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = Path(OUT_DIR, 'news')

#Logging
FORMAT = '%(asctime)s:%(levelname)s:%(message)s'

#Time
TIMEOUT = 120