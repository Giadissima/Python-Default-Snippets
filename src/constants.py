from os.path import join, dirname, isabs
from os import getenv
from src.parser import Parser

import __main__

# questa funzione controlla se esiste una variabile d'ambiente associata al nome, 
# oppure un argomento passato da linea di comando, altrimenti, ritorna il valore di default
def check_if_env_or_arg(name, name_env, args, default):
    if args!= None and args[name] != None:
        return args[name]
    if getenv(name_env) != None:
        if isinstance(default, float):
            return float(getenv(name_env)) 
        if isinstance(default, int):
            return int(getenv(name_env))       
        if isinstance(default, bool):
            return bool(getenv(name_env))
        if isinstance(default, list):
            return list(getenv(name_env).split(" "))
        return getenv(name_env)
    return default

# join two path if the second path is relative, otherwise return only the secind path
def check_if_abs(arg_to_join, possible_abs_path):
    if(isabs(possible_abs_path)):
        return possible_abs_path
    return join(arg_to_join, possible_abs_path)
  
parser = Parser()
args = parser.arguments()

# Path
BASE_PATH = check_if_abs(dirname(__main__.__file__), check_if_env_or_arg("basepath", "BASE_PATH", args, "src"))
IMAGES_PATH = check_if_abs(BASE_PATH, check_if_env_or_arg("imagespath", "IMAGES_PATH", args, join(BASE_PATH, "tester_img")))
BASE_LOG_PATH = check_if_env_or_arg("logpath", "LOG_PATH", args, "log")
LOG_PATH = join(BASE_LOG_PATH, "debug.log")
ERROR_LOG_PATH = join(BASE_LOG_PATH, "error.log")
DEV_MODE = check_if_env_or_arg("dev_mode", "DEV_MODE", args, "True")
DEV_MODE = DEV_MODE.lower() == 'true'

# IMAGES
IMG_CATEGORIES = check_if_env_or_arg("imgcategories", "IMG_CATEGORIES", args, ['pippo', 'jack'])
IMG_SIZE = check_if_env_or_arg("imagesize", "IMG_SIZE", args, 100)

