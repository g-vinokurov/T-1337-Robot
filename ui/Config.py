
import dotenv
import pathlib

env = dotenv.dotenv_values('.env')

# Project config
PROJECT_DIR = pathlib.Path(__file__).absolute().parent

# Assets config
FONTS_DIR = PROJECT_DIR / 'Assets' / 'Fonts'
ICONS_DIR = PROJECT_DIR / 'Assets' / 'Icons'
IMAGES_DIR = PROJECT_DIR / 'Assets' / 'Images'

# Logging config
LOG_LVL = env.get('LOG_LVL', 'CRITICAL')
LOG_FILE = env.get('LOG_FILE', None)
LOG_FMT = env.get('LOG_FMT', '%(asctime)s %(levelname)s %(message)s')
